using LaTeX

x = linspace(-6,6,100)
y = sin(x)./x

import Winston
w = Image([], 7, Winston.plot(x, y))

import Gadfly
g = Image(7, 7, Gadfly.plot(x = x, y = y))

# needs pygments to be installed
c = Code("""
type MyJuliaType
    a::Array{Int}
end
""")

openpdf(report(
    Section("Results", {
        Section("Plots", Figure("Plot comparison",Tabular({w,g}))),
        Section("Code", c)
})))
