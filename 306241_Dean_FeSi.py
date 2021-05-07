
def FeSi_hs():
    ext_vg = 25
    sec_x_pt = 4
    total_time =  600
    e_peak =  708.9
    E = [e_peak-0.2 ,e_peak-1.7]
    cyc=12
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)
    cyc=6
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)



def FeSi_E_map_3():
    # FeSi -- xstal
  
    ext_vg = 25
    sec_x_pt = 4
    total_time = 600


    E = np.arange(705,706.1,0.5)
    cyc=2
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


    E = np.arange(706.5,708.6,0.2)
    cyc=3
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)
    
    
    E = np.arange(709,710.1,0.5)
    cyc=2
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)



def FeSi_E_map_2():
    # FeSi -- xstal
  
    ext_vg = 25
    sec_x_pt = 4
    total_time = 600


    E = np.arange(705,706.1,0.5)
    cyc=2
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


    E = np.arange(706.5,708.6,0.2)
    cyc=3
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)
    
    
    E = np.arange(709,710.1,0.5)
    cyc=2
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


def FeSi_E_map():
    # FeSi -- xstal
  
    ext_vg = 25
    sec_x_pt = 4
    total_time = 600


    E = np.arange(704,706.1,0.5)
    cyc=2
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


    E = np.arange(706.2,710.1,0.2)
    cyc=3
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)
    
    
    E = np.arange(710.5,713.1,0.5)
    cyc=2
    for i in E:
        # yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)





def rixs_en_map_FeSi(split_time, total_exp, cycles, energy, ext_vg, reason=''): 
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
    def rixs_cleanup_1(sclr_set_time_n=1):
        "Set RIXS stuff off and scalar read time."
        print('\n\n...............Cleaning up................\n\n')
        yield from sleep(1)   
        yield from pzshutter_disable()
        yield from mv(sclr.preset_time, sclr_set_time_n)

    try:
        dets=[rixscam, sclr]
        #dets=[rixscam, sclr, stemp.temp.B.T]
        #dets=[rixscam, sclr,stemp.temp.B.T, voltage_dc, current_rbk]
        yield from mv(extslt.vg, ext_vg, extslt.hg, 150)
        yield from pzshutter_enable()
        yield from mv(rixscam.cam.acquire_time, split_time)  
        yield from mv(sclr.preset_time, split_time)
        yield from mv(pgm.en, energy)
        yield from mv(gvbt1, 'Open')
        yield from sleep(5)
        pts = int(total_exp/split_time)

        import time
        fails.clear()
   
        for i in range(cycles):
            try:
                print('Starting cycle {} of {}' .format((i+1), cycles))
                yield from count(dets, num=pts, md = {'reason':'Length = '+str(np.int(pts*split_time))+' s -'+reason} ) 
                yield from mvr(cryo.y, -0.002) # if you do not want to move comment out this line
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
        yield from rixs_cleanup_1()
        #return fails
        raise
    
    print('\n\n..........rixs_one_energy() finished normally...........\n\n')#this prints regardless of quiting during scan or letting it finish
    yield from rixs_cleanup_1()    

    return fails
