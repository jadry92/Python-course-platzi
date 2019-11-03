import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import sin, cos, pi
import struct 
#npoints=50
#x = [x*2*pi/npoints for x in range(npoints+1)]
#y1 = [sin(t) for t in x]
#y2 = [cos(t) for t in x]

#for i in x:
#	a[i]=x[i]-x[i]

#print(x)

#plt.figure(figsize=(10, 5))
#plt.title('Sine & Cosine')
#plt.xlabel('t (radians)')
#plt.ylabel('red: sin (t), blue: cos (t)')
#plt.grid(True)
#plt.xlim(0,2*pi)
#plt.ylim(-1.1,1.1)
#a=[[1,2,3],[1,2,3],[1,2,3]]
#plt.plot(x, y1, color="red", label="sine")
#plt.plot(x, y2, color="blue", label="cosine")
#plt.legend()
f = open("/home/equipo4/Documentos/UIS/JOHAN/FWI_dens_cons/input/Modelo_ori_marmousi_1.bin", "rb")
nz=211
nx=68
nt=876

#P=f.read(4)
P = struct.unpack('f'*nx*nz,f.read(nx*nz*4))
f.close()

#hess = [[0 for ix in range(nz)] for iz in range(nx)]
#hess = np.zeros(nx,nz)

#for iz in range(0,nx):
#	for ix in range(0,nx): 
#		hess[iz][ix]=P[ix+nx*iz]

hess = np.reshape(P,[nx,nz])
#a = [11,1,1,1,1,1,2,12,3,13,1,31,31,4,5,465,]
#b = [a for v in a if v % 2 != 0]
#print(a)
#print(b)
#print(hess)
#print(hess)	
plt.imshow(hess)
plt.show()

