def almostDinner():
    
    ext_vg = 7
    total_time = 600
    cyc = 2
    en = 853.3
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test for 90deg')
    
    yield from pol_H(-3)
    yield from sleep(90)
    cyc = 2
    en = 853.3
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test for lunch')

def Feb25Dinner():
    
    yield from pol_V(-2)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 6
    en = 854.95
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test for 90deg')
    
    yield from pol_H(-3)
    yield from sleep(90)
    en = 854.95
    cyc = 6
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test for 90deg')

    yield from pol_H(-3)
    yield from sleep(90)
    en = 853.3
    cyc = 6
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test for 90deg')

    yield from pol_V(-2)
    yield from sleep(90)
    en = 853.3
    cyc = 6
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test for 90deg')

def Feb26LNO_70deg():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 1200
    cyc = 5
    en = 853.7
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LNO 70 deg')

def Feb26nightSNO():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 6
    en = 853.25
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SNO 90 deg')

def Feb27NNO_70deg():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 6
    en = 853.2
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 70 deg LH improve statistics')

def Feb26morningNNO():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 6
    en = 853.3
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 90 deg improve statistics')

def Feb26NNO_70deg():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 6
    en = 853.28
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 70 deg improve statistics')

def Feb27NNO_70deg_180K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 1200
    cyc = 6
    en = 853.38
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 70 deg LH 180 K PM metal')

def Feb27SNO_70deg_180K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 12
    en = 853.23
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SNO 70 deg LH 180 K AF insulator')

def Feb27SNO_70deg_225K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 900
    cyc = 2
    en = 853.2
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SNO 70 deg LH 225 K above Tn')

def Feb27SNO_70deg_300K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 900
    cyc = 9
    en = 853.29
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SNO 70 deg LH 300 K above Tn')


def Feb27NNO_70deg_225K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 900
    cyc = 12
    en = 853.39
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 70 deg LH 225 K above Tn')

def Feb28LNO_70deg_300K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 1200
    cyc = 9
    en = 853.75
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LNO 70 deg 300K')

def Feb28NNO_70deg_300K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 900
    cyc = 12
    en = 853.3
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 70 deg LH 300 K above Tn')

def Feb28NNO_70deg_150K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 12
    en = 853.2
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 70 deg LH 150K')

def Mar2NNO_150deg_35K():
    
    ext_vg = 11
    total_time = 900
    cyc = 8
    en = 528.3
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'NNO 150 deg LV 35K O K edge')

def Mar3LNO_150deg_35K():
    
    ext_vg = 11
    total_time = 1200
    cyc = 24
    en = 528.39
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'LNO 150 deg LV 35K O K edge')

def Mar3OPpi0_15deg_35K():
    
    ext_vg = 15
    total_time = 600
    cyc = 6
    en = 528.18
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 15deg LV 35K')

def Mar4UDpi0_15deg_35K():
    
    ext_vg = 15
    total_time = 600
    cyc =18
    en = 528.2
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 15deg LV 35K')

def Mar5UDpi0_94deg_35K():
    
    yield from pol_V(-4.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.58
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 94deg LV 35K')

def Mar4ODpi0_94deg_35K():
    
    yield from pol_V(-4.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.8
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 94deg LV 35K')

def Mar5OPpipi_95deg_35K():

    #yield from pol_V(-4.5)
    #yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.8
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pipi 95deg LV 35K')



def Mar5OPpi0_94deg_80K_LV():

    #yield from pol_V(-4.5)
    #yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 18
    en = 931.55
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 94deg LV 80K')

def Mar5ODpi0_94deg_35K_LV():

    yield from pol_V(-4.5)
    #yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.59
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 94deg LV 35K more statistics')

def Mar5OPpi0_94deg_35K_LH():

    #yield from pol_V(-4.5)
    yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.8
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 94deg LH 35K more statistics')

def Mar5ODpi0_94deg_35K_LH():

    #yield from pol_V(-4.5)
    #yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.69
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 94deg LH 35K')



def Mar6OPpi0_88deg_80K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.55
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 88deg LV 80K')

def Mar7OPpi0_88deg_100K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.62
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 88deg LV 100K')

def Mar7OPpi0_94deg_150K_LV():

    #yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.7
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 94deg LV 150K')

def Mar8OPpi0_88deg_250K_LV():

    #yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.79
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 88deg LV 250K')

def Mar7UDpi0_88deg_100K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.66
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 88deg LV 100K')

def Mar8UDpi0_88deg_250K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.56
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 88deg LV 250K')

def Mar8UDpi0_94deg_250K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.57
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 94deg LV 250K')

def Mar8UDpi0_88deg_35K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 9
    en = 931.75
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 88deg LV 35K')

def Mar8ODpi0_88deg_35K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.8
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 88deg LV 35K')

def Mar9OPpi0_112deg_35K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.8
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 112deg LV 35K')

def Mar8ODpi0_94deg_250K_LV():

    #yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.7
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 94deg LV 250K')

def Mar8ODpi0_88deg_250K_LV():

    #yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.79
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 88deg LV 250K')

def Mar7ODpi0_88deg_100K_LV():

    #yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.76
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 88deg LV 100K')

def Mar6OPpi0_94deg_100K_LV():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 18
    en = 931.6
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 88deg LV 100K')

def Mar6OPpi0_94deg_100K_LH():

    #yield from pol_V(-4.5)
    yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 12
    en = 931.67
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 94deg LH 100K')

def Mar6UDpi0_94deg_100K_LV():

    yield from pol_V(-4.5)
    #yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 7
    en = 931.64
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'UD pi0 94deg LV 100K')

def Mar6ODpi0_94deg_100K_LV():

    yield from pol_V(-4.5)
    #yield from pol_H(-5.5)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 7
    en = 931.64
    sec_x_pt = 2
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OD pi0 94deg LV 100K')

def Mar3OPpi0_40deg_35K():
    
    ext_vg = 15
    total_time = 600
    cyc = 18
    en = 528.18
    sec_x_pt = 6
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 40deg LV 35K')

def Mar3OPpi0_70deg_35K():
    
    ext_vg = 15
    total_time = 600
    cyc = 1
    en = 528.25
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'OP pi0 70deg LV 35K')

def Feb28SNO_70deg_150K():
    
    yield from pol_H(-3)
    yield from sleep(90)
    ext_vg = 7
    total_time = 600
    cyc = 3
    en = 853.3
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SNO 70 deg LH 150K')

def firstevening():
    ext_vg = 15
    E_peak = [528.4, 531]
    split_times = [6,6]
    total_times = [10, 15]
    num_cycles = 12
    
    yield from pol_V(0.75)
    yield from sleep(3) 
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg, 'LV ' )

    yield from pol_H(0.5)
    yield from sleep(3)
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg, 'LH ' )

def Nov3rd_night():
    peak_en = 528.5
    #yield from pol_V(1.9)
    #yield from sleep(30)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    
    #Move to SNO
    yield from mv(cryo.y,47.36180)
    yield from mv(cryo.z,20.50000)
    yield from mv(cryo.x,17.95300)

    peak_en = 528.6
    yield from sleep(30)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)

def Nov3rd_overnight():
    
    #Move to SNO for 3 hours
    #yield from mv(cryo.y,47.36180)
    #yield from mv(cryo.z,20.50000)
    #yield from mv(cryo.x,17.95300)

    peak_en = 528.6
    #yield from sleep(30)
    #yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)

    #Move back to NNO to complete 3 hours
    
    peak_en = 528.5

    yield from mv(cryo.x,18.32010)
    yield from mv(cryo.y,2.70000)
    yield from mv(cryo.z,20.58000)
    yield from sleep(30)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)

    #Move to LNO for 3 hours

    peak_en = 528.6
    
    yield from mv(cryo.x,18.01300)
    yield from mv(cryo.y,55.67150)
    yield from mv(cryo.z,20.96000)
    yield from sleep(30)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)
    yield from mvr(cryo.y,-0.020)
    yield from mvr(cryo.z,-0.026)
    yield from mvr(cryo.x,0.012)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)

def Nov4th_morning_repeatdata():
    
    peak_en = 528.5

    #Move to SNO (repeat)

    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)

    #Move to LNO (repeat)

    yield from mv(cryo.x,18.06610)
    yield from mv(cryo.y,55.60740)
    yield from mv(cryo.z,20.92000)

    yield from sleep(30)
    yield from rixs_one_energy_1(2,10*60,3,peak_en, 15)


def E_detuning():
    ext_vg = 15
    #yield from sleep(3) 
    yield from rixs_one_energy_1(6, 15*60, 12, 528.23, ext_vg, 'LV' )
    

    E_peak = [528.03, 527.83, 527.63, 527.43]
    split_times = [6,6,6,6]
    total_times = 15*60
    num_cycles = 12
    
    yield from pol_V(0.75)
    #yield from sleep(3) 
    for en, split in zip(E_peak, split_times):
        yield from rixs_one_energy_1(split, total_times, num_cycles, en, ext_vg, 'LV ' )


def E_detuning_June27():
    ext_vg = 11
    total_times = 15*60
    
    yield from pol_V(0.75)
    #yield from sleep(3)
    #yield from rixs_one_energy(6, total_times, 8, 528.2, ext_vg, 'E = 528.2 -- LV ' )
    #yield from rixs_one_energy(6, total_times, 4, 528.0, ext_vg, 'E = 528.0 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 527.72, ext_vg, 'E = 527.72 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 527.52, ext_vg, 'E = 527.52 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 12, 527.32, ext_vg, 'E = 527.32 -- LV ' )

