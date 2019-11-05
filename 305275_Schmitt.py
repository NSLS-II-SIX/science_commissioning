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

