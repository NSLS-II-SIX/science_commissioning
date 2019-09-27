def LCO_night():
    ext_vg = 10
    total_time = 600
    split_time = 5

    E_peak = 931

    # Detune -0.75 eV 
    detune=-0.75
    num_cycles = 12
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    yield from sleep(1)

    # Detune -0.5 eV 
    detune=-0.5
    num_cycles = 12
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    yield from sleep(1)

    # Detune -0.25 eV 
    detune=-0.25
    num_cycles = 12
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    yield from sleep(1)

    # Detune 0 eV 
    detune=0
    num_cycles = 12
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    yield from sleep(1)

    # Detune 0.25 eV 
    detune=0.25
    num_cycles = 12
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    yield from sleep(1)




def One_High_Stats():
    ext_vg = 7
    total_time = 600
    split_time = 5
    num_cycles=12
    target_Emax = 931.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,target_Emax,ext_vg, 'q = -0.3')


