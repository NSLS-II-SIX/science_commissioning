def Hematite_film_dinner():
    ext_vg = 15
    total_time = 600
    cyc = 6
    yield from pol_H(0)
    yield from sleep(10)
    E = list(np.arange(707.5,707.6,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th43')


def KMO_highRes_final():

    ext_vg = 15
    total_time = 600
    cyc = 18
    yield from pol_V(-2)
    yield from sleep(10)
    E = list(np.arange(529.4,529.5,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th43')

    yield from mv(cryo.x, 19.880)
    yield from mv(cryo.y, 55.1)
    yield from mv(cryo.z, 13.345)
    yield from mv(cryo.t, 20)
    yield from sleep(5)
    yield from mv(cryo.t, 25)
    yield from sleep(5)
    ext_vg = 15
    total_time = 600
    cyc = 18
    yield from pol_V(-2)
    yield from sleep(10)
    E = list(np.arange(529.4,529.5,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th43')


def KMO_highRes_temp220K():

    ext_vg = 15
    total_time = 600
    cyc = 18
	# th = 10, tth = 90
    yield from pol_V(-2)
    yield from sleep(10)
    E = list(np.arange(529.4,529.5,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')



def KMO_highRes_th_43():

    ext_vg = 15
    total_time = 600
    cyc = 18
	# th = 10, tth = 90
    yield from pol_V(-2)
    yield from sleep(10)
    E = list(np.arange(529.5,529.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th43')

def KMO_highRes_20191102():

    ext_vg = 15
    total_time = 600
    cyc = 18
	# th = 10, tth = 90
    yield from pol_V(-2)
    yield from sleep(10)
    E = list(np.arange(529.5,529.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')
    cyc = 18
    yield from pol_H(-3)
    yield from sleep(10)
    E = list(np.arange(529.5,529.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')

    yield from pol_V(-2)
    cyc = 12
    yield from sleep(10)
    E = list(np.arange(529.5,529.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')

def KMO_th_dep_20191031():

    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 10, tth = 90
    yield from pol_V(-2)
    E = list(np.arange(530.6,530.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')
    cyc = 12
    yield from pol_H(-3)
    E = list(np.arange(530.6,530.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')

    yield from mv(cryo.x, 19.03)
    yield from mv(cryo.y, 52.5)
    yield from mv(cryo.z, 16.1)
    yield from mv(cryo.t, 45)
    yield from sleep(10)
    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_V(-2)
    E = list(np.arange(530.6,530.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th45')
    cyc = 9    
    yield from pol_H(-3)
    E = list(np.arange(530.6,530.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th45')

    yield from mv(cryo.x, 19.625)
    yield from mv(cryo.y, 52.5)
    yield from mv(cryo.z, 15.15)
    yield from mv(cryo.t, 25)
    yield from sleep(10)
    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 25, tth = 90
    yield from pol_V(-2)
    E = list(np.arange(530.6,530.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th25')
    cyc = 9
    yield from pol_H(-3)
    E = list(np.arange(530.6,530.8,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th25')






def test_stability_20191022():
    ext_vg = 11
    total_time = 2
    cyc = 1000
    en = 931.6
    sec_x_pt = 0.1
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')


def offset_gr1800_rixscam():
    ######################### Grating 1800l/mm  ##################################
    det_list=[rixscam]
    #yield from beamline_align_v2()
    yield from sleep(120)
    cff_ideal_1800 = 4.40
    yield from mv(pgm.cff, cff_ideal_1800)
    yield from mv(extslt.vg,7)
    offset=0
    yield from mv(pgm.en,931.6)
    yield from sleep(10)

    yield from count(det_list, num = 24)
    for i in range(0, 6):
        yield from mv(pgm.cff,cff_ideal_1800+i*0.02) #fine
        yield from mv(pgm.en,931.6)
        yield from sleep(30)
        yield from count(det_list, num = 24)
        print('Cff = {}' .format((cff_ideal_1800+i*0.02)))
    yield from mv(pgm.cff,cff_ideal_1800)

from epics import caget 
foe_P_in = EpicsSignalRO('XF:02IDA-OP{DI:2}P:Supply-I',name='foe_P_in')
m2_P_in = EpicsSignalRO('XF:02IDB-OP{Mir:2-WPG:1}DI-I',name='m2_P_in')
foe_P_out = EpicsSignalRO('XF:02IDA-OP{DI:2}P:Return-I',name='foe_P_out') 
tiltmeter_2_x = EpicsSignalRO('XF:02IDD-ES{DAA:1-TiltM:2}Axis:X-I',name='tiltmeter_2_x')
tiltmeter_2_y = EpicsSignalRO('XF:02IDD-ES{DAA:1-TiltM:2}Axis:Y-I',name='tiltmeter_2_y')

def test_stability_20191018():
    dets = [rixscam,m6.pit,espgm.m7pit, espgm.grpit, foe_P_in, m2_P_in, foe_P_out,tiltmeter_2_x,tiltmeter_2_y]
    for i in range(0,200):
        yield from count(dets, num = 24)
        print(i)


def hBN_th38_thinFlake():
    ext_vg = 40
    total_time = 600
    cyc = 29
	# th = 15, tth = 90
    yield from pol_V()
    E = [405.7]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')

def hBN_th15_406_highRes_firstFlake_at_SIX_bis():
    ext_vg = 11
    total_time = 600
    cyc = 8
	# th = 15, tth = 90
    yield from pol_V()
    E = [406]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')

def hBN_th15_406_highRes_firstFlake_at_SIX():
    ext_vg = 11
    total_time = 600
    cyc = 6
	# th = 15, tth = 90
    yield from pol_V()
    E = [406]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')


def hBN_th38_406_highRes_firstFlake_at_SIX():
    ext_vg = 11
    total_time = 600
    cyc = 18
	# th = 15, tth = 90
    yield from pol_V()
    E = [406]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')


def hBN_th15_406_highRes():
    ext_vg = 11
    total_time = 600
    cyc = 24
	# th = 15, tth = 90
    yield from pol_V()
    E = [406]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')

    ext_vg = 11
    total_time = 600
    cyc = 24
	# th = 15, tth = 90
    yield from pol_H()
    E = [406]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')
    print('Now flakes!! May the scattering Gods be with you!!')

def hBN_th15_407():
    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_V()
    E = [407]#,407,408,409,410]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')
        print(i)

def hBN_th15_406():
    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_V()
    E = [406.0]#,407,408,409,410]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')
        print(i)

def hBN_th15_405():
    ext_vg = 20
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_V()
    E = [406]#,407,408,409,410]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')
        print(i)

def hBN_th15_Emap():
    ext_vg = 20
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_V()
    E = [405]#,407,408,409,410]
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')
        print(i)


def hBN_th20_401():
    ext_vg = 20
    total_time = 600
    cyc = 6
	# th = 15, tth = 90
    yield from pol_V()
    E = list(np.arange(401,401.4,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')


def RuO2_last_macro():

    ext_vg = 11
    total_time = 600
    cyc = 15
	# th = 15, tth = 90
    yield from pol_H()
    E = list(np.arange(529.6,529.7,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th10')


    yield from mv(cryo.x, 25.979)
    yield from mv(cryo.y, 18.8)
    yield from mv(cryo.z, 14.97)
    yield from mv(cryo.t, 35)
    yield from sleep(10)
    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_H()
    E = list(np.arange(529.6,529.7,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th 35')

    yield from mv(cryo.x, 25.793)
    yield from mv(cryo.y, 18.8)
    yield from mv(cryo.z, 14.83)
    yield from mv(cryo.t, 42.5)
    yield from sleep(10)
    ext_vg = 11
    total_time = 600
    cyc = 12
	# th = 15, tth = 90
    yield from pol_H()
    E = list(np.arange(529.6,529.7,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'th 35')



def RuO2_highstat_highres():
    ext_vg = 11
    total_time = 600
    cyc = 18
	# th = 15, tth = 90
    yield from pol_H()
    E = list(np.arange(529.6,529.7,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'HighStatAndRes')


def KMO_emapOxy_3():
    ext_vg = 11
    total_time = 600
    E = list(np.arange(530.0,530.1,0.5))
    yield from pol_H()
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,6,i,ext_vg, 'E_map')
    yield from pol_V()
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,6,i,ext_vg, 'E_map')

def KMO_emapOxy_2():
    ext_vg = 20
    total_time = 600
    cyc = 1
    yield from pol_H()
    E = list(np.arange(532.0,533.05,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    E = list(np.arange(530.5,530.6,0.5))
    ext_vg = 11
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,6,i,ext_vg, 'E_map')

def KMO_emapOxy():
    ext_vg = 20
    total_time = 600
    cyc = 1
    yield from pol_H()
    E = list(np.arange(529.9,534.05,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    E = list(np.arange(530.5,530.6,0.5))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,6,i,ext_vg, 'E_map')


def RuO2_highstat_medres():
    ext_vg = 11
    total_time = 600
    cyc = 3
	# th = 15, tth = 90
    yield from pol_H()
    E = list(np.arange(529.6,529.7,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

def RuO2_emapOxy():
    ext_vg = 20
    total_time = 600
    cyc = 1
    yield from pol_H()
    E = list(np.arange(529.0,533.1,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_V()
    E = list(np.arange(529.0,533.1,0.1))
    for i in E:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')



def wednesday_am_v3():
    ext_vg = 100
    total_time = 900
    cyc = 4
    yield from pol_H()
    E = list(np.arange(463.0,465.5,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')


def wednesday_lull_v2():
    ext_vg = 20
    total_time = 900
    cyc = 16
    sec_x_pt = 5

    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map'
    yield from pol_H()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,462.0,ext_vg, 'E_map')
    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,462.0,ext_vg, 'E_map')
    # we can stop here
    yield from pol_H()
    yield from rixs_one_energy_1(sec_x_pt,total_time,2,462.0,ext_vg, 'E_map')
    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,2,462.0,ext_vg, 'E_map')
    yield from pol_H()
    yield from rixs_one_energy_1(sec_x_pt,total_time,2,462.0,ext_vg, 'E_map')
    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,2,462.0,ext_vg, 'E_map')

def wednesday_lull():
    ext_vg = 100
    total_time = 900
    cyc = 5
    E = list(np.arange(461.0,466.5,0.5))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

    ext_vg = 20
    total_time = 900
    cyc = 16
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map'
    yield from pol_H()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,462.0,ext_vg, 'E_map')
    yield from pol_V()
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,462.0,ext_vg, 'E_map')

def lunch_201901001():
    ext_vg = 20
    total_time = 900
    cyc = 16
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,462.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

def night_20190930():
    ext_vg = 20
    total_time = 900
    cyc = 8
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(461,466.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')

def xas_ruO2():
    yield from pol_H()
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)

def xas_ruO2_rixs():
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)#77216
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from pol_H()
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)
    yield from xas([sclr,rixscam,ring_curr],pgm.en,460,465,51,5)

    ext_vg = 20
    total_time = 900
    cyc = 8
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(462,462.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')




def energy_map_bulk_CRO():
    ext_vg = 20
    total_time = 600
    cyc = 12
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')
    yield from pol_H()
    E = list(np.arange(461,464.5,1.0))
    for i in E:
        sec_x_pt = 5
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map')



def test_stability_20190930_v2():
    ext_vg = 11
    total_time = 10
    cyc = 60
    en = 462
    sec_x_pt = 1
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')

def test_stability_20190930():
    ext_vg = 11
    total_time = 1
    cyc = 60
    en = 462
    sec_x_pt = 1
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')

def high_res_SCO_tth130_v3():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th48_tth130')

    yield from mv(cryo.x, 25.852)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.88)
    yield from mv(cryo.t, 53)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th53_tth130')

    yield from mv(cryo.x, 25.67)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.70)
    yield from mv(cryo.t, 58)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th58_tth130')

    yield from mv(cryo.x, 25.48)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.60)
    yield from mv(cryo.t, 63)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th63_tth130')

    yield from mv(cryo.x, 25.383)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.57)
    yield from mv(cryo.t, 68)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 9
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th68_tth130')




def high_res_SCO_tth130_v2():

    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 2
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th43_tth130')

    yield from mv(cryo.x, 25.863)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 16.070)
    yield from mv(cryo.t, 48)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th48_tth130')

def high_res_SCO_tth130():
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th33_tth130')

    yield from mv(cryo.x, 26.006)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 16.24)
    yield from mv(cryo.t, 38)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th38_tth130')

    yield from mv(cryo.x, 25.873)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 15.97)
    yield from mv(cryo.t, 43)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th43_tth130')

    yield from mv(cryo.x, 25.863)
    yield from mv(cryo.y, 60.782)
    yield from mv(cryo.z, 16.070)
    yield from mv(cryo.t, 48)
    yield from sleep(30)
    ext_vg = 11
    total_time = 600
    cyc = 6
    en = 931.9
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'SCO_th48_tth130')


def test_stability():
    ext_vg = 11
    total_time = 60
    cyc = 200
    en = 460
    sec_x_pt = 1
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')


def high_res_Fe_54uc_tth150_th75():
    ext_vg = 15
    total_time = 600
    cyc = 6
    en = 707.8
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc_tth150_th75')


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




