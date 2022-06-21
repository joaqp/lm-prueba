import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

p=pd.read_csv("./presion_tp1.csv")
print(type(p))
Fs=500
Ts=1/Fs

L=len(p)
print("L:{0}".format(L))
K=np.arange(0,L)
t=K*Ts


fft_spectrum = np.fft.rfft(p)
fft_spectrum_abs = np.abs(fft_spectrum)
res = float(Fs / (L-1)) #Resolucion frecuencial
n = np.array(range(0, L)) * res 


plt.subplot(2,1,1)
line,=plt.plot(t,p)
line.set_color('red')
plt.xlabel("t(s)")
plt.ylabel("Voltaje")


plt.subplot(2,1,2)
line,=plt.plot(n, fft_spectrum_abs)
line.set_color('orange')
plt.xlabel("frequencia, Hz")
plt.ylabel("Amplitud")

plt.show()