def NiRhO_E_map():
  
    ext_vg = 20
    total_time = 480
    cyc=3

    #E = np.arange(852.1,857.7,0.25)
    E = np.arange(852.1,853.11,0.25)
    sec_x_pt = 5
    for i in E:
        yield from sleep(10)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)
    
    E = np.arange(853.225,854.11,0.125)
    sec_x_pt = 5
    for i in E:
        yield from sleep(10)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)

    
    E = np.arange(854.35,857.7,0.25)
    sec_x_pt = 5
    for i in E:
        yield from sleep(10)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)

def NiRhO_20210314_plan():
    ext_vg = 12
    total_time = 600
    sec_x_pt = 5

    #########################################
    E = 853.8
    cyc=3


    yield from pol_H(-5.3)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    yield from pol_V(-5.5)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)


    #########################################
    # E = 856.3
    # cyc=5

    # yield from pol_H(-5.3)
    # yield from sleep(10)
    # yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    # yield from pol_V(-5.5)
    # yield from sleep(10)
    # yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    # #########################################
    # E = 853.8
    # cyc=6

    # yield from pol_H(-5.3)
    # yield from sleep(10)
    # yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    # yield from pol_V(-5.5)
    # yield from sleep(10)
    # yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)



def NiRhO_20210315_plan():
    ext_vg = 12
    total_time = 600
    sec_x_pt = 5

    #########################################
    E = 853.8
    cyc=3


    yield from pol_H(-5.3)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    yield from pol_V(-5.5)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)


    #########################################
    E = 853.4
    cyc=3


    yield from pol_H(-5.3)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    yield from pol_V(-5.5)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)


    #########################################
    E = 856.3
    cyc=18

    yield from pol_H(-5.3)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)

    yield from pol_V(-5.5)
    yield from sleep(10)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg)
