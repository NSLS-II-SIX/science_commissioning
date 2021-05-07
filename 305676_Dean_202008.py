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


def energy_dep_La4Ni3O8_oxygen():
    
    ext_vg = 30
    total_time = 600
    cyc = 5
    sec_x_pt = 5
    
    #yield from pol_V(-2.5)

    E = np.hstack([528,list(np.arange(529,531.1,0.2)),532,534,536.7])

    for i in E:
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

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
