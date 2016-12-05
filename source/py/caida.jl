function ball()
  g  = 9.81
  v0 = 10
  ym = v0^2/(2*g)
  tm = (2*v0)/g
  dt = 0.02
  t  = Float64[]
  y  = Float64[]
  local n = length(t)
  for i in 0:n
     while(y[i] >-0.01)
          t[i] += dt
          y[i] = v0*t[i] - 0.5*g*t[i]^2
          if(y[i]< -0.01)
            break
          end
      end
   end
end
