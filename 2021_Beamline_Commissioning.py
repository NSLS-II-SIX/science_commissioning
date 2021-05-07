def test_stability_20210126():
    ext_vg = 11
    total_time = 300
    cyc = 200
    en = 710
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')



from epics import caget
foe_P_in = EpicsSignalRO('XF:02IDA-OP{DI:2}P:Supply-I',name='foe_P_in')
m2_P_in = EpicsSignalRO('XF:02IDB-OP{Mir:2-WPG:1}DI-I',name='m2_P_in')
foe_P_out = EpicsSignalRO('XF:02IDA-OP{DI:2}P:Return-I',name='foe_P_out')
foe_air_temp = EpicsSignalRO('XF:02ID-OP{TCtrl:1-Chan:D}T-I',name='foe_air_temp')
pgm_air_temp = EpicsSignalRO('XF:02ID-OP{TCtrl:1-Chan:D5}T-I',name='pgm_air_temp')

def test_zero_order_20210127():
    for i in range(0,10): 
        #yield from count([m2_P_in,m3_diag_cam],num=50)




