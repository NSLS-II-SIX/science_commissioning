#TAKE OUT SCALER!!!!!!!!!

def SrRuO3_Dec2018():
 
    energy = [461]
    rixscam_exp = 5
    #real counting time is rixscam_exp + 2 sec
    reps=8
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'SrRuO3 Ru M3 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [461.5]
    rixscam_exp = 5
    reps=8
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'SrRuO3 Ru M3 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [462]
    rixscam_exp = 5
    reps=8
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'SrRuO3 Ru M3 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [462.5]
    rixscam_exp = 5
    reps=8
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'SrRuO3 Ru M3 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')

    energy = [461]
    rixscam_exp = 5
    #real counting time is rixscam_exp + 2 sec
    reps=8
    cts=120
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    yield from mv(sclr.preset_time, rixscam_exp)
    for energy in energy:
        yield from mv(pgm.en, energy)

        yield from mv(gvbt1,'open')     
        for i in range(reps):
            yield from count([rixscam, sclr, ring_curr], num=cts, md = {'reason': 'SrRuO3 Ru M3 300K th20 tth90 LH'})        
        yield from mv(gvbt1,'close')


#TAKE OUT SCALER!!!!!!!!!
#real counting time is rixscam_exp + 2 sec
 

def SmS_Dec2018_Frinight():

    yield from mv(gvbt1,'open')     
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1074,1074.5,1075,1075.5,1076,1076.5]
    #6 energies, 6 reps each, 36 scans
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        


    energies=[1077,1077.5,1078,1078.5,1079,1079.5,1080,1080.5,1081,1081.5,1082]
    #11 energies, 4 reps each, 44 scans
    reps=4
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        

    energies=[1082.5,1083,1083.5,1084]
    #4 energies, 6 reps each, 24 scans
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        
  
    yield from mv(gvbt1,'close')




def SmS_Dec2018_SatPM():

    yield from mv(gvbt1,'open')     
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1076.5,1080]
    reps=5
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        
    
    rixscam_exp = 5
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1060]
    reps=2
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LV'})  


    yield from mv(gvbt1,'close')




def SmS_Dec2018_SatPM2():

    yield from mv(gvbt1,'open')     
    
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1075]
    reps=6
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LV'})        
 
    yield from mv(gvbt1,'close')




def SmS_Dec2018_Satnight():

    yield from mv(gvbt1,'open')     
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1074,1074.5,1075,1075.5,1076,1076.5]
    #6 energies, 5 reps each, 36 scans
    reps=5
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        


    energies=[1077,1077.5,1078,1078.5,1079,1079.5,1080,1080.5,1081,1081.5,1082]
    #11 energies, 4 reps each, 44 scans
    reps=4
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        

    energies=[1082.5,1083,1083.5,1084]
    #4 energies, 5 reps each, 24 scans
    reps=5
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        
  
    yield from mv(gvbt1,'close')



def SmS_Dec2018_Sunnight():

    yield from mv(gvbt1,'open')     
    rixscam_exp = 1
    yield from mv(rixscam.cam.acquire_time, rixscam_exp)
    
    energies=[1075,1076]
    #6 energies, 5 reps each, 36 scans
    reps=2
    cts=120
    for energy in energies:
        yield from mv(pgm.en, energy)
        for i in range(reps):
            yield from count([rixscam, ring_curr], num=cts, md = {'reason': 'SmS Sm M5 300K th20 tth90 LH'})        
       

    yield from mv(gvbt1,'close')


