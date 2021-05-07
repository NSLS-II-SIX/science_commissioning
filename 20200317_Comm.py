

def YIG_20201127():
    # YIG -- xstal
    ext_vg = 12
    total_time = 600
	##########################################################################################
    energy_d = 710.73
    sec_x_pt = 5
    cyc = 9 #30  
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

    energy_d = 710.13
    sec_x_pt = 5
    cyc = 9 #30   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

    energy_d = 709
    sec_x_pt = 5
    cyc = 12 #30   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)









def Bi2212_20201109():
    sclr_disable()
    ext_vg = 20 #25
    energy=528.5
    sec_x_pt = 4
    total_time = 600
    cyc = 3
    
	##########################################################################################

    # yield from pol_V(-2.9)
    # yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)


    yield from pol_H(-3.5)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy,ext_vg)

    yield from pol_V(-2.9)
    yield from sleep(30)




def Fe2O3_20201024():
    # YIG -- xstal
    ext_vg = 12.5
    total_time = 300
    cyc = 7 #30   

	##########################################################################################
    energy_d = 710.4
    sec_x_pt = 3
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

	##########################################################################################



def Fe2O3_map_20201025():
    sclr_disable()
    ext_vg = 20 #25
    total_time = 600
    cyc = 1 
    
	##########################################################################################
    E2 = np.arange(713.8,714.45,0.3)
    sec_x_pt = 3
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')
    yield from sleep(30)

def Fe2O3_map_20201024():
    sclr_disable()
    ext_vg = 20 #25
    total_time = 600
    cyc = 1 
    
	##########################################################################################
    yield from pol_V(-4.2)
    yield from sleep(2)
    E0 = np.arange(707.8,709.65,0.2)
    sec_x_pt = 3
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E1 = np.arange(709.8,712.05,0.2)
    sec_x_pt = 2
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E2 = np.arange(712.3,714.45,0.3)
    sec_x_pt = 3
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')
    yield from sleep(30)




def Fe2O3_map_20201023():
    sclr_disable()
    ext_vg = 20 #25
    total_time = 600
    cyc = 1 
    
	##########################################################################################

    yield from pol_H(-4.2)
    yield from sleep(30)

    E0 = np.arange(707.8,709.65,0.2)
    sec_x_pt = 3
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E1 = np.arange(709.8,712.05,0.2)
    sec_x_pt = 2
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E2 = np.arange(712.3,714.45,0.3)
    sec_x_pt = 3
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')
    yield from sleep(30)
    ##########################################################################################
    yield from pol_V(-4.2)
    yield from sleep(30)
    E0 = np.arange(707.8,709.65,0.2)
    sec_x_pt = 3
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E1 = np.arange(709.8,712.05,0.2)
    sec_x_pt = 2
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E2 = np.arange(712.3,714.45,0.3)
    sec_x_pt = 3
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')
    yield from sleep(30)




def FeAs_20200911():
    # YIG -- xstal
    ext_vg = 15
    total_time = 600
    cyc = 12 #30   

	##########################################################################################
    energy_d = 708.4
    sec_x_pt =4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)




def YIG_20200910():
    # YIG -- xstal
    ext_vg = 11
    total_time = 600
    cyc = 6 #30   

	##########################################################################################
    energy_d = 710
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

    energy_d = 708.88
    sec_x_pt = 5
    cyc = 12
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

    energy_d = 708.27
    sec_x_pt = 5
    cyc = 12
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)









def BFO_20200910():
    # YIG -- xstal
    ext_vg = 11
    total_time = 600
    cyc = 9 #30   

	##########################################################################################
    energy_d = 710
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)





def Fe2O3_20200909():
    # YIG -- xstal
    ext_vg = 11
    total_time = 300
    cyc = 12 #30   

	##########################################################################################
    energy_d = 708.8
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

	##########################################################################################
    energy_d = 709.68
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)

	##########################################################################################
    energy_d = 710.2
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)



def Fe2O3_map_20200909():
    sclr_disable()
    ext_vg = 20 #25
    total_time = 600
    cyc = 1 
    
    # yield from pol_H(-4.0)

    E0 = np.arange(707.8,709.65,0.2)
    sec_x_pt = 4
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E1 = np.arange(709.8,712.05,0.2)
    sec_x_pt = 2
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')

    E2 = np.arange(712.3,714.45,0.3)
    sec_x_pt = 4
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'F2O3')




def Fe_20200907_re():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 15
    sec_x_pt = 5
    total_time = 600
    cyc = 2 #12
    E = 708.2   

    ############## Linear ###############
    # yield from pol_H(-4.0)
    #####################################

    ############## Circular + #############
    #yield from mv(m1_pid_fbk,'OFF')
    #yield from mv(m3_pid_fbk,'OFF')
    
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.4992)
    yield from mv(pgm.en,E)
    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'ON')
    #yield from mv(m3_pid_fbk,'ON')


    ######################################

    ############## Keithley ON ##############
    # yield from mv(voltage_dc,-15)
    # yield from mv(keithley_output,'ON')
    yield from sleep(10)
    #######################################

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,E,ext_vg, 'Fe film')
 
    ############## Keithley OFF ##############  
    # yield from mv(voltage_dc,0)
    # yield from mv(keithley_output,'OFF')
    #######################################




def BFO_20200907_re():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 11
    sec_x_pt = 3
    total_time = 600
    cyc = 2
    E = 710.1
    # E = 708.75    

    # yield from pol_H(-4.0)

    yield from rixs_en_map(sec_x_pt,total_time,cyc,E,ext_vg, 'BFO crystal')
	##########################################################################################
    # yield from pol_V(-4.0)
    # yield from sleep(30) 
    # yield from rixs_en_map(sec_x_pt,total_time,cyc,E,ext_vg, 'BFO crystal')



def BFO_20200907():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 20
    total_time = 600
    cyc = 1 
    
    # yield from pol_H(-4.0)

    E2 = np.arange(712.2,714.05,0.3)
    sec_x_pt = 5
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

	##########################################################################################
    yield from pol_V(-4.0)
    yield from sleep(30)
    yield from beamline_align_v3()
    yield from sleep(5)


    E0 = np.arange(708,709.7,0.2)
    sec_x_pt = 5
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

    E1 = np.arange(709.8,711.05,0.2)
    sec_x_pt = 3
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

    E2 = np.arange(711.3,714.05,0.3)
    sec_x_pt = 5
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')






def BFO_20200906():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 20
    total_time = 600
    cyc = 1 
    
    # yield from pol_H(-4.0)

    E0 = np.arange(708,709.7,0.2)
    sec_x_pt = 5
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

    E1 = np.arange(709.8,711.05,0.2)
    sec_x_pt = 3
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

    E2 = np.arange(711.3,714.05,0.3)
    sec_x_pt = 5
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

	##########################################################################################
    yield from pol_V(-4.0)
    yield from sleep(30)
    yield from beamline_align_v3()
    yield from sleep(5)


    E0 = np.arange(708,709.7,0.2)
    sec_x_pt = 5
    for i in E0:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

    E1 = np.arange(709.8,711.05,0.2)
    sec_x_pt = 3
    for i in E1:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')

    E2 = np.arange(711.3,714.05,0.3)
    sec_x_pt = 5
    for i in E2:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'BFO crystal')












def LSCO_20200819():
    # YIG -- xstal
    ext_vg = 20
    sec_x_pt = 5
    total_time = 600
    cyc = 6 #30   

	##########################################################################################
    energy_d = 528.95


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)



def LSCO_20200820():
    # YIG -- xstal
    ext_vg = 13
    sec_x_pt = 5
    total_time = 600
    cyc = 25    

	##########################################################################################
    energy_d = 528.95


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)
    yield from sleep(30)

	##########################################################################################
    energy_d = 530.45


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg)
    yield from sleep(30)


 
def Fe2O3_20200819_RIXSMCD_Edep_Current():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 2
    total_time = 600
    cyc = 4   
    #yield from mv(keithley_output,'OFF')
    #yield from mv(current_pulse,-0.009)
    #yield from mv(time_pulse,0.001)
    #yield from mv(interval_pulse,8) #30sec

	##########################################################################################
    energy_d = 708.6

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.506)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')


    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.566)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    yield from sleep(30)
    ##########################################################################################
    energy_d = 709.68

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.589)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    yield from sleep(30)




    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.529)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)


    ##########################################################################################
    energy_d = 710.4


    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.543)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)


    # cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.603)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    yield from sleep(30)




    ##########################################################################################
    energy_d = 713.8

    # cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.675)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    yield from sleep(30)
   

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.615)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')
    yield from sleep(30)

    ##########################################################################################


def Fe2O3_20200818_RIXSMCD_Edep_Current():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 2
    total_time = 600
    cyc = 4       
    energy_d = 710.4
    yield from mv(keithley_output,'ON')

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.543)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)


    # cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.603)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    yield from sleep(30)

    yield from mv(keithley_output,'OFF')







def Fe2O3_20200817_RIXSMCD_Edep_Current():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    

    #yield from mv(keithley_output,'OFF')
    #yield from mv(current_pulse,-0.009)
    #yield from mv(time_pulse,0.001)
    #yield from mv(interval_pulse,8) #30sec
    yield from mv(keithley_output,'ON')
    ##########################################################################################

    energy_d = 709.68

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.589)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    yield from sleep(30)




    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.529)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)


    ##########################################################################################
    energy_d = 710.4


    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.543)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)


    # cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.603)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    yield from sleep(30)




    ##########################################################################################
    energy_d = 713.8

    # cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.675)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    yield from sleep(30)
   

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.615)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')
    yield from sleep(30)

    ##########################################################################################

    yield from mv(keithley_output,'OFF')
























def Fe2O3_20200816_RIXSMCD_Edep_Current2():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    

    #yield from mv(keithley_output,'OFF')
    #yield from mv(current_pulse,-0.009)
    #yield from mv(time_pulse,0.001)
    #yield from mv(interval_pulse,8) #30sec
    yield from mv(keithley_output,'ON')
    ##########################################################################################

    #energy_d = 709.68



    #yield from mv(m1_pid_fbk,'OFF')
    #yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    #yield from mv(epu1.phase,19.295)
    #yield from mv(epu1.gap,28.529)
    #yield from mv(pgm.en,energy_d)
    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'ON')
    #yield from mv(m3_pid_fbk,'ON')
   
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    #yield from sleep(30)

    #cyc = 6
    #yield from mv(m1_pid_fbk,'OFF')
    #yield from mv(m3_pid_fbk,'OFF')

    # C-
    #yield from mv(epu1.phase,-19.295)
    #yield from mv(epu1.gap,28.589)
    #yield from mv(pgm.en,energy_d)
    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'ON')
    #yield from mv(m3_pid_fbk,'ON')


    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    #yield from sleep(30)
    ##########################################################################################
    #energy_d = 710.4
    # cyc = 6
    #yield from mv(m1_pid_fbk,'OFF')
    #yield from mv(m3_pid_fbk,'OFF')

    # C-
    #yield from mv(epu1.phase,-19.295)
    #yield from mv(epu1.gap,28.603)
    #yield from mv(pgm.en,energy_d)
    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'ON')
    #yield from mv(m3_pid_fbk,'ON')


    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'OFF')
    #yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    #yield from mv(epu1.phase,19.295)
    #yield from mv(epu1.gap,28.543)
    #yield from mv(pgm.en,energy_d)
    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'ON')
    #yield from mv(m3_pid_fbk,'ON')
   
    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    #yield from sleep(30)



    ##########################################################################################
    energy_d = 713.8

    # cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.675)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')
    yield from sleep(30)
   

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.615)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')
    yield from sleep(30)

    ##########################################################################################

    yield from mv(keithley_output,'OFF')


def Fe2O3_20200816_RIXSMCD_Edep_Current():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 708.6

    #yield from mv(keithley_output,'OFF')
    #yield from mv(current_pulse,0.009)
    #yield from mv(time_pulse,0.001)
    #yield from mv(interval_pulse,8) #30sec
    yield from mv(keithley_output,'ON')

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.506)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')


    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.566)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    yield from mv(keithley_output,'OFF')

def Fe2O3_20200816_RIXSMCD_Edep():
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600

    cyc = 2    
    energy_d = 710.4



    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.543)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.603)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    ##############################################################################


def Fe2O3_20200816_pD_RIXSMCD_Edep():
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    #cyc = 6    
    energy_d = 713.8



    #yield from mv(m1_pid_fbk,'OFF')
    #yield from mv(m3_pid_fbk,'OFF')
    
    # C-
    #yield from mv(epu1.phase,-19.295)
    #yield from mv(epu1.gap,28.675)
    #yield from mv(pgm.en,energy_d)
    #yield from sleep(30)
    #yield from mv(m1_pid_fbk,'ON')
    #yield from mv(m3_pid_fbk,'ON')


    #yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    #yield from sleep(30)

    cyc = 5
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')


    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.615)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')



def Fe2O3_20200811_RIXSMCD():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 709.68



    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.529)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.589)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')



def Fe2O3_20200811_RIXSMCD_Edep():
    # YIG -- xstal
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 708.6



    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.506)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.566)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    ##############################################################################
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 710.4



    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.543)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.603)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')

    ##############################################################################
    ext_vg = 15
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 713.8



    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    

    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.615)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ Fe2O3')

    yield from sleep(30)

    #cyc = 6
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.675)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- Fe2O3')








def YIG_20200807():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 23
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(707.4, 712.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map YIG-crystal')
    sclr_enable()


def YIG_20200808():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 11
    sec_x_pt = 4
    total_time = 600
    cyc = 12 #12 #9
    E =  [708.78,708.17]#[709.9]# [710.5] #
    for i in E:
        #yield from mv(extslt.vg,100)
        #yield from xas([ring_curr,sclr],pgm.en,707,711,81,1)
        yield from sleep(5)   

        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'YIG crystal')




def YIG_20200809_XMCD_d():
    # YIG -- xstal
    ext_vg = 11
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 709.7

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.59)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')


    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- YIG-magnet')

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    cyc = 6
    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.53)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
   
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ YIG-magnet')


def YIG_20200809_XMCD_a2():
    # YIG -- xstal
    ext_vg = 11
    sec_x_pt = 4
    total_time = 600
    cyc = 9    
    energy_a2 = 710.56

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')

    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.607)
    yield from mv(pgm.en,energy_a2)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_a2,ext_vg, 'C- YIG-magnet')

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    
    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.547)
    yield from mv(pgm.en,energy_a2)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')

    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_a2,ext_vg, 'C+ YIG-magnet')



def YIG_20200808_XMCD_d():
    # YIG -- xstal
    ext_vg = 11
    sec_x_pt = 4
    total_time = 600
    cyc = 6    
    energy_d = 709.7

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.59)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C- YIG-magnet')

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.53)
    yield from mv(pgm.en,energy_d)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_d,ext_vg, 'C+ YIG-magnet')


def YIG_20200808_XMCD_a2():
    # YIG -- xstal
    ext_vg = 11
    sec_x_pt = 4
    total_time = 600
    cyc = 9    
    energy_a2 = 710.56

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    # C-
    yield from mv(epu1.phase,-19.295)
    yield from mv(epu1.gap,28.607)
    yield from mv(pgm.en,energy_a2)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_a2,ext_vg, 'C- YIG-magnet')

    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    # C+
    yield from mv(epu1.phase,19.295)
    yield from mv(epu1.gap,28.547)
    yield from mv(pgm.en,energy_a2)
    yield from sleep(30)
    yield from mv(m1_pid_fbk,'ON')
    yield from mv(m3_pid_fbk,'ON')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,energy_a2,ext_vg, 'C+ YIG-magnet')





def YIG_20200320_v3():
    # YIG -- xstal
    ext_vg = 25
    sec_x_pt = 3
    total_time = 900

    # C-
    yield from mv(epu1.phase,-19.3)
    yield from mv(epu1.gap,28.58)
    yield from mv(pgm.en,709.6)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,709.6,ext_vg, 'C+ YIG-magnet')
    yield from mv(epu1.gap,28.55)
    yield from mv(pgm.en,708.4)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,708.4,ext_vg, 'C+ YIG-magnet')

    # C+
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    yield from mv(epu1.phase,19.3)
    yield from mv(epu1.gap,28.5)
    yield from mv(pgm.en,709.6)
    yield from sleep(30)
    yield from beamline_align_v3()
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,709.6,ext_vg, 'C+ YIG-magnet')
    yield from mv(epu1.gap,28.48)
    yield from mv(pgm.en,708.4)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,708.4,ext_vg, 'C+ YIG-magnet')





def YIG_20200320_v2():
    # YIG -- xstal
    ext_vg = 25
    sec_x_pt = 3
    total_time = 900
    # C+
    yield from mv(epu1.phase,19.3)
    yield from mv(epu1.gap,28.5)
    yield from mv(pgm.en,709.6)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,709.6,ext_vg, 'C+ YIG-magnet')
    yield from mv(epu1.gap,28.48)
    yield from mv(pgm.en,708.4)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,708.4,ext_vg, 'C+ YIG-magnet')

    # C-
    yield from mv(m1_pid_fbk,'OFF')
    yield from mv(m3_pid_fbk,'OFF')
    yield from mv(epu1.phase,-19.3)
    yield from mv(epu1.gap,28.58)
    yield from mv(pgm.en,709.6)
    yield from sleep(30)
    yield from beamline_align_v3()
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,709.6,ext_vg, 'C+ YIG-magnet')
    yield from mv(epu1.gap,28.55)
    yield from mv(pgm.en,708.4)
    yield from sleep(30)
    yield from rixs_one_energy_1(sec_x_pt,total_time,1,708.4,ext_vg, 'C+ YIG-magnet')



def YIG_20200319():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 25
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(707.4, 712.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map YIG-GGG')


def YIG_20200318_v3():
    # YIG -- xstal
    sclr_disable()
    ext_vg = 25
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(707.4, 712.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map YIG-SGGG')

    # YIG -- NGG
    yield from mv(cryo.y, 58.0)
    yield from mv(cryo.x, 17.666)
    yield from mv(cryo.z, 17.15)

    ext_vg = 25
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(707.4, 712.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map YIG-SGGG')
    sclr_enable()

def YIG_20200318_v2():
    sclr_disable()
    ext_vg = 25
    sec_x_pt = 4
    total_time = 900
    E = list(np.arange(712.2, 713.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,1,i,ext_vg, 'E_map YIG-SGGG')
    sclr_enable()



def Fe_54uc_th76():
    ext_vg = 15
    total_time = 600
    cyc = 9
    en = 707.5
    #pol is H
    sec_x_pt = 5
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,en,ext_vg, 'Fe_54uc_tth150_th11')




def YIG_20200317():

    ext_vg = 11
    total_time = 600
    cyc = 12
    # Pol  Vertical
    #yield from pol_V(-2)
    sec_x_pt = 4
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,708.0,ext_vg, 'YIG / SGGG')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,708.5,ext_vg, 'YIG / SGGG')
    yield from rixs_one_energy_1(sec_x_pt,total_time,cyc,709.9,ext_vg, 'YIG / SGGG')

    sclr_disable()
    ext_vg = 25
    total_time = 900
    E = list(np.arange(707, 711.1, 0.2))
    for i in E:
        yield from sleep(5)   
        yield from rixs_en_map(sec_x_pt,total_time,cyc,i,ext_vg, 'E_map YIG-SGGG')
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
                yield from mvr(cryo.y, 0.002) # if you do not want to move comment out this line
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
