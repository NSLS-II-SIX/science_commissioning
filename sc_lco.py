def FeP_FeAs_last_night():
# FeAs [010]
    ext_vg = 11
    E_peak = 708
    num_cycles = 13
    yield from sleep(3)
    theta = [10]
    samx = [22.88]
    samy = [14.4]
    samz = [16.35]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeP [010]
    ext_vg = 11
    E_peak = 708
    num_cycles = 13
    yield from sleep(3)
    theta = [10]
    samx = [ 22.5470]
    samy = [25.51]
    samz = [16.97]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    ext_vg = 11
    E_peak = 708
    num_cycles = 13
    yield from sleep(3)
    theta = [54]
    samx = [24.152]
    samy = [25.51]
    samz = [18.77]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeAs [010]
    ext_vg = 11
    E_peak = 708
    num_cycles = 13
    yield from sleep(3)
    theta = [54]
    samx = [23.886]
    samy = [14.4]
    samz = [18.06]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeAs [010]
    ext_vg = 500
    E_peak = 700
    num_cycles = 3
    yield from sleep(3)
    theta = [54]
    samx = [23.886]
    samy = [14.4]
    samz = [18.06]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

def YIG_Spec_tth110():
    #yield from beamline_align_v2()
    #yield from sleep(5)

    # theta = 43.5
    ext_vg = 11
    E_peak = 710.0
    num_cycles = 6
    yield from sleep(3)
    theta = [54.0]
    #samx = [15.793]
    #samy = [65.0]
    #samz = [17.95]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(6,600,num_cycles,E_peak,ext_vg, 'YIG - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

def FeP_th27():
# FeP [010]
    theta = 27
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [27]
    samx = [23.12]
    samy = [25.51]
    samz = [18.1]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


def FeP_LV():
# FeP [010]
    theta = 43.5
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [43.5]
    samx = [23.72]
    samy = [25.51]
    samz = [18.55]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


def FeP_FeAs_thDepSaturday():
# FeAs [010]
    theta = 10
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [10]
    samx = [22.894]
    samy = [14.4]
    samz = [16.56]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeAs [010]
    theta = 43.5
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [43.5]
    samx = [23.49]
    samy = [14.4]
    samz = [17.7]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeP [010]
    theta = 10
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [10]
    samx = [22.62]
    samy = [25.51]
    samz = [17.55]
    yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeP [010]
    theta = 43.5
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [43.5]
    samx = [23.72]
    samy = [25.51]
    samz = [18.55]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeAs [010]
    theta = 27
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [27]
    samx = [23.13]
    samy = [14.4]
    samz = [17.2]
    yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeAs [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

# FeP [010]
    theta = 27
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [27]
    samx = [23.12]
    samy = [25.51]
    samz = [18.1]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


def FeP_th10():
# FeP [010]
    # theta = 10
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [10]
    samx = [22.574]
    samy = [25.51]
    samz = [17.24]
    #yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

def FeP_FeAs_thDep():
   # FeAs [010]
   # theta = 10
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [10]
    samx = [22.88]
    samy = [14.4]
    samz = [16.65]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

   # FeAs [010]
   # theta = 40
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [40]
    samx = [23.35]
    samy = [14.4]
    samz = [17.65]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

   #FeAs [010]
   # theta = 68
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [68.2]
    samx = [24.442]
    samy = [14.4]
    samz = [18.45]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


    # FeP [010]
    # theta = 68
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [67.8]
    samx = [24.606]
    samy = [25.510]
    samz = [18.94]
    yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


    # FeP [010]
    # theta = 10
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [10]
    samx = [22.57]
    samy = [25.51]
    samz = [17.29]
    yield from mv(cryo.t,theta[i]-2)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


    # theta = 40
    ext_vg = 11
    E_peak = 708
    num_cycles = 12
    yield from sleep(3)
    theta = [40]
    samx = [23.525]
    samy = [25.510]
    samz = [18.54]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'FeP [010] - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

def YIG_Spec_dinner_tth130():
    yield from beamline_align_v2()
    yield from sleep(5)

    # theta = 65
    ext_vg = 11
    E_peak = 710.0
    num_cycles = 6
    yield from sleep(3)
    theta = [65]
    #samx = [15.793]
    #samy = [65.0]
    #samz = [17.95]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(6,600,num_cycles,E_peak,ext_vg, 'YIG - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)




def E_cal_Fe():
    yield from rixs_one_energy(4,80,1,698,30, 'Fe cal - LV ')
    yield from rixs_one_energy(4,80,1,699,30, 'Fe cal - LV ')
    yield from rixs_one_energy(4,80,1,700,30, 'Fe cal - LV ')
    yield from rixs_one_energy(4,80,1,701,30, 'Fe cal - LV ')
    yield from rixs_one_energy(4,80,1,702,30, 'Fe cal - LV ')

def LCVO_OK_magnet_thDep():
    # theta = 10
    ext_vg = 15
    E_peak = 529.4
    num_cycles = 12
    yield from pol_V(4)
    yield from sleep(3)
    theta = [10]
    samx = [15.793]
    samy = [65.0]
    samz = [17.95]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'LCVO - LV - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    # theta = 25
    ext_vg = 15
    E_peak = 529.4
    num_cycles = 12
    theta = [25]
    samx = [16.58]
    samy = [65.0]
    samz = [20.33]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'LCVO - LV - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    # theta = 40
    E_peak = 529.4
    num_cycles = 12
    theta = [40]
    samx = [17.958]
    samy = [65.0]
    samz = [22.35]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'LCVO - LV - // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    # theta = 40
    yield from pol_H(2.5)
    yield from sleep(3)
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'LCVO - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)


def LCVO_OK_magnet_th67p5_LH():
    # theta = 67.5
    ext_vg = 15
    E_peak = 529.4
    num_cycles = 12
    theta = [10]
    #samx = [22.9181]
    #samy = [22.5]
    #samz = [17.34]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'LCVO - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)



def LCVO_OK_magnet_th67p5():
    # theta = 67.5
    ext_vg = 15
    E_peak = 529.4
    num_cycles = 12
    theta = [67.5]
    #samx = [22.9181]
    #samy = [22.5]
    #samz = [17.34]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(8,600,num_cycles,E_peak,ext_vg, 'LCVO - LH - // th = {} deg' .format(theta[i]))
        yield from sleep(1)




def Iron_100uc_emission():
    # Fe 100 uc
    ext_vg = 50
    E_peak = 700.0
    num_cycles = 4
    theta = [12]
    #samx = [22.9181]
    #samy = [22.5]
    #samz = [17.34]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(5,600,num_cycles,E_peak,ext_vg, 'Fe 100 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)

def Iron_30uc_6uc():
    # Fe 6 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 18
    theta = [12]
    #samx = [22.9181]
    #samy = [22.5]
    #samz = [17.34]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(3,600,num_cycles,E_peak,ext_vg, 'Fe 30 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    # Fe 30 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 8
    theta = [12]
    samx = [22.9381]
    samy = [19.3]
    samz = [17.14]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(1.5,600,num_cycles,E_peak,ext_vg, 'Fe 30 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)



def Iron_100uc():
    # Fe 100 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 2
    theta = [12]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.y,samy[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(1.5,600,num_cycles,E_peak,ext_vg, 'Fe 100 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)


def Iron_spec_overday():
    # Fe 3 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 4
    theta = [12]
    samx = [22.7951]
    samy = [28.0]
    samz = [17.67]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(5,600,num_cycles,E_peak,ext_vg, 'Fe 3 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)

def Iron_spec_overnight():
    # Fe 100 uc
    ext_vg = 11
    E_peak = 708.0
    theta = [65]
    samx = [25.0580]
    samy = [12.80]
    samz = [18.8200]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(2,600,4,E_peak,ext_vg, 'Fe 100 uc // th = {} deg' .format(theta[i]))
        yield from sleep(5)

    # Fe 30 uc
    ext_vg = 11
    E_peak = 708.0
    theta = [65]
    samx = [24.9140]
    samy = [19.3]
    samz = [18.770]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(3,600,6,E_peak,ext_vg, 'Fe 30 uc // th = {} deg' .format(theta[i]))
        yield from sleep(5)

    # Fe 6 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 12
    theta = [65]
    samx = [24.6650]
    samy = [22.5]
    samz = [18.67]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(4,600,12,E_peak,ext_vg, 'Fe 6 uc // th = {} deg' .format(theta[i]))
        yield from sleep(5)

    yield from beamline_align_v2()
    yield from sleep(5)
    # Fe 3 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 12
    theta = [65]
    samx = [24.6570]
    samy = [28.0]
    samz = [18.75]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(5,600,18,E_peak,ext_vg, 'Fe 3 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    # Fe 3 uc
    ext_vg = 11
    E_peak = 708.0
    num_cycles = 12
    theta = [65]
    samx = [24.6570]
    samy = [28.0]
    samz = [18.75]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.y,samy[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(5)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        yield from rixs_one_energy(5,600,18,E_peak,ext_vg, 'Fe 3 uc // th = {} deg' .format(theta[i]))
        yield from sleep(1)

    print('Macro is done!!! Go in peace!! RIXS rocks!!!')


def LCO_spec_overnight():
    ext_vg = 9.8
    total_time = 600
    split_time = 8
    E_peak = 528.95

    num_cycles = 10
    theta = [68]
    #samx = [  22.765,  23.2550,  23.91250]
    #samz = [ 17.620, 18.220, 18.745]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        print('#'*20)
        print('#'*80)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        print('#'*80)
        print('#'*20)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from sleep(1)
    
    print('Macro is done!!! Go in peace!! RIXS rocks!!!')

def LCO_LH_th40():
    ext_vg = 15
    total_time = 600
    split_time = 8
    E_peak = 529.4

    num_cycles = 10
    theta = [40]
    #samx = [  22.765,  23.2550,  23.91250]
    #samz = [ 17.620, 18.220, 18.745]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        print('#'*20)
        print('#'*80)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        print('#'*80)
        print('#'*20)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from sleep(1)
    print('Macro is done!!! Go in peace!! RIXS rocks!!!')

def LCO_OK():
    ext_vg = 20
    total_time = 600
    split_time = 5
    E_peak = 531.4

    num_cycles = 7
    theta = [10]
    #samx = [  22.765,  23.2550,  23.91250]
    #samz = [ 17.620, 18.220, 18.745]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        #yield from mv(cryo.x,samx[i])
        #yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        print('#'*20)
        print('#'*80)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        print('#'*80)
        print('#'*20)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from sleep(1)
    print('Macro is done!!!!!')


def LCO_qMap_night():
    ext_vg = 10
    total_time = 600
    split_time = 3
    E_peak = 931.0

    num_cycles = 10
    theta = [80, 90, 100, 110]
    samx = [ 25.74, 26.1800, 26.6200, 26.9970]
    samz = [ 18.785, 18.6750, 18.4550, 18.1950]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        print('#'*20)
        print('#'*80)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        print('#'*80)
        print('#'*20)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from sleep(1)

    print('#'*20)
    print('#'*80)
    print('#'*120)    
    print('loop is done')
    print('#'*120)
    print('#'*80)
    print('#'*20)
    yield from pol_H(-3)
    yield from sleep(5)
    theta = [110]
    samx = [ 26.9970 ]
    samz = [ 18.1950 ]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        print('#'*20)
        print('#'*80)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        print('#'*80)
        print('#'*20)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from sleep(1)


    yield from pol_V(4)
    yield from sleep(5)
    theta = [120]
    samx = [ 27.2800 ]
    samz = [ 17.8950 ]
    for i in range(len(theta)):
        yield from mv(cryo.t,theta[i])
        yield from mv(cryo.x,samx[i])
        yield from mv(cryo.z,samz[i])
        yield from sleep(1)
        print('#'*20)
        print('#'*80)
        print('#'*120)
        print('th = {} deg' .format(theta[i]))
        print('#'*120)
        print('#'*80)
        print('#'*20)
        yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak,ext_vg, 'th = {} deg' .format(theta[i]))
        yield from sleep(1)



def LCO_night():
    ext_vg = 10
    total_time = 600
    split_time = 3

    E_peak = 931.0

    ## Detune -0.75 eV 
    #detune=-0.75
    #num_cycles = 12
    #print('*'*150)
    #print('DE={}eV' .format(detune))
    #print('*'*150)
    #yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    #yield from sleep(1)

    ## Detune -0.5 eV 
    #detune=-0.5
    #num_cycles = 12
    #print('*'*150)
    #print('DE={}eV' .format(detune))
    #print('*'*150)
    #yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    #yield from sleep(1)

    # Detune -0.25 eV 
    #detune=-0.25
    #num_cycles = 12
    #print('*'*150)
    #print('DE={}eV' .format(detune))
    #print('*'*150)
    #yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV realign' .format(detune))
    #yield from sleep(1)

    # Detune 0 eV 
    #detune=0
    #num_cycles = 6
    #print('*'*150)
    #print('DE={}eV' .format(detune))
    #print('*'*150)
    #yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    #yield from sleep(1)

    # Detune 0.25 eV 
    detune=0.25
    num_cycles = 8
    print('*'*150)
    print('DE={}eV' .format(detune))
    print('*'*150)
    yield from rixs_one_energy(split_time,total_time,num_cycles,E_peak+detune,ext_vg, 'DE={}eV' .format(detune))
    yield from sleep(1)




def One_High_Stats():
    ext_vg = 7
    total_time = 600
    split_time = 5
    num_cycles=12
    target_Emax = 931.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,target_Emax,ext_vg, 'q = -0.3')


def CrO2():
    split_time = 5
    total_time = 1500
    num_cycles = 1
    ext_vg = 50

    energy = 582.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 581.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 580.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 579.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 578.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 577.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 576.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 575.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 574.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)
    energy = 584.5
    yield from rixs_one_energy(split_time,total_time,num_cycles,energy,ext_vg)

    


