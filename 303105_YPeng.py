
def take_xas():
    yield from mv(extslt.vg,100, extslt.hg, 150)
    yield from xas([sclr],pgm.en,930,934,161)

def example_plan(detune, num_scans=8):
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
