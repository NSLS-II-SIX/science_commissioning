def Fe3Sn2_th0_highStats():
    ext_vg = 15
    total_time = 600
    cyc = 18
    sec_x_pt = 5
    E = [706.5] # film
    # E = [707.35,709] #crystal
    
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'Fe3Sn2')


def Fe3Sn2_th0():
    ext_vg = 11
    total_time = 600
    cyc = 6 
    sec_x_pt = 5
    E = [706.5] # film
    # E = [707.35,709] #crystal
    
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'Fe3Sn2')

    yield from pol_H(0)
    yield from sleep(30)
    yield from beamline_align_v2()
    yield from sleep(30)
    cyc = 9
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'Fe3Sn2')


voltage_dc = EpicsSignal('XF:02IDD{K2611:1}SP-VLvl', name = 'voltage_dc')
keithley_output = EpicsSignal('XF:02IDD{K2611:1}Cmd:Out-Ena', name = 'keithley_output')
current_rbk = EpicsSignal('XF:02IDD{K2611:1}RB-MeasI', name = 'current_rbk')
#yield from mv(keithley_output,'OFF')
#yield from mv(keithley_output,'ON')
#yield from mv(voltage_dc,0.5)

def Fe_film_tth150_without_field():
    ext_vg = 15
    total_time = 900
    cyc = 6
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    # yield from mv(keithley_output,'OFF')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,706.6,ext_vg, 'Fe film')

    yield from mv(voltage_dc,0.0)
    yield from mv(keithley_output,'OFF')

def Fe_film_tth150_with_E_field_4():
    ext_vg = 15
    total_time = 900
    cyc = 12
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    yield from mv(keithley_output,'ON')
    yield from mv(voltage_dc,-10.0)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,706.6,ext_vg, 'Fe film')

    yield from mv(voltage_dc,0.0)
    yield from mv(keithley_output,'OFF')

def Fe_film_tth150_with_E_field():
    ext_vg = 15
    total_time = 900
    cyc = 12
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    yield from mv(keithley_output,'ON')
    yield from mv(voltage_dc,0.5)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,706.6,ext_vg, 'Fe film')

    yield from mv(voltage_dc,1.0)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,706.6,ext_vg, 'Fe film')
    yield from mv(voltage_dc,0.0)
    yield from mv(keithley_output,'OFF')


def Fe_film_tth150_with_E_field_2():
    ext_vg = 15
    total_time = 900
    cyc = 12
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    yield from mv(keithley_output,'ON')
    yield from mv(voltage_dc,-9.0)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,706.6,ext_vg, 'Fe film')

    yield from mv(voltage_dc,0.0)
    yield from mv(keithley_output,'OFF')


def Fe_film_tth150_with_E_field_3():
    ext_vg = 15
    total_time = 900
    cyc = 12
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    yield from mv(keithley_output,'ON')
    yield from mv(voltage_dc,-17.5)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,706.5,ext_vg, 'Fe film')

    yield from mv(voltage_dc,0.0)
    yield from mv(keithley_output,'OFF')


def YIG_film_energy_map_tth110():
    ext_vg = 11
    total_time = 600
    cyc = 12
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,9,708.85,ext_vg, 'YIG')
    yield from rixs_one_energy_1(sec_x_pt,total_time,12,707.65,ext_vg, 'YIG')
    #E = [707.65]
    #for i in E:
        #sec_x_pt = 5
        #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'YIG')



def YIG_film_specular_search():
    ext_vg = 100
    total_time = 30
    cyc = 1
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 1
    E = [708.85] 
    th = [45.6,45.8,46,46.2,46.8,47.0,47.2,47.4,47.6,47.8,48,48.2,48.4,48.6,48.8,49.,49.2,49.4,49.6,49.8,50.0,50.2,50.4,50.6,50.8,51,51.2,51.4,51.6,51.8,52.0]
    for i in th:
        yield from mv(cryo.t,i)
        yield from mvr(cryo.z,0.035)
        yield from mvr(cryo.x,-0.0035)
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,708.85,ext_vg, 'YIG')

def YIG_film_energy_map():
    ext_vg = 11
    total_time = 600
    cyc = [6,9] 
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    E = [707.35,708.55] # film
    # E = [707.35,709] #crystal
    
    for c, i in zip(cyc, E):
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,c,i,ext_vg, 'YIG')

    # Moving to sample transfer position
    # yield from mv(cryo.t,257)
    # yield from mv(cryo.y,44)
    # yield from mv(cryo.x,14)
    # yield from mv(ow,-69.75)

def YIG_energy_map():
    ext_vg = 11
    total_time = 600
    cyc = 9
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 5
    E = [710.6,709.4,707.65,707.1]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'high Res_th_62')


pulse_time = EpicsSignal('XF:02IDD{K2611:1}Cmd-Pulse.SCAN', name = 'pulse_time')
#yield from mv(pulse_time,'300 second')
#yield from mv(pulse_time,'Passive')

def Hematite_device_th20_20191115():
    ext_vg = 11
    total_time = 600
    cyc = 9
    # Pol  Vertical
    #yield from pol_V(-2)
    yield from sleep(10)
    # E = 708.5
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,708.5,ext_vg, 'high Res_th_0')

    # Pol  Horizontal
    yield from pol_H(0)
    yield from sleep(10)
    yield from beamline_align_v2()
    yield from sleep(30)
    # E = 708.5
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,708.5,ext_vg, 'high Res_th_0')

def Hematite_middle_th40_highres_20191113():
    ext_vg = 11
    total_time = 600
    cyc = 9
    # Pol  Horizontal
    #yield from pol_H(0)
    yield from sleep(10)
    # E = 708.5
    sec_x_pt = 5
    E = [707.5,709.1]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'high Res_th_40')



def Hematite_device_th20_E_map_20191113():
    ext_vg = 11
    total_time = 600
    cyc = 12
    # Pol  Horizontal
    #yield from pol_H(0)
    yield from sleep(10)
    # E = 708.5
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,3,708.5,ext_vg, 'high Res_th_20')
    # E = 707.5 and 709.1
    E = [707.5,709.1]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'high Res_th_20')

	# Check XAS LH
    yield from mv(rixscam.cam.acquire_time, 1) 
    yield from mv(extslt.vg,200)
    yield from xas([sclr,ring_curr,rixscam],pgm.en,705,713,81,1)
    yield from mv(rixscam.cam.acquire_time, 5) 

def Hematite_device_middle_specular():
    ext_vg = 11
    total_time = 600
    cyc = 9
    yield from pol_H(0)
    yield from sleep(10)
    E = [708.5]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'high Res_th_59')


def Hematite_film_specular():
    ext_vg = 11
    total_time = 600
    cyc = 9
    yield from pol_H(0)
    yield from sleep(10)
    E = [708.5]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'high Res_th_59')

def Hematite_film_lunch():
    ext_vg = 11
    total_time = 600
    cyc = 12
    yield from pol_H(0)
    yield from sleep(10)
    E = [708.5]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'high Res_th_20')

def Hematite_film_dinner():
    ext_vg = 15
    total_time = 600
    cyc = 6
    yield from pol_H(0)
    yield from sleep(10)
    E = list(np.arange(707.5,707.6,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th43')


def Hematite_film_E_map_20191111():
    ext_vg = 15
    total_time = 600
    cyc = 6
    # Pol  Vertical
    yield from pol_V(-2)
    yield from sleep(10)
    # E = 706.7
    yield from rixs_one_energy_1(5,900,4,706.7,ext_vg, 'th20')
    # E = 707,708.5 and 709.1
    E = [707,708.5,709.1]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th20')

    # Pol  Horizontal
    yield from pol_H(0)
    yield from sleep(10)
    yield from beamline_align_v2()
    yield from sleep(30)
    # E = 706.7
    yield from rixs_one_energy_1(5,900,4,706.7,ext_vg, 'th20')
    # E = 707,708.5 and 709.1
    E = [707,708.5,709.1]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th20')
    
	# Check XAS LH
    yield from mv(rixscam.cam.acquire_time, 1) 
    yield from mv(extslt.vg,200)
    yield from xas([sclr,ring_curr,rixscam],pgm.en,705,713,81,1)

	# Check XAS LV
    yield from pol_V(-2)
    yield from sleep(10)
    yield from beamline_align_v2()
    yield from xas([sclr,ring_curr,rixscam],pgm.en,705,713,81,1)


def Hematite_film_E_map_20191112():
    ext_vg = 15
    total_time = 600
    cyc = 6
    # Pol  Horizontal
    yield from pol_H(0)
    yield from sleep(10)
    yield from beamline_align_v2()
    yield from sleep(30)

    E = [707,708.5,709.1]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th20')


def Hematite_device_th20_E_map_20191113_02():
    ext_vg = 11
    total_time = 600
    cyc = 9
    # Pol  Horizontal
    #yield from pol_H(0)
    yield from sleep(10)
    # E = 708.5
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,707.5,ext_vg, 'high Res_th_40')
















