from xmlrpc.client import _datetime_type
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

#Ejercio 2a y 2b ----------------------------------------

S1=pd.read_csv("./presion_tp1.csv")
print(type(S1))
Fs=500
Ts=1/Fs

L=len(S1)
# print(S1.values.reshape([1,L]).tolist())
# print("L:{0}".format(L))
K=np.arange(0,L)
t=K*Ts


Vmax_sensor=1
Vmin_sensor=-1

Vmax_ADC=3.3
Vmin_ADC=0

G=(Vmax_ADC-Vmin_ADC)/(Vmax_sensor-Vmin_sensor)
offset=(Vmax_ADC-Vmin_ADC)/2

S2=S1*G+ offset
res = float(Fs / (L-1)) #Resolucion frecuencial
n = np.array(range(0, L)) * res 

#Ejercicio 3 --------------------------------------

S2_min= Vmin_ADC
S2_max=Vmax_ADC


#D1 -> 8 bits ---------------

N1=8
D1_min=0
D1_max=2**N1-1
D1f=(S2*(D1_max/S2_max))
D1=round(S2*(D1_max/S2_max))
E1=D1-D1f

plt.subplot (3,1,1) 
plt.plot(t, D1)    
plt.plot(t, D1f)
plt.plot(t, E1)                                                                     
plt.xlabel('t[s]')  

plt.title("D1")

#D2 --> 12

N2=12
D2_max=2**N2-1
D2f=(S2*(D2_max/S2_max))
D2=round(S2*(D2_max/S2_max))
E2=D2-D2f

 
plt.subplot (3,1,2) 
plt.plot(t, D2)    
plt.plot(t, D2f)
plt.plot(t, E2)                                                                     
plt.xlabel('t[s]')                                                         
plt.title("D2")

#D3 --> 24

N3=24
D3_max=2**N3-1
D3f=(S2*(D3_max/S2_max))
D3=round(S2*(D3_max/S2_max))
E3=D3-D3f

plt.subplot (3,1,3) 
plt.plot(t, D3)    
plt.plot(t, D3f)
plt.plot(t, E3)                                                                     
plt.xlabel('t[s]')                                                         
plt.title("D3")

plt.plot
#Graficos ------------------------------------
plt.subplot(2,1,1)
line,=plt.plot(t,S1)
line.set_color('red')
plt.xlabel("t(s)")
plt.ylabel("Voltaje")

plt.subplot(2,1,2)
line,=plt.plot(n, S2)
line.set_color('orange')
plt.xlabel("frequencia, Hz")
plt.ylabel("Amplitud")


plt.show()

#---------------------------------------------------




