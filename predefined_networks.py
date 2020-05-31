import pandapower.networks as nw
import pandapower as pp
net = nw.simple_four_bus_system()
pp.runpp(net)
print(net.res_bus)
print(net)
