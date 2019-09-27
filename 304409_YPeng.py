
def take_xas():
    yield from mv(extslt.vg,50, extslt.hg, 150, pgm.en, 527.75)
    #yield from xas([sclr],pgm.en,520,539,161,.1)
    E_com, E_max = yield from xas([sclr],pgm.en,527.75,528.5,76,1)
    print(E_com - 0.0133, '  ', E_max)

def xas_rixscam(exp_time=2, repeats=2):
    Emaxs = []
    rixscam.xip.count_event_3x3.kind = Kind.hinted  # plot the rixscam live
    yield from pzshutter_enable()

    yield from mv(rixscam.cam.acquire_time, exp_time)  
    yield from mv(sclr.preset_time, exp_time)
    yield from mv(extslt.vg,100, extslt.hg, 150)
    for i in range(0,repeats):
        yield from mv(pgm.en, 527.15)
        yield from mv(gvbt1,'open')
        yield from sleep(2)
        #yield from scan([rixscam,sclr,ring_curr], pgm.en,525,535,200)  # for long XAS
        yield from scan([rixscam,sclr,ring_curr], pgm.en,527.15,529,38) # for detuning
        Emaxs.append(peaks['max']['rixscam_xip_count_event_3x3'][0])     # comment out for print_summary

    yield from mv(rixscam.cam.acquire_time, 1)  
    yield from mv(sclr.preset_time, 1)
    rixscam.xip.count_event_3x3.kind = Kind.normal  # plot the rixscam live
    yield from mv(extslt.vg,15)
    print('Emaxs:\t',Emaxs,'\t----> avg:\t',np.mean(Emaxs))
    return np.mean(Emaxs)
    
    



def detuning(target_E=528.02, detune=0, split_time=4, total_exp=300, num_scans=10, doXAS=True):
    print("You are scanning at DETUNE (eV) = %f" % detune)
    # TO CHECK XAS and get new target_E
    
    if doXAS is True:
        yield from sleep(2)
        sclr_enable()
        target_E = yield from xas_rixscam(exp_time=2)
        sclr_disable()
    else:
        pass
    
    target_E = target_E + detune
    print('\n\n\tMoving pgm to {:.2f}eV for DETUNE {}\n\n'.format(target_E, detune))
    yield from mv(pgm.en,target_E)
	

    # TO MEASURE RIXS
    yield from sleep(10)
    yield from rixs_one_energy_1(split_time,total_exp,num_scans,target_E,15)



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
