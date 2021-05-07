def Bi2212_test():

    total_time = 600
    cyc = 2 
    energy = 932.59

    ext_vg = 12
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)
    
    yield from sleep(10)
    ext_vg = 15
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)
    
    yield from sleep(10)
    ext_vg = 20
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)
    
