import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

S1=pd.read_csv("./presion_tp1.csv")
print(type(S1))
Fs=500
Ts=1/Fs

L=len(S1)
print(S1.values.reshape([1,L]).tolist())
print("L:{0}".format(L))
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

