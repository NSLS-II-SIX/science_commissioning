def lots_of_same(repeat_block=30):
    ext_vg = 11
    en = 527.94

    split = 2
    total = 20*60 
    num_cycles = 12
    
    for i in range(0,repeat_block):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg, 'testing sclr fail without plot' )
        #yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg, 'testing sclr fail' , False)

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


def take_xas():
    yield from mv(extslt.vg,100, extslt.hg, 150)
    yield from xas([sclr],pgm.en,930,934,161)

def detuning(detune=0, num_scans=8):
    #detune=-0.1
    print("You are scanning at DETUNE (eV) = %f" % detune)
    # TO CHECK XAS
    yield from mv(extslt.vg,100, extslt.hg, 150)
    sclr_enable()
    target_Emax = yield from xas([sclr],pgm.en,931.5,933,150)
    sclr_disable()
    print('\n\n\tMoving pgm to {:.2f}eV for DETUNE {}\n\n'.format(target_Emax+detune, detune))
    yield from mv(pgm.en,target_Emax+detune)
	

    # TO MEASURE RIXS
    #yield from pol_H(-1.5) 
    yield from pol_V(4)
    yield from sleep(10)
    yield from rixs_one_energy(2.0,300,num_scans,target_Emax+detune,10)

    yield from mv(extslt.vg,100, extslt.hg, 150)
    sclr_enable()
    target_Emax = yield from xas([sclr],pgm.en,924,944,301)
    sclr_disable()
