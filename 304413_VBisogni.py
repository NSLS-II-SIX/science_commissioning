def high_res_Fe_54uc_plane():
    ext_vg = 15
    total_time = 900
    cyc = 16
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc_tth150_th10')

def high_res_Fe_17uc_plane():
    ext_vg = 15
    total_time = 900
    cyc = 12
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_tth150_th10')

def high_res_Fe_3uc_plane():
    ext_vg = 15
    total_time = 900
    cyc = 5
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_tth150_th10')

def high_res_Fe_3uc_17uc_tth130():
    ext_vg = 15
    total_time = 900
    cyc = 5
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_tth150_th10')

    #yield from mv(cryo.t, 10)
    #yield from mv(cryo.x, 25.555)
    #yield from mv(cryo.y, 58.7)
    #yield from mv(cryo.z, 16.02)
    #yield from sleep(30)
    #ext_vg = 15
    #total_time = 600
    #cyc = 6
    #en = 707.8
    #pol is H
    #sec_x_pt = 5
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc_tth150_th10')



def high_res_Fe_54uc_tth150_th11():
    ext_vg = 15
    total_time = 600
    cyc = 6
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc_tth150_th11')


def high_res_Fe_3uc_tth150_th10():
    ext_vg = 15
    total_time = 600
    cyc = 3
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_17uc_tth150_th10')


def high_res_Fe_3uc_tth150_offres():
    ext_vg = 15
    total_time = 600
    cyc = 1
    en = 704
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_tth150_offres')


def high_res_Fe_3uc_tth150():
    ext_vg = 15
    total_time = 900
    cyc = 12
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_tth150')


def high_res_Fe_17uc_tth150():
    ext_vg = 15
    total_time = 600
    cyc = 9
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_17uc_tth150')


def high_res_Fe_3uc_17uc_tth130():
    ext_vg = 15
    total_time = 900
    cyc = 12
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_tth130')

    yield from mv(cryo.x, 23.020)
    yield from mv(cryo.y, 71.4)
    yield from mv(cryo.z, 16.5)
    yield from sleep(30)
    ext_vg = 15
    total_time = 600
    cyc = 9
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_17uc_tth130')





def high_res_Fe_3uc_thinAl():
    ext_vg = 15
    total_time = 900
    cyc = 12
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc_thinAl')

def emission():
    ext_vg = 500
    total_time = 300
    cyc = 1
    en = 700
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'emission')


def high_res_Fe_54uc_tth130():
    ext_vg = 15
    total_time = 600
    cyc = 6
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc_tth130')


def high_res_Fe_17uc_tth90():
    ext_vg = 15
    total_time = 600
    cyc = 1
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_17uc_tth90')


def high_res_Fe_3uc_17uc():
    ext_vg = 15
    total_time = 900
    cyc = 12
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc')

    yield from mv(cryo.x, 25.358)
    yield from mv(cryo.y, 71.012)
    yield from mv(cryo.z, 15.35)
    yield from sleep(30)
    ext_vg = 15
    total_time = 600
    cyc = 9
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_17uc')

    # these are extra scans to fill time
    yield from mv(cryo.x, 23.372)
    yield from mv(cryo.y, 65.812)
    yield from mv(cryo.z, 17.77)
    yield from sleep(30)

    ext_vg = 15
    total_time = 900
    cyc = 8
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_3uc')


def high_res_Fe_54uc():
    ext_vg = 15
    total_time = 600
    cyc = 6
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc')


def high_res_Fe_6uc():
    ext_vg = 15
    total_time = 600
    cyc = 12
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_6uc')

def high_res_Fe_30uc():
    ext_vg = 15
    total_time = 600
    cyc = 3
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_30uc')

def high_res_Fe_100uc():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_100uc')


def energy_map_lvco_v2():
    ext_vg = 15
    total_time = 900
    cyc = 1
    
    #yield from pol_V()
    #E1 = list(np.arange(528.8,529.3,0.2))
    #for i in E1:
    #    sec_x_pt = 3
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E2 = list(np.arange(531,532.3,0.2))
    for i in E2:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    E3 = list(np.arange(532.4,534,0.2))
    for i in E3:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


    yield from mv(pgm.en,530)
    yield from pol_H()
    yield from beamline_align_v2()
    yield from sleep(5)

    E1 = list(np.arange(528.8,529.3,0.2))
    for i in E1:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E2 = list(np.arange(529.4,532.3,0.2))
    for i in E2:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    E3 = list(np.arange(532.4,534,0.2))
    for i in E3:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


def energy_map_lvco_v3():
    ext_vg = 15
    total_time = 900
    cyc = 1
    
    #yield from pol_V()
    #E1 = list(np.arange(528.8,529.3,0.2))
    #for i in E1:
    #    sec_x_pt = 3
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E2 = list(np.arange(529.8,531,0.2))
    for i in E2:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')



def energy_map_lvco_v4():
    ext_vg = 15
    total_time = 900
    cyc = 1
    
    yield from pol_V()
    E1 = list(np.arange(528.4,528.7,0.2))
    for i in E1:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    yield from mv(extslt.vg,150)
    yield from xas([sclr],pgm.en,527,540,131,1)
    yield from pol_H() # Tom Caswell
    yield from mv(extslt.vg,15)
    yield from sleep(60) # sempre sia lodato
    yield from beamline_align_v2()
    yield from mv(extslt.vg,150)
    yield from xas([sclr],pgm.en,527,540,131,1)



def energy_map_lvco_v5():
    ext_vg = 15
    total_time = 900
    cyc = 1

    E0 = list(np.arange(528.4,528.7,0.2))
    for i in E0:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E1 = list(np.arange(528.8,529.3,0.2))
    for i in E1:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E2 = list(np.arange(529.4,532.3,0.2))
    for i in E2:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    E3 = list(np.arange(532.4,533.5,0.2))
    for i in E3:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


def energy_map_lvco_v6():
    ext_vg = 15
    total_time = 900
    cyc = 1
    #pol is H
    E0 = list(np.arange(528.4,528.7,0.2))
    for i in E0:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
        yield from mvr(cryo.y,0.001)

    E1 = list(np.arange(529,529.3,0.2))
    for i in E1:
        sec_x_pt = 3 
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
        yield from mvr(cryo.y,0.001)

    E2 = list(np.arange(529.4,532.3,0.2))
    for i in E2:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
        yield from mvr(cryo.y,0.001) 
    
    E3 = list(np.arange(532.4,533.5,0.2))
    for i in E3:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
        yield from mvr(cryo.y,0.001)


def energy_map_lvco_v7():
    ext_vg = 15
    total_time = 900
    cyc = 1
    #pol is H
    E0 = list(np.arange(530.2,530.7,0.2))
    for i in E0:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
        yield from mvr(cryo.y,0.001)


def high_res_LCVO():
    ext_vg = 15
    total_time = 900
    cyc = 2
    en = 529.4
    #pol is V
    # B = 0.25 T, theta =15, LH - 8 scans of these are sufficient!!
    sec_x_pt = 5
    for i in range(0,3):
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'E_map')
        yield from mvr(cryo.y,0.001)
        yield from sleep(5)
        print (cyc*(i+1))

    yield from pol_H()
    yield from sleep(10)
    yield from beamline_align_v2()
    yield from sleep(10)

    for i in range(0,5):
       yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'E_map')
       yield from mvr(cryo.y,0.001)
       yield from sleep(5)
       print (cyc*(i+1))


def rixs_one_energy(split_time, total_exp,cycles,energy, ext_vg,reason=''): 
    sclr_disable()
    #dets = [rixscam]#[rixscam, sclr]
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
        #yield from mvr(cryo.y,0.007)
        #yield from mvr(cryo.z,0.0017) #in case of sample on wedge
        #yield from mvr(cryo.x,-0.0017)
    yield from pzshutter_disable()

    sclr_enable()
    yield from mv(gvbt1,'close') # close GV before CCD
    #yield from mv(shutterb,'close') # close ShutterB before CCD


def rixs_one_energy_nosh(split_time, total_exp,cycles,energy, ext_vg,reason=''): 
    dets = [rixscam]
    yield from mv(extslt.vg,ext_vg, extslt.hg, 150)
    #yield from pzshutter_enable()
    yield from mv(gvbt1,'open') # open GV before CCD
    yield from mv(rixscam.cam.acquire_time, split_time)
    yield from mv(pgm.en,energy)
    yield from sleep(5)
    pts = int(total_exp/split_time)
    for i in range(0,cycles):
        print('Starting cycle {} of {}' .format((i+1),cycles))
        yield from count(dets, num=pts, md = {'reason':'Length = '+str(total_exp*cycles)+' s -'+reason} )
        print('Ending cycle {} of {}\n' .format((i+1),cycles))

def energy_map_coso():
    ext_vg = 10
    total_time = 360
    cyc = 1
    #E_peak = 930.79 eV
    sclr_disable()
    yield from pzshutter_enable()

    #E1 = list(np.arange(927.5,929.39,0.2))
    #for i in E1:
       #sec_x_pt = 3
       #yield from rixs_one_energy_nosh(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    #E2 = list(np.arange(929.5,929.79,0.2))
    #for i in E2:
        #sec_x_pt = 2
        #yield from rixs_one_energy_nosh(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E3 = list(np.arange(929.8,931.39,0.2))
    for i in E3:
        sec_x_pt = 1
        yield from rixs_one_energy_nosh(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    E4 = list(np.arange(931.5,932.39,0.2))
    for i in E4:
        sec_x_pt = 2
        yield from rixs_one_energy_nosh(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    yield from pzshutter_disable()

def High_Stats():
    yield from mv(extslt.vg,150, extslt.hg, 150)
   
    target_Emax = yield from xas([sclr],pgm.en,929,932,61)
    sclr_disable()
    print('The peak energy is {:.2f} eV' .format(target_Emax))

    ext_vg = 11
    total_time = 600
    yield from mv(gvbt1,'open')
    yield from pzshutter_enable()
    #yield from rixs_one_energy_nosh(5,total_time,6,target_Emax,ext_vg, 'High Stat')
    #yield from rixs_one_energy_nosh(5,total_time,6,target_Emax-0.3,ext_vg, 'High Stat')
    #yield from rixs_one_energy_nosh(5,total_time,7,target_Emax-0.9,ext_vg, 'High Stat')
    yield from rixs_one_energy_nosh(5,total_time,5,target_Emax-1.6,ext_vg, 'High Stat')
    #yield from mv(extslt.vg,100, extslt.hg, 150)
    #target_Emax = yield from xas([sclr],pgm.en,929,932,61)
    #sclr_disable()
    yield from rixs_one_energy_nosh(5,total_time,6,target_Emax+0.2,ext_vg, 'High Stat')
    yield from rixs_one_energy_nosh(5,total_time,7,target_Emax+0.7,ext_vg, 'High Stat')
    yield from rixs_one_energy_nosh(5,total_time,7,target_Emax+1.1,ext_vg, 'High Stat')
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
    sclr_enable()


def One_High_Stats():
    ext_vg = 11
    total_time = 600
    target_Emax = 708.6
    yield from mv(gvbt1,'open')
    yield from pzshutter_enable()
    yield from rixs_one_energy_nosh(5,total_time,12,target_Emax,ext_vg, 'High Stat')
    yield from pzshutter_disable()
    yield from mv(gvbt1,'close')
    sclr_enable()




