import pandapower as pp

net = pp.create_empty_network()

bus1 = pp.create_bus(net, name="HV Busbar", vn_kv=110, type="b")
bus2 = pp.create_bus(net, name="HV Busbar 2", vn_kv=110, type="b")
bus3 = pp.create_bus(net, name="HV Transformer Bus", vn_kv=110, type="n")
bus4 = pp.create_bus(net, name="MV Transformer Bus", vn_kv=20, type="n")
bus5 = pp.create_bus(net, name="MV Main Bus", vn_kv=20, type="b")
bus6 = pp.create_bus(net, name="HV bus1", vn_kv=20, type="b")
bus7 = pp.create_bus(net, name="HV bus2", vn_kv=20, type="b")

pp.create_ext_grid(net, bus1, vm_pu=1.02, va_degree=50)
trafo = pp.create_transformer(net, bus3, bus4, name="110/20 kV Transformer", std_type="25 MVA 110/20 kV")
