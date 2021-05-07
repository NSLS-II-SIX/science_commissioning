def RNO_night():

    ext_vg = 11
    sec_x_pt = 3
    total_time = 600
    cyc = 4

    energy = 853.75

    #yield from pol_H(-2.5)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg, 'RNO')
    
    energy = 855.25
  
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg, 'RNO')




def RNO_20200830():

    sclr_disable()
    #####parameters####
    ext_vg = 30 # vertical slit opening
    sec_x_pt = 3 # exposure time for RIXScam
    total_time = 300 # total counting time
    cyc = 1 # number of scans

    #############################################
    # E = list(np.arange(575.6, 581.7, 0.2))
    # E = list(np.arange(856.125, 858.1, 0.125))
    E = list(np.arange(856.625, 858.1, 0.125))
    ############################################
    # set-up the polarization
    #yield from pol_H(-2.5)
    #yield from mv(pgm.en,E[0])

    #############################################
    for i in E:
        yield from mvr(cryo.y, 0.003) # move sample a tiny bit after previous scan
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map RNO')
    sclr_enable()


def RNO_20200829():

    sclr_disable()
    #####parameters####
    ext_vg = 30 # vertical slit opening
    sec_x_pt = 2 # exposure time for RIXScam
    total_time = 300 # total counting time
    cyc = 1 # number of scans

    #############################################
    # E = list(np.arange(575.6, 581.7, 0.2))
    E = list(np.arange(852.5, 856.1, 0.125))
    ############################################
    # set-up the polarization
    #yield from pol_H(-2.5)
    #yield from mv(pgm.en,E[0])

    #############################################
    for i in E:
        yield from mvr(cryo.y, 0.003) # move sample a tiny bit after previous scan
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map RNO')

    sec_x_pt = 3 # exposure time for RIXScam
    total_time = 300 # total counting time
    cyc = 1 # number of scans

    #############################################
    # E = list(np.arange(575.6, 581.7, 0.2))
    # E = list(np.arange(856.125, 858.1, 0.125))
    E = list(np.arange(856.625, 858.1, 0.125))
    ############################################
    # set-up the polarization
    #yield from pol_H(-2.5)
    #yield from mv(pgm.en,E[0])

    #############################################
    for i in E:
        yield from mvr(cryo.y, 0.003) # move sample a tiny bit after previous scan
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map RNO')
    sclr_enable()


def LCO_20200828():

    sclr_disable()
    #####parameters####
    ext_vg = 40 # vertical slit opening
    sec_x_pt = 5 # exposure time for RIXScam
    total_time = 900 # total counting time
    cyc = 1 # number of scans

    #############################################
    # E = list(np.arange(575.6, 581.7, 0.2))
    E = list(np.arange(576.4, 581.7, 0.2))
    ############################################
    # set-up the polarization
    yield from pol_H(-2.5)
    yield from mv(pgm.en,E[0])

    #############################################
    for i in E:
        yield from mvr(cryo.y, 0.003) # move sample a tiny bit after previous scan
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map LCO')

    sclr_enable()




def LS5BO_20200827():
    sclr_disable()


	#####parameters####
    ext_vg = 40 # vertical slit opening
    sec_x_pt = 5 # exposure time for RIXScam
    total_time = 900 # total counting time
    cyc = 1 # number of scans

	#############################################
    E = list(np.arange(575.4, 582.1, 0.2))

	#############################################
	# set-up the polarization
    yield from pol_H(-2.5)
    yield from mv(pgm.en,E[0])

	#############################################
    for i in E:
        yield from mvr(cryo.y, 0.003) # move sample a tiny bit after previous scan
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map L5BO')

    sclr_disable()







#########################################################################################
def L5BO_20200826():
    sclr_disable()
    #####parameters####
    ext_vg = 40 # vertical slit opening
    sec_x_pt = 5 # exposure time for RIXScam
    total_time = 900 # total counting time
    cyc = 1 # number of scans

    #############################################
    E = list(np.arange(575, 581.1, 0.2))

    #############################################
    # set-up the polarization
    yield from pol_H(-2.5)
    yield from mv(pgm.en,E[0])

	#############################################
    for i in E:
        yield from mvr(cryo.y, 0.003) # move sample a tiny bit after previous scan
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map L5BO')

    sclr_disable()

#########################################################################################
def LCO_20200826():
    sclr_disable()
    ext_vg = 25
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(707.4, 712.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map LCO')

#########################################################################################
def dinner_plan():

    ext_vg = 30
    sec_x_pt = 5
    total_time = 900
    cyc = 1

    energy = 578.6

    yield from pol_H(-2.5)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg, 'LCO')

    yield from pol_V(-2)	
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg, 'LCO')


def LaCrO3_plan():

    ext_vg = 20
    sec_x_pt = 5
    total_time = 600
    cyc = 12

    energy = 576.8

    #yield from pol_H(-2.5)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg, 'LCO')
    
    energy = 577.8
  
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg, 'LCO')

















#############################################################################################################################
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




