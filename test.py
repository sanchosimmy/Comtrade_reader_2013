from tkinter import filedialog as fd
import math
import struct
import matplotlib.pyplot as plt
import numpy as np
print("Sancho's COMTRADE reader")
filename = fd.askopenfilename(initialdir='')
tempstring=filename.split('.')
datfile=tempstring[0]+".dat"
cfgfile=filename
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
print(total)
print(analog)
digital=total-analog
analogchannelname=[];
digitalchannelname=[];
unit=[];
for x in range(0,analog):
    pmu=f.readline().split(',')
    analogchannelname.append(pmu[1])
    unit.append(pmu[4])
for x in range(0,digital):
    pmu=f.readline().split(',')
    digitalchannelname.append(pmu[1])
print(analogchannelname)
print(digitalchannelname)
pmu=f.readline()
pmu=f.readline()
pmu=f.readline().split(',')
tempstring=pmu[1]
samples=int(tempstring);
print(samples)
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
# for x in range(0,10):
#     print(data[x])
data=np.array(data)
print(data.shape)
plt.plot(data[:,2])
plt.plot(data[:,3])
plt.plot(data[:,4])
plt.show()

"""
a=f.read(4)
ans=int.from_bytes(a,"little")
print(type(ans))
print(ans)
print(f"A={a}")
a=f.read(4)
ans=int.from_bytes(a,"little")
print(type(ans))
print(ans)
print(f"A={a}")

a=f.read(4)
ans=struct.unpack('<f', f.read(4))
print(type(ans))
print(ans)
print(f"A={a}")

a=f.read(4)
ans=struct.unpack('<f', a)
print(type(ans))
print(ans)
print(f"A={a}")
a=f.read(4)
ans=struct.unpack('<f', a)
print(type(ans))
print(ans)
print(f"A={a}")


#print(f"E={e}")
#sample_no = int(e,16)
#print(sample_no)
#struct.unpack('!f', bytes.fromhex(t))
"""
f.close()	
