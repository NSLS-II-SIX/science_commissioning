def S03_first_night():
    rixscam_exp = 30
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)

    E = [462.5,461]
    yield from pol_H(1.6)
    m7_pit_vals = None
    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, 400, 'S03 300K GI' )

    yield from mv(rixscam.cam.acquire_time, 15)
    yield from mv(sclr.preset_time, 1)

def S04_polV_300K(N_scans=1):
    rixscam_exp = 3
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)

    E = [455]
    #yield from pol_V(-1.8)
    m7_pit_vals = None
    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, N_scans, 'S04 300K Spec' )

    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)

def S04_polH_300K(N_scans=1):
    rixscam_exp = 5
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)

    E = [463.2]

    m7_pit_vals = None

    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, N_scans, 'S04 300K GI' )

    yield from mv(rixscam.cam.acquire_time, 15)
    yield from mv(sclr.preset_time, 1)



def S04_polHV_300K_NI(N_scans=1):
    rixscam_exp = 8
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)
    
    E = [462.4]
    
    m7_pit_vals = None
    #yield from pol_H(1.6)
    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, N_scans, 'S04 300K NI' )

    yield from mv(m1_fbk,0) 
    yield from pol_V(-1.8)
    yield from sleep(10)
    yield from mv(m1_fbk_cam_time,0.03)
    yield from mv(m1_fbk,1)

    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, N_scans, 'S04 300K NI' )


    yield from mv(shutterb,'Close')
    yield from mv(rixscam.cam.acquire_time, 15)
    yield from mv(sclr.preset_time, 1)


def S04_polV_100K_NI(N_scans=1):
    rixscam_exp = 2
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)

    E = [462.5]
    #yield from pol_V(-1.8)
    m7_pit_vals = None
    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, N_scans, 'S04 100K Spec' )

    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)

def S04_polH_300K_Monday2(N_scans=1):
    rixscam_exp = 5
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)

    E = [460.7]
    # Using horizontal pol
    m7_pit_vals = None
    yield from rixscam_acquire_w_shutter(E,m7_pit_vals, N_scans, 'S04 300K th20 LH' )

    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)

def S04_polH_300K_Tuesday_count(reps=1, cts=60):
    rixscam_exp = 5
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)

    E = 460.7
    yield from mv(pgm.en, E)
    # Using horizontal pol
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    yield from mv(gvbt1,'open')     
    for i in range(reps):
        yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'S04 300K th20 LH'})        
    yield from mv(gvbt1,'close')
    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)

def S04_polV_300K_Monday_night(reps=1, cts=60):
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,50)
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    
    energies = [461.2, 462.2, 463.2]
    for energy in energies:
        yield from mv(pgm.en, energy)


        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'S04 300K th20 LV'})        
        yield from mv(gvbt1,'close')
    
    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)


def S04_polH_300K_Tuesday_night(reps=1, cts=60):
    rixscam_exp = 5
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)

    yield from mv(extslt.vg,20)
    yield from count([rixscam, sclr, ring_curr], num=1, md = {'reason': 'dummy'})
    
    energies = [461.0]
    for energy in energies:
        yield from mv(pgm.en, energy)


        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'S04 300K th20 LH'})        
        yield from mv(gvbt1,'close')
    
    yield from mv(rixscam.cam.acquire_time, 5)
    yield from mv(sclr.preset_time, 1)



