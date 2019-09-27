
def plan_one_energy(pts,cycles,energy): 
    dets = [rixscam]
    yield from mv(extslt.vg,10, extslt.hg, 150)
    #yield from pol_H(-2)
    rixscam_exp = 3.0
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
        yield from count(dets, num=pts, md = {'reason':'bsco op96'} )
        print('Ending cycle {}\n' .format(i+1))
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
    #yield from mv(shutterb,'close')
    

