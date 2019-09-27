
def ReN3_polH_300K_Tuesday_night(reps=9, cts=60):
    rixscam_exp = 5
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,70)
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    
    #energies = []
    for energy in range(444,454+1):
        yield from mv(pgm.en, energy)


        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'ReN3 300K th20 LH'})        
        yield from mv(gvbt1,'close')
    
    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)



def ReN3_polH_300K_Wed_night(reps=27, cts=120):
    rixscam_exp = 5

    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,200)
        
    #energies = []
    #for energy in range(444,454+1):

    energy=448.7
    #Spectrometer energy = 445 eV        
    m7p=5.768
    grp=6.3153
    yield from mv(pgm.en, energy)
    yield from mv(espgm.m7pit,m7p)
    yield from mv(espgm.grpit,grp)

    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})

    yield from mv(gvbt1,'open')     
    for i in range(reps):
        yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'ReN3 300K th20 tth 90 LH 448.7 eV'})        
    yield from mv(gvbt1,'close')
    
    energy=460.2
    #Spectrometer energy = 461 eV        
    m7p=5.723935
    grp=6.247742
    yield from mv(pgm.en, energy)
    yield from mv(espgm.m7pit,m7p)
    yield from mv(espgm.grpit,grp)

    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})

    yield from mv(gvbt1,'open')     
    for i in range(reps):
        yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'ReN3 300K th20 tth 90 LH 460.2 eV'})        
    yield from mv(gvbt1,'close')


    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)
    yield from mv(shutterb,'close')



def OK_polH_300K_Thu_morning(reps=10, cts=120):
    
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,40)
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    
    #energy = [529]
    for energy in range(530,536+1,6):
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)

RE.md['proposal'] =  '302976'
RE.md['sample'] = 'Cd2Re2O7'



def OK_polH_300K_Thu_evening(reps=1, cts=120):
    
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,40)
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    
    energy = [531]
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)


def OK_polH_300K_Thu_night(reps=40, cts=120):
    
    rixscam_exp = 2
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,20)
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    
    energy = [529]
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)


def OK_polH_300K_Fri_night():

    yield from mv(extslt.vg,40)
    
    #yield from pzshutter_disable()
    #yield from align.m1pit    #yield from m3_check()
    #yield from mv(m1_fbk_th,1600)
    #yield from sleep(5)
    #yield from mv(m1_fbk_sp,extslt_cam.stats1.centroid.x.value)
    #yield from sleep(2)
    #yield from mv(m1_fbk,1)
    #yield from pzshutter_enable()
 
          
    #energy = [530]
    #rixscam_exp = 1
    #yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    #reps=1
    #cts=120
    #yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    #yield from mv(sclr.preset_time, rixscam_exp)
    #for energy in energy:
    #    yield from mv(pgm.en, energy)

    #    yield from mv(gvbt1,'open')     
    #    for i in range(reps):
    #        yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
    #    yield from mv(gvbt1,'close')
   
    #energy = [529.5]
    #rixscam_exp = 2
    #reps=10
    #cts=120
    #yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    #yield from mv(sclr.preset_time, rixscam_exp)
    #for energy in energy:
    #    yield from mv(pgm.en, energy)

    #    yield from mv(gvbt1,'open')     
    #    for i in range(reps):
    #        yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
    #    yield from mv(gvbt1,'close')
 
    energy = [529.25]
    rixscam_exp = 2
    reps=10
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [529]
    rixscam_exp = 2
    reps=14
    #reps=20
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [528.75]
    rixscam_exp = 5
    reps=8
    #reps=12
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [531]
    rixscam_exp = 1
    reps=9
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [528.5]
    rixscam_exp = 5
    reps=13
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'O-K 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')


    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)

    yield from mv(stemp.ctrl2.setpoint,300)
    yield from temp_eq(0.5,10)
    yield from sleep(120)








