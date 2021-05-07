
def test_M3_pitch():
    m3_pit_start=-0.755829 
    m3_pit_step=0.00001 # smallest step ~ 0.000002 deg
    for jj in range(0,10):
        yield from mv(m3.pit, m3_pit_start+jj*m3_pit_step)
        yield from mv(extslt.vg,50)
        yield from mv(extslt.hg,5)
        yield from rel_scan([sclr],extslt.hc,-0.1,0.1,41)
        yield from mv(extslt.vg,11)
        yield from mv(extslt.hg,200)
        yield from rel_scan([sclr],cryo.y,0,0.03,91)


def test_stability_20200720():
    ext_vg = 11
    total_time = 180
    cyc = 180
    en = 707
    sec_x_pt = 3
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')
    yield from mv(extslt.hg,150)


def test_ccd_noise():
    
    yield from mv(rixscam.cam.acquire_time, 1)  
    yield from count([rixscam],num=600)
    yield from mv(rixscam.cam.acquire_time, 2)  
    yield from count([rixscam], num=300)
    yield from mv(rixscam.cam.acquire_time, 3)  
    yield from count([rixscam], num = 200)
    yield from mv(rixscam.cam.acquire_time, 4)  
    yield from count([rixscam], num = 150)
    yield from mv(rixscam.cam.acquire_time, 5)  
    yield from count([rixscam], num = 120)
    
    yield from mv(rixscam.cam.acquire_time, 1)  
    yield from count([rixscam],num= 600)
    yield from count([rixscam], num= 300)
    yield from count([rixscam], num = 200)
    yield from count([rixscam], num = 150)
    yield from count([rixscam], num = 120)


from epics import caget
foe_P_in = EpicsSignalRO('XF:02IDA-OP{DI:2}P:Supply-I',name='foe_P_in')
m2_P_in = EpicsSignalRO('XF:02IDB-OP{Mir:2-WPG:1}DI-I',name='m2_P_in')
foe_P_out = EpicsSignalRO('XF:02IDA-OP{DI:2}P:Return-I',name='foe_P_out')
foe_air_temp = EpicsSignalRO('XF:02ID-OP{TCtrl:1-Chan:D}T-I',name='foe_air_temp')
pgm_air_temp = EpicsSignalRO('XF:02ID-OP{TCtrl:1-Chan:D5}T-I',name='pgm_air_temp')

#RE(count([foe_P_in,foe_P_out,m2_P_in,sclr,ring_curr],num=300,delay=1))

def test_stability_20200721():
    dets = [sclr,ring_curr,m1.pit,m3.pit,pgm.grpit,foe_P_in,m2_P_in,foe_P_out]
    for i in range(0,10):
        yield from count(dets, num = 20)
        print(i)

def test_M3_pitch_20200721():
    dets = [sclr,ring_curr,m1.pit,m3.pit]
    m3_pit_start=-0.755991-0.000002*20
    m3_pit_step=0.000002 # smallest step ~ 0.000002 deg
    for jj in range(0,40):
        yield from mv(m3.pit, m3_pit_start+jj*m3_pit_step)
        yield from count(dets, num = 120)

def test_M3_pitch_20200721_2():
    dets = [sclr,ring_curr,m1.pit,m3.pit]
    yield from rel_scan(dets,m3.pit,-0.0002,+0.0002,101)
    #yield from rel_scan(dets,m3.pit,-0.002,+0.002,101)
    #yield from rel_scan(dets,m3.pit,+0.002,-0.002,101)

    #yield from xas(dets,pgm.en,865,873,800,1)

def test_M3_pitch_20200722():
    dets = [sclr,ring_curr,m1.pit,m3.pit]
    m3_pit_start=-0.756040-0.0004
    m3_pit_step=0.0004*2/30
    for jj in range(0,31):
        yield from mv(m3.pit, m3_pit_start+jj*m3_pit_step)
        yield from xas(dets,pgm.en,867,869.5,201,1)

def test_M3_pitch_20200722_2():
    dets = [sclr,ring_curr,m1.pit,m3.pit]
    #M1_feedback ON
    #M3_feedback ON
    for jj in range(0,200):
        yield from xas(dets,pgm.en,867,869.5,201,1)

def test_M3_pitch_20200728():
    dets = [sclr,ring_curr,m1.pit,m3.pit]
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    for jj in range(0,400):
        yield from xas(dets,pgm.en,866.3,869.2,201,1)
        yield from sleep(30)

def test_M3_pitch_20200727_1():
    dets = [sclr,ring_curr,m1.pit,m3.pit]
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'OFF')
    yield from mv(extslt.hg,500)    
    for jj in range(0,200):
        yield from xas(dets,pgm.en,867,869.5,201,1)
        yield from sleep(30)

def test_zero_order_20200801():
    for i in range(0,16): 
        yield from count([ring_curr,m1.pit,m3.pit,pgm.m2pit,pgm.grpit,m3_diag_cam],num=500, delay=10)


def test_zero_order_20200802():
    for i in range(0,6): 
        yield from count([ring_curr,m1.pit,m3.pit,pgm.m2pit,pgm.grpit,m3_diag_cam],num=1000)  

def test_zero_order_20201026():
    for i in range(0,21): 
        yield from count([m2_P_in,m3_diag_cam],num=4000)
        yield from sleep(300)

def test_zero_order_20201029():
    for i in range(0,4): 
        yield from count([m2_P_in,gc_diag_cam],num=4000)

def test_zero_order_long_20201026():
    for i in range(0,4): 
        yield from count([m2_P_in,foe_air_temp, pgm_air_temp,m3_diag_cam],num=2000, delay=10)



def testccd_20201027():
    for i in range(0,240): 
        yield from count([rixscam],num=120) 
        yield from sleep(60)




