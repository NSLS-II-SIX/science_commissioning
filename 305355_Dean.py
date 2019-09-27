def check_Q_cdw():
    
    ext_vg = 100
    total_time = 600
    cyc = 1
    en = 931.4318
    #pol is V
    sec_x_pt = 1

#    yield from mv(cryo.x, 24.36)
#    yield from mv(cryo.z, 15.64)
#    yield from mv(cryo.t, 41)
#    yield from sleep(30)
#    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th41_tth130')

    yield from mv(cryo.x, 24.37)
    yield from mv(cryo.z, 15.59)
    yield from mv(cryo.t, 40)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th40_tth130')

    yield from mv(cryo.x, 24.37)
    yield from mv(cryo.z, 15.59)
    yield from mv(cryo.t, 39)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th39_tth130')

    yield from mv(cryo.x, 24.38)
    yield from mv(cryo.z, 15.54)
    yield from mv(cryo.t, 38)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th38_tth130')

    yield from mv(cryo.x, 24.38)
    yield from mv(cryo.z, 15.54)
    yield from mv(cryo.t, 37)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th37_tth130')

    yield from mv(cryo.x, 24.39)
    yield from mv(cryo.z, 15.49)
    yield from mv(cryo.t, 36)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th36_tth130')

    yield from mv(cryo.x, 24.39)
    yield from mv(cryo.z, 15.49)
    yield from mv(cryo.t, 35)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LSCO_th35_tth130')


def HT_cdw():
    
    ext_vg = 20
    total_time = 600
    cyc = 1
    en = 931.4318
    #pol is V
    sec_x_pt = 5

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)

def LSNO_cdw():
    
    ext_vg = 11
    total_time = 600
    cyc = 9
    en = 853.565
    #pol is V
    sec_x_pt = 5

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)

def high_res_SCO_tth130_v3():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th48_tth130')

    yield from mv(cryo.x, 25.852)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.88)
    yield from mv(cryo.t, 53)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th53_tth130')

    yield from mv(cryo.x, 25.67)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.70)
    yield from mv(cryo.t, 58)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th58_tth130')

    yield from mv(cryo.x, 25.48)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.60)
    yield from mv(cryo.t, 63)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th63_tth130')

    yield from mv(cryo.x, 25.383)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.57)
    yield from mv(cryo.t, 68)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 9
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th68_tth130')


