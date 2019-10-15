### For users to run at start of bluesky

RE.md['proposal'] = 'hBN - 305353' #'commissioning' #'bdt' #'commissioning'
RE.md['group'] = 'BNL' # 'SIX'
RE.md['project'] = 'hBN'#'' #'commissioning'
RE.md['orientation'] = ''
RE.md['SAF'] = '304958'
#RE.md.pop('SAF')
RE.md.pop('orientation')
RE.md.pop('project')
RE.md.pop('group')


### To change polarization  ###
# RE(pol_V(0.75))
# RE(pol_H(0.5))
### BASIC SCAN ####
fails = []
def rixs_one_energy_1(split_time, total_exp,cycles,energy, ext_vg,reason='', disable_sclr_plt = True): 
    '''Basic scan for one RIX spectrum for a single energy
    split_time\t :\t float - exposure time of scan [seconds]
    total_exp\t :\t integer - total integrated exposure time for a single scan (or cycle) [seconds]
    cycles\t :\t integer - number of times to repeat a single total_exp 
    energy\t :\t float - incident beamline energy [eV] for all cycles
    ext_vg\t :\t float - exit slit vertical gap [um] for all cycles (note 11 is realy 10 and 7 is really 5)
    reason\t :\t string - extra metadata to describe scan purpose.  use db[scan_id].start.reason to recover from database
    '''
    def rixs_cleanup(sclr_set_time_n):
        # this part is the clean up
        print('\n\n...............Cleaning up................\n\n')
        yield from sleep(1)   
        yield from pzshutter_disable()
        sclr_enable()        
        yield from mv(sclr.preset_time,sclr_set_time_n)
          
        #yield from mv(gvbt1,'close') # close GV before CCD # this magically closes when the scan finishes or is interupted.  Don't understand why.
    

    
    sclr_set_time=sclr.preset_time.value
    try:
        if disable_sclr_plt == True:
            sclr_disable()   
        else:
	        sclr_enable()
        dets=[rixscam, sclr,stemp.temp.B.T]
        #dets=[rixscam]
        yield from mv(extslt.vg,ext_vg, extslt.hg, 150)
        yield from pzshutter_enable()
        yield from mv(rixscam.cam.acquire_time, split_time)  
        yield from mv(sclr.preset_time, split_time)
        yield from mv(pgm.en,energy)
        yield from mv(gvbt1,'open')
        yield from sleep(5)
        pts = int(total_exp/split_time)

        import time
        fails.clear()
   
        for i in range(0,cycles):
            try:
                print('Starting cycle {} of {}' .format((i+1),cycles))
                yield from count(dets, num=pts, md = {'reason':'Length = '+str(np.int(pts*split_time))+' s -'+reason} ) 
                #yield from mvr(cryo.y,0.002)
                yield from sleep(3)
                print('Ending cycle {} of {}\n' .format((i+1),cycles))
            except TimeoutError as e:
                print('*'*50)
                print(f"HAD A TIMEOUT on loop {i+1}")
                print(f"Exception: {e}")
                print('*'*50)
                yield from bps.checkpoint()
                yield from bps.sleep(30)
                yield from bps.unstage(rixscam)
                fails.append((j, time.ctime()))
                continue

    #except KeyboardInterrupt:
        #print('\n\n..........User interuptted rixs_one_energy()...........\n\n')
        #yield from rixs_cleanup(sclr_set_time)
        #return fails
        #raise

    except Exception:
        print('\n\nOOPS!  Possibly you stopped rixs_one_energy()')
        yield from rixs_cleanup(1)
        #return fails
        raise
    
    # print('\n\n..........rixs_one_energy() finished normally...........\n\n')#this prints regardless of quiting during scan or letting it finish
    # yield from rixs_cleanup(sclr_set_time)    

    return fails



