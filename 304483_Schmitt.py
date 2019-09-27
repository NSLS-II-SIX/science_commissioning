def firstevening():
    ext_vg = 11
    E_peak = [528.4, 531]
    split_times = [6,6]
    total_times = [10, 15]
    num_cycles = 12
    
    yield from pol_V(0.75)
    yield from sleep(3) 
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy(split, total, num_cycles, en, ext_vg, 'LV ' )

    yield from pol_H(0.5)
    yield from sleep(3) 
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy(split, total, num_cycles, en, ext_vg, 'LH ' )


def E_detuning():
    ext_vg = 11
    yield from sleep(3) 
    yield from rixs_one_energy_1(6, 15*60, 12, 528.23, ext_vg, 'LV' )
    

    E_peak = [528.03, 527.83, 527.63, 527.43]
    split_times = [6,6,6,6]
    total_times = 15*60
    num_cycles = 12
    
    yield from pol_V(0.75)
    yield from sleep(3) 
    for en, split in zip(E_peak, split_times):
        yield from rixs_one_energy_1(split, total_times, num_cycles, en, ext_vg, 'LV ' )


def E_detuning_June27():
    ext_vg = 11
    total_times = 15*60
    
    yield from pol_V(0.75)
    yield from sleep(3)
    #yield from rixs_one_energy(6, total_times, 8, 528.2, ext_vg, 'E = 528.2 -- LV ' )
    #yield from rixs_one_energy(6, total_times, 4, 528.0, ext_vg, 'E = 528.0 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 527.72, ext_vg, 'E = 527.72 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 527.52, ext_vg, 'E = 527.52 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 12, 527.32, ext_vg, 'E = 527.32 -- LV ' )

def E_detuning_June28():
    ext_vg = 11
    total_times = 15*60
    
    yield from pol_V(0.75)
    yield from sleep(3)
    #yield from rixs_one_energy(6, total_times, 8, 528.2, ext_vg, 'E = 528.2 -- LV ' )
    #yield from rixs_one_energy(6, total_times, 4, 528.0, ext_vg, 'E = 528.0 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 527.72, ext_vg, 'E = 527.72 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 527.52, ext_vg, 'E = 527.52 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 12, 527.32, ext_vg, 'E = 527.32 -- LV ' )

def E_detuning_June29():
    ext_vg = 11
    total_times = 15*60
    
    yield from pol_V(0.75)
    yield from sleep(3)
    #yield from rixs_one_energy_1(6, total_times, 12, 528.23, ext_vg, 'E = 528.23 -- LV ' )
    #yield from rixs_one_energy_1(6, total_times, 12, 528.03, ext_vg, 'E = 528.03 -- LV ' )
    #yield from rixs_one_energy_1(6, total_times, 12, 527.83, ext_vg, 'E = 527.83 -- LV ' )
    #yield from rixs_one_energy_1(6, total_times, 12, 527.6, ext_vg, 'E = 527.6 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 12, 527.33, ext_vg, 'E = 527.33 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 4, 528.13, ext_vg, 'E = 528.13 -- LV ' )

def E_detuning_June30():
    ext_vg = 11
    total_times = 15*60
    
    yield from pol_V(0.75)
    yield from sleep(3)
    #yield from rixs_one_energy_1(6, total_times, 12, 528.2, ext_vg, 'E = 528.2 -- LV ' )
    #yield from rixs_one_energy_1(6, total_times, 12, 528.0, ext_vg, 'E = 528.0 -- LV ' )
    #yield from rixs_one_energy_1(6, total_times, 12, 527.8, ext_vg, 'E = 527.8 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 3, 527.56, ext_vg, 'E = 527.56 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 12, 527.36, ext_vg, 'E = 527.36 -- LV ' )
    #yield from rixs_one_energy_1(6, total_times, 4, 528.13, ext_vg, 'E = 528.13 -- LV ' )

def E_detuning_July1():
    ext_vg = 11
    total_times = 15*60
    
    yield from pol_V(0.75)
    yield from sleep(3)
    yield from rixs_one_energy_1(6, total_times, 12, 528.14, ext_vg, 'E = 528.14 -- LV ' )
    yield from rixs_one_energy_1(6, total_times, 12, 527.94, ext_vg, 'E = 527.94 -- LV ' )

def secondafternoon():
    ext_vg = 11
    E_peak = [528.4, 531]
    split_times = [5,5]
    total_times = [10*60, 10*60]
    num_cycles = 9
    
    yield from pol_V(0.75)
    yield from sleep(3) 
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy(split, total, num_cycles, en, ext_vg, 'LV ' )
