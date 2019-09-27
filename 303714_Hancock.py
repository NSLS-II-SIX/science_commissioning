#TAKE OUT SCALER!!!!!!!!!
 

def YbInCu4_Feb26():

    yield from mv(gvbt1,'open')     
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1518.5, 1519, 1519.5, 1520, 1520.5, 1521, 1521.5, 1522, 1522.5, 1523, 1523.5]
    #11 energies, 6 reps each, 66 scans
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'YbInCu4 100K theta=10 deg sigma pol'})        

    energies=[1518.5, 1519, 1519.5, 1520, 1520.5, 1521, 1521.5, 1522, 1522.5, 1523, 1523.5]
    #11 energies, 6 reps each, 66 scans
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'YbInCu4 100K theta=10 deg sigma pol'}) 

    energies=[1518.5, 1519, 1519.5, 1520, 1520.5, 1521, 1521.5, 1522, 1522.5, 1523, 1523.5]
    #11 energies, 6 reps each, 66 scans
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'YbInCu4 100K theta=10 deg sigma pol'})

    yield from mv(gvbt1,'close')


def plan_one_energy1(pts,cycles,energy): 
    sclr_disable()
    dets = [rixscam]
    yield from mv(extslt.vg,10, extslt.hg, 150)
    #yield from pol_H(-2)
    rixscam_exp = 1.0
    #yield from mv(cryo.y,28.65)
    #yield from mv(cryo.x,26.31)
    #yield from mv(cryo.z,15.835)
    yield from pzshutter_enable()
    yield from mv(gvbt1,'open')
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(pgm.en,energy)
    yield from sleep(5)
    for i in range(0,cycles):
        print('Starting cycle {}' .format(i+1))
        yield from count(dets, num=pts, md = {'reason':'90K th=67.5deg V pol'} )
        print('Ending cycle {}\n' .format(i+1))
    yield from pzshutter_disable()
    sclr_enable()
    yield from mv(gvbt1,'close')
    #yield from mv(shutterb,'close')







def YbInCu4_Feb26PM():

    yield from mv(gvbt1,'open')     
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1520.3]
    #1 energy, 6 reps
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'YbInCu4 100K theta=67.5 deg H pol'})  

