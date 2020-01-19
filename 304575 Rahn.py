def firstevening():
    ext_vg = 10
    E_peak = [1521.25]
    split_times = [0.5,0.5]
    total_times = [6,6]
    num_cycles = 3
    
    yield from pol_V(0)
    yield from mv(epu1.gap,21.5)
    yield from sleep(3) 
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg, 'LV ' )

    yield from pol_H(0)
    yield from mv(epu1.gap,22.35)
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

