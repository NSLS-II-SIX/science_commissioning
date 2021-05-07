def restart():
	yield from sleep(3600)
	yield from mv(extslt.vg,20)
	yield from rixscam_pgm_en_centroid(120)
	yield from mv(pgm.en,853)
	yield from sleep(3600)
	ext_vg = 11
	total_time = 300
	cyc=3
	en = 853
	sec_x_pt = 1
	yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')
	ext_vg = 15
	total_time = 300
	cyc=3
	en = 853
	sec_x_pt = 1
	yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')
	ext_vg = 20
	total_time = 300
	cyc=3
	en = 853
	sec_x_pt = 1
	yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')
	yield from sleep(3600)
	ext_vg = 11
	total_time = 300
	cyc=3
	en = 853
	sec_x_pt = 1
	yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')
	ext_vg = 15
	total_time = 300
	cyc=3
	en = 853
	sec_x_pt = 1
	yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')
	ext_vg = 20
	total_time = 300
	cyc=3
	en = 853
	sec_x_pt = 1
	yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'test')




