
# yield from pol_V(-2)
# yield from pol_H(-3)


def xas_rixscam(exp_time=2, repeats=1):
    Emaxs = []
    rixscam.xip.count_event_3x3.kind = Kind.hinted  # plot the rixscam live
    yield from pzshutter_enable()

    yield from mv(rixscam.cam.acquire_time, exp_time)  
    yield from mv(sclr.preset_time, exp_time)
    yield from mv(extslt.vg,30, extslt.hg, 150)
    for i in range(0,repeats):
        yield from mv(pgm.en, 850)
        yield from mv(gvbt1,'open')
        yield from sleep(2)
        yield from scan([rixscam,sclr,ring_curr], pgm.en,850,862,121) # for detuning
        #Emaxs.append(peaks['max']['rixscam_xip_count_event_3x3'][0])     # comment out for print_summary

    yield from mv(rixscam.cam.acquire_time, 1)  
    yield from mv(sclr.preset_time, 1)
    rixscam.xip.count_event_3x3.kind = Kind.normal  # plot the rixscam live
    #yield from mv(extslt.vg,15)
    #print('Emaxs:\t',Emaxs,'\t----> avg:\t',np.mean(Emaxs))
    #return np.mean(Emaxs)


def energy_map_ncnf_s3():
    ext_vg = 11
    total_time = 300
    cyc = 1
    
    yield from pol_H(-3)

    #E = list(np.arange(850.5,852.05,0.1))
    #for i in E:
    #    sec_x_pt = 3
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_ncnf_s3')

    #E = list(np.arange(852.1,852.85,0.1))
    #for i in E:
    #    sec_x_pt = 2
    #    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_ncnf_s3')

    #E = list(np.arange(852.9,856.55,0.1))
    E = list(np.arange(854.5,856.55,0.1))
    for i in E:
        sec_x_pt = 1
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_ncnf_s3')

    E = list(np.arange(856.6,857.35,0.1))
    for i in E:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_ncnf_s3')

    E = list(np.arange(857.4,858.55,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_ncnf_s3')


def energy_map_nps():
    ext_vg = 11
    total_time = 300
    cyc = 1
    
    yield from pol_H(-3)

    E = list(np.arange(850,852.1,0.2))
    for i in E:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nps')

    E = list(np.arange(852.2,853.1,0.2))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nps')

    E = list(np.arange(853.2,855.7,0.2))
    for i in E:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nps')

    E = list(np.arange(855.8,861.1,0.2))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nps')


def energy_map_nio():
    ext_vg = 11
    total_time = 300
    cyc = 1
    
    yield from pol_H(-3)

    E = list(np.arange(850,852.85,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

    E = list(np.arange(852.9,854.45,0.1))
    for i in E:
        sec_x_pt = 2
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

    E = list(np.arange(854.5,857.35,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

    E = list(np.arange(857.4,862.05,0.1))
    for i in E:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

def energy_map_nio_PD():
    ext_vg = 11
    total_time = 300
    cyc = 1
    
    yield from pol_H(-3)

    E = list(np.arange(854.7,857.35,0.1))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

    E = list(np.arange(857.4,862.05,0.1))
    for i in E:
        sec_x_pt = 4
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

def energy_map_NCNF_L2_S4():
    ext_vg = 11
    total_time = 300
    cyc = 1
    
    yield from pol_H(-3)

    E = list(np.arange(870.2,873.3,0.2))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_nio')

def energy_map_NCNF_K_F():
    ext_vg = 11
    total_time = 6
    cyc = 1
    
    yield from pol_H(-3)

    E = list(np.arange(686.9,686.94,0.2))
    for i in E:
        sec_x_pt = 3
        yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map_ncncf_k_f')

def eshift_test():

	while True:
		yield from xas([sclr,ring_curr], pgm.en, 848,860,120, 0.2)
		time.sleep(60)
	

