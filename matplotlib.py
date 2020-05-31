import pandapower.networks as nw
import pandapower.plotting as plot
import matplotlib.pyplot as plt
import seaborn
colours = seaborn.color_palette()

net = nw.mv_oberrhein()
bc = plot.create_bus_collection(net, buses=net.bus.index, color=colours[0], size=80, zorder=1)
lc = plot.create_line_collection(net, lines=net.line.index, color='grey', zorder=2)

long_lines = net.line.loc[net.line.length_km > 2.].index
lc1 = plot.create_line_collection(net, lines=long_lines, color=colours[2], zorder=2)
plot.draw_collections([lc, bc, lc1])
plt.show()