def example_night_one_energy():
    ext_vg = 11
    E_peak = 708
    num_cycles = 13
    yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))

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



def example_night_one_energy():
    ext_vg = 11
    E_peak = 708
    num_cycles = 13
    yield from sleep(3)
    #theta = [10]
    #samx = [22.88]
    #samy = [14.4]
    #samz = [16.35]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        #yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)
