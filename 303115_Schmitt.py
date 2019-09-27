


def plan_one_energy1(split_time, total_exp,cycles,energy, ext_vg,reason=''): 
    sclr_disable()
    dets = [rixscam]
    yield from mv(extslt.vg,ext_vg, extslt.hg, 150)
    #yield from pol_H(2.8)
    #yield from pol_V(1.9)
    #yield from mv(cryo.y,28.65)
    #yield from mv(cryo.x,26.31)
    #yield from mv(cryo.z,15.835)
    yield from pzshutter_enable()
    yield from mv(gvbt1,'open') # open GV before CCD
    yield from mv(rixscam.cam.acquire_time, split_time)
    yield from mv(pgm.en,energy)
    yield from sleep(5)
    pts = int(total_exp/split_time)
    for i in range(0,cycles):
        print('Starting cycle {} of {}' .format((i+1),cycles))
        yield from count(dets, num=pts, md = {'reason':'Length = '+str(total_exp*cycles)+' s -'+reason} )
        print('Ending cycle {} of {}\n' .format((i+1),cycles))
        yield from mvr(cryo.y,0.007)
        #yield from mvr(cryo.z,0.0017) #in case of sample on wedge
        #yield from mvr(cryo.x,-0.0017)
    yield from pzshutter_disable()

    sclr_enable()
    yield from mv(gvbt1,'close') # close GV before CCD
    #yield from mv(shutterb,'close') # close ShutterB before CCD


def first_night():
    yield from mv(extslt.vg,10, extslt.hg, 150)
    yield from pol_H(2.8)
    yield from plan_one_energy1(4.0,600,18,528.38)
    yield from pol_V(1.9)
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,18,528.38)
    
    yield from pol_H(2.8)
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,528.38)
    yield from pol_V(1.9)
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,528.38)

def second_dinner():
    #yield from pol_V(1.9)
    #yield from sleep(10)
    #yield from plan_one_energy1(4.0,600,11,528.4, 10)
    
    #yield from sleep(10)
    yield from plan_one_energy1(3.0,600,2,528.38, 20)


def second_night():
    #yield from pol_V(1.9)
    #yield from sleep(30)
    peak_en = 528.3
    yield from plan_one_energy1(2.0,600,12,peak_en, 20)
    
    yield from pol_H(2.8)
    yield from sleep(30)
    yield from plan_one_energy1(2.0,600,12,peak_en, 20)

    #yield from pol_H(2.8)
    yield from sleep(30)
    yield from plan_one_energy1(2.0,600,6,peak_en, 20)

    yield from pol_V(1.9)
    yield from sleep(30)
    peak_en = 528.3
    yield from plan_one_energy1(2.0,600,6,peak_en, 20)

def aftermacrocrash():
    peak_en = 528.3
    yield from plan_one_energy1(2.0,600,8,peak_en, 20)

def test_38deg():
    peak_en = 528.3
    yield from plan_one_energy1(2.0,600,2,peak_en, 20)

def test_90deg_LH():
    peak_en = 528.37
    #yield from pol_H(2.8)
    #yield from sleep(30)
    yield from plan_one_energy1(2.0,2.0,12,peak_en, 200)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.x,0.03)

def third_night():
    peak_en = 528.3
    yield from pol_V(1.9)
    yield from sleep(30)
    yield from plan_one_energy1(2.0,600,12,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.02)
    yield from mvr(cryo.x,0.02)

    peak_en = 527.97
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.x,0.03)

    peak_en = 528.07
    yield from sleep(30)
    yield from plan_one_energy1(3.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.x,0.03)

    peak_en = 528.57
    yield from sleep(30)
    yield from plan_one_energy1(3.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.x,0.03)

    peak_en = 528.87
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.x,0.03)


def fourth_afternoon():
    peak_en = 528.4
    #yield from pol_V(1.9)
    #yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.03)

def fourth_evening():
    peak_en = 528.4
    yield from pol_V(1.9)
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.03)

    peak_en = 528.2
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.03)

    peak_en = 528.1
    yield from sleep(30)
    yield from plan_one_energy1(5.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.03)

    peak_en = 528.0
    yield from sleep(30)
    yield from plan_one_energy1(5.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.03)

    peak_en = 528.6
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.03)


def fourth_evening():
    peak_en = 528.37
    yield from pol_V(1.9)
    yield from sleep(30)
    yield from plan_one_energy1(3.0,600,12,peak_en, 20)
    yield from mvr(cryo.y,-0.024)
    yield from mvr(cryo.z,-0.02)
    yield from mvr(cryo.x,0.02)

    peak_en = 528.17
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.012)
    yield from mvr(cryo.z,-0.01)
    yield from mvr(cryo.x,0.01)

    peak_en = 528.07
    yield from sleep(30)
    yield from plan_one_energy1(5.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.012)
    yield from mvr(cryo.z,-0.01)
    yield from mvr(cryo.x,0.01)

    peak_en = 527.97
    yield from sleep(30)
    yield from plan_one_energy1(5.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.012)
    yield from mvr(cryo.z,-0.01)
    yield from mvr(cryo.x,0.01)

    peak_en = 528.57
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.012)
    yield from mvr(cryo.z,-0.01)
    yield from mvr(cryo.x,0.01)


def fourth_evening_leftover():

    peak_en = 528.57
    yield from sleep(30)
    yield from plan_one_energy1(4.0,600,6,peak_en, 20)
    yield from mvr(cryo.y,-0.012)
    yield from mvr(cryo.z,-0.01)
    yield from mvr(cryo.x,0.01)

def fifth_dinner():
    yield from count([rixscam], num = 150, md={'reason':'test lvo/sto'})
    yield from count([rixscam], num = 150, md={'reason':'test lvo/sto'})
    yield from count([rixscam], num = 150, md={'reason':'test lvo/sto'})

    yield from plan_one_energy1(6.0,300,12,459.8, 40)

    yield from plan_one_energy1(6.0,300,12,460.55, 40)

    yield from mv(shutterb,'close')

def fifth_evening():
    exp_frame = 180 #180
    #for peak_en in np.linspace(459.1, 461.3, 12):
    for peak_en in np.linspace(461.1, 461.3, 2):

        yield from plan_one_energy1(6,exp_frame,10,peak_en,40)

    yield from plan_one_energy1(6,exp_frame,30,460.5,40)
    yield from plan_one_energy1(6,exp_frame,20,459.9,40)
      
    yield from mv(shutterb,'close')


def sixth_evening():
    exposure = 180

    #yield from pol_H(2.8)
    #yield from sleep(30)

    #yield from plan_one_energy1(5,exposure,40,459.9,40)
    yield from plan_one_energy1(6,exposure,20,459.9,40)
    #yield from plan_one_energy1(5,exposure,40,461.1,40)

    #yield from xas([sclr], pgm.en, 454, 470, 321) 

    #yield from pol_V(3.4)
    #yield from sleep(30)
      
    #yield from plan_one_energy1(5,exposure,20,459.9,40)
    #yield from plan_one_energy1(5,exposure,20,460.5,40)
    #yield from plan_one_energy1(5,exposure,20,461.1,40)

    yield from mv(shutterb,'close')


def test_xcam():
    yield from count([rixscam], num = 5)
    yield from sleep(10)
    yield from count([rixscam], num = 5)
    yield from sleep(10)
    








