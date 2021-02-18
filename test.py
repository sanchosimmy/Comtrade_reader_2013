from tkinter import Tk
from tkinter import filedialog as fd
import math
import struct
import matplotlib.pyplot as plt
import numpy as np
Tk().withdraw()
print("Sancho's COMTRADE reader")
filename = fd.askopenfilename(initialdir='')
tempstring=filename.split('.')
datfile=tempstring[0]+".dat"
cfgfile=tempstring[0]+".cfg"
f = open(cfgfile, "rt")
pmu=f.readline().split(',')
pmu_name=pmu[0]
pmu_id=int(pmu[1])
COMTRADE_ver=pmu[2]
#print(pmu_name)
#print(pmu_id)
#print(COMTRADE_ver)
pmu=f.readline().split(',')
total=int(pmu[0])
temp=pmu[1].split('A')
tempstring=temp[0]
analog=int(tempstring)
print(f"Total channels = {total}")
print(f"Total Analog channels = {analog}")
digital=total-analog
print(f"Total Analog channels = {digital}")
analogchannelname=[];
digitalchannelname=[];
unit=[];
print("Analog channels are : ")
for x in range(0,analog):
    pmu=f.readline().split(',')
    analogchannelname.append(pmu[1])
    print(pmu[1])
    unit.append(pmu[4])
print("Digital channels are : ")
for x in range(0,digital):
    pmu=f.readline().split(',')
    digitalchannelname.append(pmu[1])
    print(pmu[1])
# print(analogchannelname)
# print(digitalchannelname)
pmu=f.readline()
pmu=f.readline()
pmu=f.readline().split(',')
tempstring=pmu[1]
samples=int(tempstring);
print(f"Total Number of samples = {samples}")
f.close()
f = open(datfile,"rb")
data=[]

# samples=100
for y in range(0,samples):
    tmp=[]
    ans=int.from_bytes(f.read(4),"little")
    tmp.append(ans)
    ans=int.from_bytes(f.read(4),"little")
    tmp.append(ans)
    for x in range(0,analog):
        ans=struct.unpack('<f', f.read(4))[0]
        tmp.append(ans)
    for x in range(0,math.ceil(digital/16)):
        ans=int.from_bytes(f.read(2),"little")
        tmp.append(ans)
    data.append(tmp)
data=np.array(data)
for x in range(0,analog):
    plt.figure(x+1)
    plt.plot(data[:,2+x])
    plt.xlabel('Samples')
    plt.ylabel(analogchannelname[x]+' ('+unit[x]+')')
# for y in range(0,analog):
#     plt.xlabel('Samples')
#     plt.ylabel(digitalchannelname[y])
#     plt.figure(x+1)
#     plt.plot(data[:,2+x])

# plt.xlabel('Samples')
# plt.ylabel('Value')

# plot1 = plt.figure(1)
# plt.plot(data[:,2])
# plot2 = plt.figure(2)
# plt.plot(data[:,3])
# plot2 = plt.figure(3)
# plt.plot(data[:,4])

plt.show()
f.close()	
