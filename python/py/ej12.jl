using Distributions
using DataFrames;
using Gadfly
function auc(h::(Range{Float64},Array{Int64,1}))
  freq=convert(Array{Float64,1},h[2])
  e=convert(Array{Float64,1},h[1])
  numbins=length(e)
  deltax=e[2:numbins]-e[1:(numbins-1)]
  sum(deltax.*freq)
end;
srand(1)
x=rand(Distributions.Gamma(3,1),10000)
xhist=hist(x,100)
nbins=length(xhist[1])
xauc=auc(xhist)
xvec=vec([z::Float64 for z in xhist[1]])
xdf=DataFrame(xmin=vec(xvec[1:(nbins-1)]),xmax=vec(xvec[2:nbins]),count=xhist[2])
xdf[:dens]=xdf[:count]/xauc;
Gadfly.plot(layer(x=xdf[:xmin],y=xdf[:dens],Geom.bar,Theme(default_color=color("lightgray"))),
layer(x=xp[:x],y=xp[:dens],Geom.line,Theme(default_color=color("orange"))))


