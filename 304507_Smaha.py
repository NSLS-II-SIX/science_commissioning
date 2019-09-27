def RIXS_qMap():
    ext_vg = 8
    total_time = 600
    split_time = 5
    E_peak = 931.0

    yield from pol_V(4.05)
    #yield from pol_H(2.4)

    num_cycles = 2
    #Barlowite
    #theta = [77, 110, 125, 140]
    #samx = [ 24.88, 26.40, 26.90, 27.37]
    #samz = [ 18.80, 18.48,18.10,17.74]

    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 110 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 110 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 110 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 110 deg')

    #Zn substituted
    theta = [125, 137]
    samx = [26.9, 27.25]
    samz = [18.04, 17.69]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from mvr(cryo.y,0.005)
        yield from sleep(1)
        #print('#'*77)
        #print('#'*110)
        print('#'*125)
        print('#'*137)
        print('th = {} deg' .format(theta[i]))
        #print('#'*77)
        #print('#'*110)
        print('#'*125)
        print('#'*137)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from sleep(1)

    yield from pol_H(2.4)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))

def RIXS_qMap2():
    ext_vg = 8
    total_time = 600
    split_time = 5
    E_peak = 931.0

    #yield from pol_V(4.05)
    #yield from pol_H(2.4)

    i = 1
    num_cycles = 2
    theta = [77, 77]
    print('#'*77)
    print('th = {} deg' .format(theta[i]))
    print('#'*77)

    
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))



def RIXS_qMap3():
    ext_vg = 8
    total_time = 600
    split_time = 5
    E_peak = 931.0

    num_cycles = 2
    
    #Barlowite
    yield from mv(cryo.y,20.64)
    theta = [80]
    samx = [25]
    samz = [18.55]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)

    yield from pol_H(2.4)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')

    yield from pol_V(4.05)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 80 deg')

    theta = [47]
    samx = [23.5]
    samz = [17.98]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)

    yield from pol_H(2.4)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')

    yield from pol_V(4.05)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')


    #Zinc-substituted barlowite
    yield from mv(cryo.y,14)
    theta = [47]
    samx = [23.7]
    samz = [17.9]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)

    yield from pol_H(2.4)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')

    yield from pol_V(4.05)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 47 deg')

    theta = [77]
    samx = [24.95]
    samz = [18.37]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)

    yield from pol_H(2.4)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')

    yield from pol_V(4.05)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
    yield from mvr(cryo.y,0.005)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 77 deg')
   

def RIXS_qMap4():
    ext_vg = 8
    total_time = 600
    split_time = 5
    E_peak = 931.0
    num_cycles = 2
    yield from pol_H(2.4)    

    #Barlowite
    yield from mv(cryo.y,20.64)
    theta = [65]
    samx = [24.4]
    samz = [18.48]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)

        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 65 deg')
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 65 deg')
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 65 deg')
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 65 deg')
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = 65 deg')

    #Zinc-substituted barlowite
    yield from mv(cryo.y,14)
    theta = [47, 65, 77]
    samx = [23.7, 24.45, 24.95]
    samz = [17.9, 18.30, 18.37]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        
        print('#'*47)
        print('#'*65)
        print('#'*77)
        print('th = {} deg' .format(theta[i]))
        print('#'*47)
        print('#'*65)
        print('#'*77)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from mvr(cryo.y,0.005)
        yield from sleep(1)






def RIXS_EMap():
    ext_vg = 11
    
    #yield from mvr(cryo.y,0.01)
    #yield from rixs_one_energy(1,600,3,931,ext_vg)
    yield from mv(cryo.y,14)
    yield from rixs_one_energy(2,600,1,930,ext_vg)
    yield from mv(cryo.y,13.98)
    yield from rixs_one_energy(1,600,1,930.5,ext_vg)
    yield from mv(cryo.y,13.96)
    yield from rixs_one_energy(1,600,1,931,ext_vg)
    yield from mv(cryo.y,13.94)
    yield from rixs_one_energy(1,600,1,931.5,ext_vg)
    yield from mv(cryo.y,13.92)
    yield from rixs_one_energy(2,600,1,932,ext_vg)
    
    yield from pol_H(2.4)
    yield from mv(cryo.y,13.96)
    yield from rixs_one_energy(1,600,1,931,ext_vg)
    

def RIXS_single_spectrum():
    ext_vg = 11
    total_time = 600
    split_time = 3
    E_peak = 931.0

    #yield from pol_V(4)

    num_cycles = 10
      
    #E_peak = yield from xas([sclr],pgm.en,931.5,933,31)
    yield from sleep(1)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
    yield from sleep(1)

def firstevening():
	yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
