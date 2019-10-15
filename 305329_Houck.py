

def energy_Nb_HiPIMS_normal():
    ext_vg = 400
    total_time = 600
    cyc = 18
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    #yield from pol_V()
    E = list(np.arange(362.5,366.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'Nb_HiPIMS_normal')

def energy_NbO2():
    ext_vg = 400
    total_time = 600
    cyc = 12
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    #yield from pol_V()
    E = list(np.arange(363.5,366.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'NbO2')

def energy_Nbebeam():
    ext_vg = 50
    total_time = 600
    
    cyc = 6
    E = [530.7, 531.1, 531.6]
    for i in E:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'Nb HiPIMS normal')

    cyc = 18
    E = [531.1]
    for i in E:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'Nb HiPIMS normal')


