import pandapower.networks as nw1
import pandapower as pp
from pandapower.plotting import simple_plot, simple_plotly, pf_res_plotly
net1 = nw1.mv_oberrhein()
pp.runpp(net1)
print(net1.res_bus)
highest = net1.res_bus.vm_pu.max()
print(highest)
highest_ones = net1.res_bus.loc[net1.res_bus.vm_pu>1.02]
print(highest_ones)
lines = net1.res_line.loc[net1.res_line.loading_percent>50.]
print(lines)
simple_plot(net1)
simple_plotly(net1)
print()
