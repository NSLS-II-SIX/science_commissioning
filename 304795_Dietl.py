def energy_462_thin_CRO_90K_v7():
    ext_vg = 30
    total_time = 600
    cyc = 24
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,462.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_thin_film')


def energy_462_thin_CRO_v5():
    ext_vg = 30
    total_time = 600
    cyc = 24
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,462.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_thin_film')

def energy_map_thin_CRO_v2():
    ext_vg = 30
    total_time = 600
    cyc = 7
    yield from pol_H()
    E = list(np.arange(461,461.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_thin_film')

    ext_vg = 30
    total_time = 600
    cyc = 18
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,464.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_thin_film')




def energy_462_CRO():
    ext_vg = 30
    total_time = 600
    cyc = 12
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,463,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'cleaved_crystal')


def energy_map_bulk_CRO():
    ext_vg = 30
    total_time = 600
    cyc = 12
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(461,464.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    E = list(np.arange(461,464.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    

def energy_462_CRO():
    ext_vg = 30
    total_time = 600
    cyc = 12
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,463,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'extra_stats')
    
    
