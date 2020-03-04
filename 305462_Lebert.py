def longscan():
    ext_vg = 20
    en = 461.1

    total_time = 600
    cyc = 1
    sec_x_pt = 1
    #yield from pol_V(-2)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)

    total_time = 600
    cyc = 500
    sec_x_pt = 5

    yield from pol_H(-3)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)


def RuCl3_overnight():
    ext_vg = 20
    total_time = 600
    cyc = 1000
    en = 461.1
    sec_x_pt = 5

#    yield from pol_H(-3)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)

def RuCl3_testLV():
    ext_vg = 20
    total_time = 600
    cyc = 2
    en = 461.1
    sec_x_pt = 1

#    yield from pol_V(-2)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'RuCl_top_150K_LH')


def RuCl3_Edep():
    ext_vg = 100
    total_time = 600
    cyc = 2
    en = 461.1
    sec_x_pt = 5

    yield from pol_H(-3)
    
    E2 = list(np.arange(461.1 - 1.5, 461.1 + 3.0, 0.75))
    for i in E2:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
