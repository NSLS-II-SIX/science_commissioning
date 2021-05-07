def longscan():
    sclr_disable()
    ext_vg = 11
    
    total_time = 1200
    cyc = 9
    sec_x_pt = 5
    en=853.5

    yield from mv(cryo.x, 20.262, cryo.y, 9.3640,  cryo.z, 14.2980, cryo.t, 10)
    yield from rixs_dean(sec_x_pt,total_time,cyc,en,ext_vg)

    yield from mv(cryo.x, 19.5320, cryo.y, 9.3640, cryo.z, 15.980,  cryo.t, 30)
    yield from rixs_dean(sec_x_pt,total_time,cyc,en,ext_vg)

    yield from mv(cryo.x, 19.1920, cryo.y, 9.3640, cryo.z,  17.098,  cryo.t, 45)
    yield from rixs_dean(sec_x_pt,total_time,cyc,en,ext_vg)


def CT():
    sclr_disable()
    ext_vg = 11
    en = 853.5

    total_time = 120
    cyc = 1
    sec_x_pt = 5

    yield from pol_V(-2)
    yield from rixs_dean(sec_x_pt,total_time,cyc,en,ext_vg)

def quicktestrixs():
    ext_vg = 11
    en = 855.9

    total_time = 5
    cyc = 3
    sec_x_pt = 5
    yield from pol_H(-3)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)

    yield from pol_V(-2)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg)

  

def energy_map_SrNiO2():
    sclr_disable()
    yield from beamline_align_v2()
    yield from sleep(5)

    ext_vg = 100
    total_time = 300
    cyc = 1
    sec_x_pt = 1
    
    #yield from mv(pgm.en,850.0)
    yield from pol_V(-2)

    #E1 = list(np.arange(850,852,0.5))
    #for i in E1:
        #yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    #E2 = list(np.arange(852, 856.5, 0.25))
    #for i in E2:
        #yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
 
    E3 = list(np.arange(859, 860.1, 0.5))
    for i in E3:
        yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    yield from mv(pgm.en, 850.0)
    yield from pol_H(-3)

    E1 = list(np.arange(850, 852, 0.5))
    for i in E1:
        yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    E2 = list(np.arange(852, 856.5, 0.25))
    for i in E2:
        yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    E3 = list(np.arange(856.5, 860.1, 0.5))
    for i in E3:
        yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

def energy_dep_La4Ni3O8():
    sclr_disable()

    ext_vg = 200
    total_time = 600
    cyc = 1
    sec_x_pt = 2
    
    yield from pol_V(-2)

    E = list(np.arange(850.5, 853.6, 1))
    for i in E:
        yield from rixs_dean(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


def energy_dep_TiO2():
    
    ext_vg = 30
    total_time = 300
    cyc = 9
    sec_x_pt = 2
    
    yield from pol_H(-2.3)

    E = np.hstack([458.35,459,460,461.2])

    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    yield from pol_V(-2.2)

    E = np.hstack([458.35,460])

    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    yield from pol_H(-2.3)

    E = np.hstack([459,460,461.2])

    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


def energy_dep_KTL002():
    
    ext_vg = 30
    total_time = 300
    cyc = 9
    sec_x_pt = 2
    
    yield from pol_H(-2.3)

    # E = np.hstack([458.35,459,460,461.2])
    E = np.hstack([460])

    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    yield from pol_V(-2.2)
    E = np.hstack([458.35,460])

    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')





def energy_dep_KTL003():
    
    ext_vg = 30
    total_time = 300
    cyc = 8
    sec_x_pt = 2
 

    #yield from sleep(30)
    #yield from pol_V(-2.2)
    #yield from sleep(30)    
    #E = np.hstack([458.35,459,460,461.2])
    #E = np.hstack([457.4,462]) # ,456.78,462

    #for i in E:
     #   yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    #yield from sleep(30)
    #yield from pol_H(-2.3)
    #yield from sleep(30)     
    E = np.hstack([462])
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')







def energy_dep_TiO2_2():
    
    ext_vg = 30
    total_time = 300
    cyc = 9
    sec_x_pt = 2
    
    yield from pol_V(-2.2)

    E = np.hstack([460])
    

    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    yield from pol_H(-2.3)

def TiO2_angledep2():
    
    ext_vg = 30
    total_time = 300
    cyc = 9
    sec_x_pt = 3
    E = [460]
    
    yield from pol_V(-2.2)
    yield from sleep(30)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=15deg')

    yield from sleep(30)
    yield from pol_H(-2.3)
    yield from sleep(30)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=15deg')


def TiO2_angledep():
    
    ext_vg = 30
    total_time = 300
    cyc = 8
    sec_x_pt = 2
    E = [460]
    
    #yield from mv(cryo.t,30)
    #yield from mv(cryo.x,24.542)
    #yield from mv(cryo.z,13.0437)
    #yield from sleep(30)
    #yield from pol_H(-2.3)
    #for i in E:
    #    yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=30deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=30deg')

    yield from mv(cryo.t,45)
    yield from mv(cryo.x,23.677)
    yield from mv(cryo.z,13.374)
    yield from sleep(30)
    yield from pol_H(-2.3)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=45deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=45deg')

    yield from mv(cryo.t,60)
    yield from mv(cryo.x,22.655)
    yield from mv(cryo.z,13.604)
    yield from sleep(30)
    yield from pol_H(-2.3)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=60deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=60deg')

    sec_x_pt = 1
    yield from mv(cryo.t,70)
    yield from mv(cryo.x,21.985)
    yield from mv(cryo.z,13.895)
    yield from sleep(30)
    yield from pol_H(-2.3)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=70deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=70deg')


def KTL003_angledep():
    
    ext_vg = 30
    total_time = 300
    cyc = 8
    sec_x_pt = 4
    E = [460]
    
    #yield from mv(cryo.t,105)
    #yield from mv(cryo.x,20.6714)
    #yield from mv(cryo.z,15.985)
    #yield from sleep(30)
    #yield from pol_H(-2.3)
    #for i in E:
    #    yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=105deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=105deg')

    yield from mv(cryo.t,120)
    yield from mv(cryo.x,20.835)
    yield from mv(cryo.z,16.995)
    #yield from sleep(30)
    yield from pol_H(-2.3)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=120deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=120deg')

    yield from mv(cryo.t,135)
    yield from mv(cryo.x,21.039)
    yield from mv(cryo.z,18.079)
    #yield from sleep(30)
    yield from pol_H(-2.3)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=135deg')
    yield from pol_V(-2.2)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=135deg')



def KTL003_angledep_2():
    
    ext_vg = 30
    total_time = 300
    E = [460]

    sec_x_pt = 1
    cyc = 5
    # yield from mv(cryo.t,70)
    # yield from mv(cryo.x,21.992)
    # yield from mv(cryo.z,13.825)
    #yield from sleep(30)
    yield from pol_H(-2.3)
    #yield from sleep(30)
    for i in E:
        yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=80deg')
    #yield from sleep(30)
    
    #cyc = 5
    #yield from pol_V(-2.2)
    #yield from sleep(30)
    #for i in E:
    #    yield from rixs_one_energy(sec_x_pt,total_time,cyc,i,ext_vg, 'th=80deg')




def La4Ni3O8_oxy_one_energy():
    
    ext_vg = 15
    total_time = 600
    cyc = 12
    sec_x_pt = 5
    
    #yield from pol_V(-2.5)
    #yield from sleep(60)
    E = [529.85]

    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


    #yield from pol_H(-2.5)
    #yield from sleep(60)
    #E = [529.85]

    #for i in E:
     #   yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

def La4Ni3O8_oxy_angledep():
    
    ext_vg = 30
    total_time = 600
    cyc = 12
    sec_x_pt = 5
    E = [529.85]
    
    yield from mv(cryo.t,45)
    yield from mv(cryo.x,22.1885)
    yield from mv(cryo.z,13.015)
    yield from sleep(30)
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th=45deg')

    yield from mv(cryo.t,60)
    yield from mv(cryo.x,21.37)
    yield from mv(cryo.z,13.805)
    yield from sleep(30)
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th=45deg')

    yield from mv(cryo.t,80)
    yield from mv(cryo.x,20.673)
    yield from mv(cryo.z,15.075)
    yield from sleep(30)
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th=45deg')

def La4Ni3O8_oxy_angledep2():
    
    ext_vg = 30
    total_time = 600
    cyc = 12
    sec_x_pt = 5
    E = [529.85]
    
    yield from sleep(30)
    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th=90deg')


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



def rixs_dean(split_time, total_exp, cycles, energy, ext_vg, reason=''): 
    """Basic scan for one RIX spectrum for a single energy
	We plan to keep the scalars off!
	ensure that sclr_disable() has been run prior to running this macro. 

	Parameters
	-----------
    split_time: float
		exposure time of scan [seconds]
    total_exp: integer
		total integrated exposure time for a single scan (or cycle) [seconds]
    cycles: integer
		number of times to repeat a single total_exp 
    energy: float
		incident beamline energy [eV] for all cycles
    ext_vg : float
		exit slit vertical gap [um] for all cycles (note 11 is realy 10 and 7 is really 5)
    reason: string
		extra metadata to describe scan purpose.  use db[scan_id].start.reason to recover from database
    """
    def rixs_cleanup(sclr_set_time_n=1):
        "Set RIXS stuff off and scalar read time."
        print('\n\n...............Cleaning up................\n\n')
        yield from sleep(1)   
        yield from pzshutter_disable()
        yield from mv(sclr.preset_time, sclr_set_time_n)

    try:
        dets=[rixscam, sclr, stemp.temp.B.T]
        #dets=[rixscam, sclr,stemp.temp.B.T, voltage_dc, current_rbk]
        yield from mv(extslt.vg, ext_vg, extslt.hg, 150)
        yield from pzshutter_enable()
        yield from mv(rixscam.cam.acquire_time, split_time)  
        yield from mv(sclr.preset_time, split_time)
        yield from mv(pgm.en, energy)
        yield from mv(gvbt1, 'open')
        yield from sleep(5)
        pts = int(total_exp/split_time)

        import time
        fails.clear()
   
        for i in range(cycles):
            try:
                print('Starting cycle {} of {}' .format((i+1), cycles))
                yield from count(dets, num=pts, md = {'reason':'Length = '+str(np.int(pts*split_time))+' s -'+reason} ) 
                yield from mvr(cryo.y, 0.002) # if you do not want to move comment out this line
                #yield from sleep(3)
                #yield from mvr(cryo.x,-0.0012) # if you do not want to move comment out this line
                #yield from mvr(cryo.z,0.0026) # if you do not want to move comment out this line
                print('Ending cycle {} of {}\n' .format((i+1),cycles))
            except TimeoutError:
                print('*'*50)
                print(f"HAD A TIMEOUT on loop {i+1}")
                print(f"Exception: {TimeoutError}")
                print('*'*50)
                yield from bps.checkpoint()
                yield from bps.sleep(30)
                yield from bps.unstage(rixscam)
                fails.append((j, time.ctime()))
                continue

    except Exception:
        print('\n\nOOPS!  Possibly you stopped rixs_one_energy()')
        yield from rixs_cleanup()
        #return fails
        raise
    
    print('\n\n..........rixs_one_energy() finished normally...........\n\n')#this prints regardless of quiting during scan or letting it finish
    yield from rixs_cleanup()    

    return fails
