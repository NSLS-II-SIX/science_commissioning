def LiCuV_overnight():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 930.2
    #en = 929.3
    sec_x_pt = 2

    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LCV-LV')

def hbs_tth150():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 930.3
    #en = 929.3
    sec_x_pt = 4

    yield from pol_V()

    #yield from pol_H(-6.5)
    #yield from sleep(15)
    #yield from beamline_align_v2()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LV')

    #yield from pol_V()
    #yield from sleep(15)
    #yield from beamline_align_v2()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LV')

def barlowite_tth150():
    ext_vg = 11
    total_time = 600
    #cyc = 6
    cyc = 4
    en = 930.35
    sec_x_pt = 4
    
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LV')

    #yield from pol_H(-6.5)
    #yield from sleep(15)
    #yield from beamline_align_v2()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')

def Zn_barlowite_tth150():
    ext_vg = 11
    total_time = 900
    #cyc = 6
    cyc = 2
    en = 930.35
    sec_x_pt = 5
    
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')

    #yield from pol_V()
    #yield from sleep(15)
    #yield from beamline_align_v2()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')

    #yield from pol_H(-6.5)
    #yield from sleep(15)
    #yield from beamline_align_v2()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LV')
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')



def test_macro():
    ext_vg = 11
    total_time = 600
    #cyc = 6
    cyc = 6
    en = 930.3
    sec_x_pt = 4

    yield from pol_V()
    yield from sleep(15)
    yield from beamline_align_v2()


def barlowite_dinner():
    ext_vg = 11
    total_time = 600
    #cyc = 6
    cyc = 6
    en = 930.3
    sec_x_pt = 4

    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LV')

    yield from pol_H(-6.5)
    yield from sleep(15)
    yield from beamline_align_v2()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')


def barlowite_night():
    ext_vg = 11
    total_time = 600
    #cyc = 6
    cyc = 6
    en = 930.3
    sec_x_pt = 4

    #yield from pol_V()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LV')

    #yield from pol_H(-6.5)
    #yield from sleep(15)
    #yield from beamline_align_v2()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'ZnBarl - LH')


def hbs_hhl_overnight():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 930.2
    sec_x_pt = 4

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS hhl - LV')
    #yield from pol_V()
    #yield from beamline_align_v2()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS hhl - LV')
    #yield from pol_H(-6.5)


def hbs_h0l_overnight_1():
    ext_vg = 11
    total_time = 600
    cyc = 8
    en = 930.3
    sec_x_pt = 4

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LH')
    #yield from pol_V()
    #yield from beamline_align_v2()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LV')
    #yield from pol_H(-6.5)

def hbs_h0l_overnight_2():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 930.3
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LV')
    yield from pol_H(-6.5)
    #yield from beamline_align_v2()
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LH')

def hbs_h0l():
    ext_vg = 11
    total_time = 600
    cyc = 5
    en = 930.6
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LH')
    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'HBS h0l - LV')


def barlowite():
    ext_vg = 11
    total_time = 300
    cyc = 9
    en = 931.4
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')

