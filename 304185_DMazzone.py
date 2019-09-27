def ErFeO3_map():

    #yield from mv(extslt.vg,100, extslt.hg, 150)
    #sclr_enable()
    #yield from xas([sclr],pgm.en,706,713,71)
    #sclr_disable()
    #yield from mv(extslt.vg,20, extslt.hg, 150)    

    yield from mv(gvbt1,'open')     
    rixscam_exp = 2
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)    
    reps=10
    cts=30
    #yield from pol_V(5.5)

    x_start=707
    x_stop=709
    num=9

    for i in range(num):
        x_val = x_start + i * (x_stop - x_start) / (num - 1)  
        yield from mv(pgm.en, x_val)

        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'ErFeO3 60K theta=10 deg pi pol'}) 
    yield from pzshutter_disable()       
    yield from mv(gvbt1,'close')
    yield from mv(extslt.vg,100, extslt.hg, 150)
    sclr_enable()
    yield from xas([sclr],pgm.en,706,713,71)
    sclr_disable()

    yield from mv(gvbt1,'open')
    yield from mv(extslt.vg,20, extslt.hg, 150) 

    x_start=709.25
    x_stop=711
    num=8
    yield from pzshutter_enable()
    for i in range(num):
        x_val = x_start + i * (x_stop - x_start) / (num - 1)  
        yield from mv(pgm.en, x_val)

        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'ErFeO3 60K theta=10 deg pi pol'})        
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
    yield from mv(extslt.vg,100, extslt.hg, 150)
    sclr_enable()
    yield from xas([sclr],pgm.en,706,713,71)
    sclr_disable()

    yield from mv(gvbt1,'open')
    yield from mv(extslt.vg,20, extslt.hg, 150) 

    x_start=711.25
    x_stop=712
    num=4
    yield from pzshutter_enable()
    for i in range(num):
        x_val = x_start + i * (x_stop - x_start) / (num - 1)  
        yield from mv(pgm.en, x_val)

        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'ErFeO3 60K theta=10 deg pi pol'})        
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
    yield from mv(extslt.vg,100, extslt.hg, 150)
    sclr_enable()
    yield from xas([sclr],pgm.en,706,713,71)
    sclr_disable()


    #yield from pol_H(3)

  
    yield from mv(gvbt1,'close')

def testslit():  
    reps=3
    cts=30
    
    yield from mv(gvbt1,'open')
    yield from mv(extslt.vg,150, extslt.hg, 150) 

    x_start=702.5
    x_stop=703.75
    num=2
    yield from pzshutter_enable()
    for i in range(num):
        x_val = x_start + i * (x_stop - x_start) / (num - 1)  
        yield from mv(pgm.en, x_val)

        for i in range(reps):
            yield from count([rixscam], num=cts, md = {'reason': 'ErFeO3 130K theta=10 deg sigma pol'})        
    yield from pzshutter_disable()


  
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

def ErFeO3_Mar30():
    #yield from mv(extslt.vg,100, extslt.hg, 150)
    #sclr_enable()
    #yield from xas([sclr],pgm.en,706,713,71)
    rixscam_exp = 2
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    sclr_disable()
    yield from mv(extslt.vg,20, extslt.hg, 150) 

    reps=40
    cts=30
    
   
    yield from mv(gvbt1,'open')
    yield from mv(extslt.vg,20, extslt.hg, 150) 

    x_val=710.5
   
    yield from pzshutter_enable()
    #for i in range(num):
    #    x_val = x_start + i * (x_stop - x_start) / (num - 1)  
    yield from mv(pgm.en, x_val)

    for i in range(reps):
        yield from count([rixscam], num=cts, md = {'reason': 'ErFeO3 115K theta=10 deg sigma pol'})        
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
    


    #yield from pol_H(3)

def carbon():
    #yield from mv(extslt.vg,100, extslt.hg, 150)
    #sclr_enable()
    #yield from xas([sclr],pgm.en,706,713,71)
    rixscam_exp = 2
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    sclr_disable()
    yield from mv(extslt.vg,20, extslt.hg, 150) 

    reps=2
    cts=30
    
   
    yield from mv(gvbt1,'open')
    yield from mv(extslt.vg,20, extslt.hg, 150) 

    x_val=710.5
   
    yield from pzshutter_enable()
    #for i in range(num):
    #    x_val = x_start + i * (x_stop - x_start) / (num - 1)  
    yield from mv(pgm.en, x_val)

    for i in range(reps):
        yield from count([rixscam], num=cts, md = {'reason': 'carbon 20 um'})        
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
      
    

