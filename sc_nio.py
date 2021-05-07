def NiO_OK_highRes_LH():

    ext_vg = 11
    total_time = 600
    E = list(np.arange(531.7,531.9,0.5)) # 531.7
    cyc = 18
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th20')

def NiO_OK_highRes_v2():

    ext_vg = 11
    total_time = 600
    cyc = 6
    E = list(np.arange(531.1,531.2,0.5)) # 531.7
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th20')
    E = list(np.arange(531.7,531.9,0.5)) # 531.7
    cyc = 18
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th20')


def energy_dep_NiO_OK_v3():
    
    #yield from pol_V(-2.5)
    sclr_disable()
    ext_vg = 30
    total_time = 900
    cyc = 1
    sec_x_pt = 5
    

    E = list(np.arange(530, 532.55, 0.1))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map NiO')
    
    sclr_enable()
    yield from mv(extslt.vg, 150)
    yield from xas([sclr,ring_curr],pgm.en,530,534,41,1)
    
    yield from mv(pgm.en,532)
    yield from pol_H(-3.0)
    yield from beamline_align_v3()
    
    yield from xas([sclr,ring_curr],pgm.en,530,534,41,1)
    sclr_disable()
    ext_vg = 30
    total_time = 900
    cyc = 1
    sec_x_pt = 5
    
    
    E = list(np.arange(530, 532.55, 0.1))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map NiO')
    
    sclr_enable()

def rixs_en_map(split_time, total_exp, cycles, energy, ext_vg, reason=''): 
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
                #yield from mvr(cryo.y, 0.002) # if you do not want to move comment out this line
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
