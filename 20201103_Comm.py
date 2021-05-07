def test_rixscam():
    cycles = 100
    for i in range(0,cycles):
        yield from count([rixscam], num = 120)
        print(i)


def hBN_th36_Emap():
    ext_vg = 20
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_V()
    E = [401.05,401.3,401.55,402.3,405.3,406.3,406.7]#,407,408,409,410]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')
        print(i)



def Pan_Wed_AMhighQ():

    ext_vg = 12
    total_time = 600

    E1 = 854.3
    cyc = 12
    yield from sleep(30)
    yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)

    E1 = 855.4
    cyc = 3
    yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)

def Pan_Tuesday_AMdispersion():

    ext_vg = 12
    total_time = 600

    E1 = 854.25
    cyc = 12
    yield from sleep(30)
    yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)

def Pan_Monday_dinner():

    ext_vg = 12
    total_time = 600

    E1 = 854.2
    cyc = 9
    yield from sleep(30)
    yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)

    #E1 = 855.5
    #cyc = 3
    #yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)



def Pan_Monday_lunch():

    ext_vg = 12
    total_time = 600

    E1 = 854.3
    cyc = 6
    yield from sleep(30)
    yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)

    E1 = 854.4
    cyc = 6
    yield from pol_V(-5.5)
    yield from sleep(30)
    yield from rixs_one_energy_1(5,total_time,cyc,E1,ext_vg)



def Peng_lastNight():

    ext_vg = 12
    total_time = 600

    E1 = 932.55
    cyc = 12
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E1,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E3 = 932.3
    cyc = 15
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E3,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E3 = 931.85
    cyc = 24
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E3,ext_vg)


def Peng_OP_TueMorn():
    ext_vg = 12
    total_time = 600

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E5 = 931.85
    cyc = 24
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E5,ext_vg)


def Peng_OP_EPC_HighTemp():

    ext_vg = 12
    total_time = 600

    E1 = 932.55
    cyc = 12
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E1,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E3 = 932.3
    cyc = 15
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E3,ext_vg)

    # yield from mv(extslt.vg,100)
    # yield from mv(gvbt1,'Open')
    # yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    # E4 = 932.05
    # cyc = 15
    # yield from sleep(30)
    # yield from rixs_one_energy_1(4,total_time,cyc,E4,ext_vg)
    
    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E5 = 931.85
    cyc = 24
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E5,ext_vg)

    # yield from mv(extslt.vg,100)
    # yield from mv(gvbt1,'Open')
    # yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    # E2 = 932.45
    # cyc = 12
    # yield from sleep(30)
    # yield from rixs_one_energy_1(4,total_time,cyc,E2,ext_vg)


    # yield from mv(extslt.vg,100)
    # yield from mv(gvbt1,'Open')
    # yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    # E0 = 932.75
    # yield from sleep(30)
    # yield from rixs_one_energy_1(4,total_time,cyc,E0,ext_vg)





def Peng_OP_Q_AND_EPC_secondNight():
    ext_vg = 12
    total_time = 600
    cyc = 21
 
    E1 = 932.7
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E1,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E2 = 931.8
    yield from sleep(30)
    cyc = 42
    yield from rixs_one_energy_1(4,total_time,cyc,E2,ext_vg)



def Peng_test():
    yield from mv(gvbt1,'Open')
    yield from mv(extslt.vg,100)
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)

def Peng_OP_Q_AND_EPC():
    ext_vg = 12
    total_time = 600
    cyc = 12
 
    E1 = 932.5
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E1,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E2 = 932.4
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E2,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E3 = 932.25
    cyc = 15
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E3,ext_vg)

    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E4 = 932.0
    cyc = 21
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E4,ext_vg)
    
    yield from mv(extslt.vg,100)
    yield from mv(gvbt1,'Open')
    yield from xas([sclr,ring_curr,rixscam],pgm.en,930,936,61,1)
    E5 = 931.7
    cyc = 30
    yield from sleep(30)
    yield from rixs_one_energy_1(4,total_time,cyc,E5,ext_vg)


       
def Fe2O3_RIXS():
    ext_vg = 15
    total_time = 600
    cyc=4
 
    # E1 = 708.9
    # yield from mv(epu1.phase,-19.295)
    # yield from mv(epu1.gap,28.574)
    # yield from mv(pgm.en,E1)
    # yield from sleep(30)
    # yield from rixs_one_energy_1(2,total_time,cyc,E1,ext_vg)

    # E2 = 710.7
    # yield from mv(epu1.phase,-19.295)
    # yield from mv(epu1.gap,28.611)
    # yield from mv(pgm.en,E2)
    # yield from sleep(30)
    # yield from rixs_one_energy_1(2,total_time,cyc,E2,ext_vg)


    # yield from mv(epu1.phase,19.295)
    # yield from mv(epu1.gap,28.548)
    # yield from mv(pgm.en,E2)
    # yield from sleep(30)
    # yield from rixs_one_energy_1(2,total_time,cyc,E2,ext_vg)

    E2 = 714
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.617)
    yield from mv(pgm.en,E2)
    yield from sleep(30)
    yield from rixs_one_energy_1(3,total_time,cyc,E2,ext_vg)

    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.68)
    yield from mv(pgm.en,E2)
    yield from sleep(30)
    yield from rixs_one_energy_1(3,total_time,cyc,E2,ext_vg)








def FeGeTe_E_map():
  
    ext_vg = 20
    total_time = 600
    cyc=2

    E = np.arange(707.1,707.5+0.1,0.2)
    sec_x_pt = 4
    for i in E:
        yield from sleep(3)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)

    E = np.arange(707.7,707.9+0.1,0.2)
    sec_x_pt = 3
    for i in E:
        yield from sleep(3)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)
    
    E = np.arange(708,708.5+0.05,0.1)
    sec_x_pt = 3
    for i in E:
        yield from sleep(3)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)

    E = np.arange(708.7,710.3+0.1,0.2)
    sec_x_pt = 3
    for i in E:
        yield from sleep(3)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)

    E = np.arange(710.5,711.3+0.1,0.2)
    sec_x_pt = 4
    for i in E:
        yield from sleep(3)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


def YIG_20210204():
    # YIG -- xstal
    ext_vg = 12
    total_time = 600
    cyc = 6 #30   
    sec_x_pt = 2
	##########################################################################################
    energy_d = 710.1
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.599)
    yield from mv(pgm.en,710.1)
    yield from sleep(15)   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)


    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.536)
    yield from mv(pgm.en,710.1)
    yield from sleep(15)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)




def YIG_20210205():
    # YIG -- xstal
    ext_vg = 12
    total_time = 600
    cyc = 3 #30   
    sec_x_pt = 2
	##########################################################################################
    energy_d = 710.1
    y_pos=[7,7.2,7.4,7.6,7.8]
    for i in y_pos:
        yield from mv(cryo.y,i)
        yield from sleep(2)
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)
       

def YIG_xcut():
    #yield from mv(epu1.phase,19.295)
    #yield from mv(epu1.gap,28.537) #update energy
    #yield from mv(pgm.en,710.15) #update energy
    #yield from mv(extslt.vg,100)
    #yield from sleep(30) 
    
    cen_y= 7.67 #check position for y center
    yield from mv(cryo.y,cen_y-0.6)
    for s in np.arange(cen_y-0.6,cen_y+0.65,0.1):
        yield from mv(cryo.y,s)
        yield from mv(cryo.x, 20.38) #check beginning of x scan
        yield from sleep(2)  
        yield from rel_scan([sclr],cryo.x,0,1.5,31) #check the range for x scan
       
def YIG_XMCD_L3():

    yield from mv(extslt.vg,200)
    yield from mv(sclr.preset_time,1)


 
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.503)
    yield from mv(pgm.en,705.5)
    yield from sleep(30)
    yield from scan([rixscam,sclr,ring_curr],pgm.en,705.5,715.5,epu1.gap,28.503,28.711,101)


    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.44)
    yield from mv(pgm.en,705.5)
    yield from sleep(30)
    yield from scan([rixscam,sclr,ring_curr],pgm.en,705.5,715.5,epu1.gap,28.44,28.648,101)





    # yield from mv(epu1.phase,19.295)
    # yield from mv(epu1.gap,28.536)
    # yield from mv(pgm.en,710.1)


def YIG_XMCD():

    yield from mv(extslt.vg,100)
    yield from mv(sclr.preset_time,2)

    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.325)
    yield from mv(pgm.en,700)
    yield from sleep(15)
    yield from scan([sclr,ring_curr],pgm.en,700,735,epu1.gap,28.325,29.055,351)

    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.388)
    yield from mv(pgm.en,700)
    yield from sleep(15)
    yield from scan([sclr,ring_curr],pgm.en,700,735,epu1.gap,28.388,29.118,351)

    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.536)
    yield from mv(pgm.en,710.1)



def YIG_20210130():
    # YIG -- xstal
    ext_vg = 12
    total_time = 600
    cyc = 6 #30   
    sec_x_pt = 2
	##########################################################################################
    energy_d = 710.05
    y_pos=[11.3,11.5,11.6,11.8,11.9,12.1]
    for i in y_pos:
        yield from mv(cryo.y,i)
        yield from sleep(2)
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)
    
    


def FeSi_E_map2():
    # FeSi -- xstal
    ext_vg = 25
    sec_x_pt = 4
    total_time = 600
    cyc=3

    yield from pol_H(-4.2)
    yield from sleep(10)

    yield from rixs_one_energy_1(sec_x_pt,total_time,3,708.2,ext_vg)
    yield from sleep(5)   
    yield from rixs_one_energy_1(sec_x_pt,total_time,3,707.7,ext_vg)



def FeSi_E_map():
    # FeSi -- xstal
  
    ext_vg = 25
    sec_x_pt = 4
    total_time = 600
    cyc=3

    yield from rixs_one_energy_1(sec_x_pt,total_time,1,705.2,ext_vg)
    yield from sleep(5)   
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,706.2,ext_vg)

    E = np.arange(707.2,711.3,0.5)
    for i in E:
        yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


    yield from rixs_one_energy_1(sec_x_pt,total_time,1,712.2,ext_vg)
    yield from sleep(5)   
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,713.2,ext_vg)



def FGT_20201206():
    # Fe3GeTe2 -- xstal
    sclr_disable()
    ext_vg = 12
    sec_x_pt = 3
    total_time = 300
    cyc=12

    E = list([710.156])
    for i in E:
        yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)

    cyc=15
    E = list([708.78])
    for i in E:
        yield from sleep(5)   
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg)


def FGT_20201205():
    # Fe3GeTe2 -- xstal
    sclr_disable()
    ext_vg = 22
    sec_x_pt = 2
    total_time = 600
    # E = list(np.arange(707.8, 711.6, 0.2))
    E = list(np.arange(707, 707.6, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,2,i,ext_vg, 'E_map FGT-crystal')


def Bi2212_20201109():
    sclr_disable()
    ext_vg = 25 #12
    energy=932.4
    sec_x_pt = 4
    total_time = 600
    cyc = 6
    
	##########################################################################################

    # yield from pol_V(-2.9)
    # yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)


    # yield from pol_H(-3.5)
    # yield from sleep(30)
    # yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)

    # yield from pol_V(-2.9)
    # yield from sleep(30)


   
def YIG_20201130():
    ext_vg = 12
    total_time = 600
    cyc = 9 #30   
    sec_x_pt = 4
	##########################################################################################
    energy = 710.3

    #yield from mv(keithley_output,'OFF')
    #yield from mv(keithley_output_B,'OFF')

    #yield from mv(current_dc_B,0.035)
    #yield from mv(keithley_output,'ON')
    #yield from mv(keithley_output_B,'ON')

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)

    #yield from mv(current_dc_B,0.0)
    #yield from mv(keithley_output,'OFF')
    #yield from mv(keithley_output_B,'OFF')

def YIG_20201103():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 23
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(707.9, 712.6, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map YIG-crystal')
    sclr_enable()

   
def YIG_20201105():
    # YIG -- xstal
    ext_vg = 15
    total_time = 600
    cyc = 14 #30   
    sec_x_pt = 5
	##########################################################################################
    energy_d = 535
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)
    
    energy_d = 537.4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)



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
        dets=[rixscam, sclr]
        #dets=[rixscam, sclr, stemp.temp.B.T]
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
                yield from mvr(cryo.y, -0.004) # if you do not want to move comment out this line
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
