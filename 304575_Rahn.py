#notes
#change polarization is either:
#RE(pol_H(0))
#or:
#RE(pol_V(0))


#After changing polarization, run:
#RE(beamline_align_v2())


#To measure signal from carbon tape for a quick test:
def measurecttest():
    ext_vg = 15
    E_peak = [1518.25]
    split_times = [4]
    total_times = [180]
    num_cycles = 1    
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg)


#To do initial alignment of sample or carbon tape on beam, run this function:

# ******* th=75 **********
def ct75100k():
    yield from mv(cryo.x,19.04)
    yield from mv(cryo.y,12.5)
    yield from mv(cryo.z,17.04)
    yield from mv(cryo.t,65.5)

def sample75100k():
    yield from mv(cryo.x,19.031)
    yield from mv(cryo.y,9.3)
    yield from mv(cryo.z,19.84)
    yield from mv(cryo.t,65.5)

#Specular on left sensor at 69.2 deg
#cryox is 19.124
#cryoy is 13
#cryoz is 19.9

#Specular on right sensor at 70.2 deg
#Note: always increase th

# ******* th=30 **********
def ct30100k():
    yield from mv(cryo.x,20.2)
    yield from mv(cryo.y,12.5)
    yield from mv(cryo.z,13.4)
    yield from mv(cryo.t,30)

def sample30100k():
    yield from mv(cryo.x,18.645)
    yield from mv(cryo.y,9.3)
    yield from mv(cryo.z,15.88)
    yield from mv(cryo.t,30)

#CHECK MANUALLY ALIGNMENT WITH:
#EXPOSURE TIME 1 SEC
#EXIT SLIT 300 UM
#DETECTOR MODE SET TO DETECTOR OUTPUT
#IMAGING MODE SET TO CONTINUOUS
#ADJUST CCZ TO PLACE BEAMS IN CENTER OF SENSORS


#To measure signal from carbon tape:
def measurect():
    ext_vg = 15
    E_peak = [1518.25]
    split_times = [4]
    total_times = [360]
    num_cycles = 1    
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg)


#To measure signal from sample, run this function:
def measuresample():
    ext_vg = 15
    E_peak = [1518.25]
    split_times = [4]
    total_times = [360]
    num_cycles = 17    
    for en, split, total in zip(E_peak, split_times, total_times):
        yield from rixs_one_energy_1(split, total, num_cycles, en, ext_vg)


# ========  LEGACY SCRIPTS =============
#********** th=75 ***************
def ct75rt():
    yield from mv(cryo.x,19.66)
    yield from mv(cryo.y,17)
    yield from mv(cryo.z,16.94)
    yield from mv(cryo.t,65.5)

def sample75rt():
    yield from mv(cryo.x,19.28)
    yield from mv(cryo.y,13)
    yield from mv(cryo.z,19.59)
    yield from mv(cryo.t,65.5)
      
def ct7530k():
    yield from mv(cryo.x,19.04)
    yield from mv(cryo.y,12.5)
    yield from mv(cryo.z,17.04)
    yield from mv(cryo.t,65.5)

def sample7530k():
    yield from mv(cryo.x,19.05)
    yield from mv(cryo.y,8.5)
    yield from mv(cryo.z,19.9)
    yield from mv(cryo.t,65.5)

#********** th= ***************
def ct30rt():
    yield from mv(cryo.x,20.82)
    yield from mv(cryo.y,17)
    yield from mv(cryo.z,13.94)
    yield from mv(cryo.t,30)

def sample30rt():
    yield from mv(cryo.x,18.8)
    yield from mv(cryo.y,13)
    yield from mv(cryo.z,15.52)
    yield from mv(cryo.t,30)

def ct3030k():
    yield from mv(cryo.x,20.2)
    yield from mv(cryo.y,12.5)
    yield from mv(cryo.z,13.4)
    yield from mv(cryo.t,30)

def sample3030k():
    yield from mv(cryo.x,18.645)
    yield from mv(cryo.y,8.5)
    yield from mv(cryo.z,15.88)
    yield from mv(cryo.t,30)



     

