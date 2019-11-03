from numpy import *
import scipy.linalg
import struct 
# Open the binarye
f_1 = open("/home/equipo4/Documentos/UIS/JOHAN/results/test_complet/cubo_imagen.bin", "rb")
f_2 = open("/home/equipo4/Documentos/UIS/JOHAN/results/test_complet/points_of_fwi_4913.bin", "rb")

nz = 69
nx = 215
nt = 625
n = 4913
ex = 200

direct = struct.unpack('f'*n*2,f_2.read(n*2*4))
f_2.close()

cube = struct.unpack('f'*ex*nz*nx,f_1.read(nx*nz*ex*4))
f_1.close()

cube_img = [[[0 for iz in range(nz)] for ix in range(nx)] for ie in range(ex)]

for ie in range(0,ex):
	for ix in range(0,nx):
		for iz in range(0,nz):
			cube_img[ie][ix][iz] = cube[iz + nz*ix + nz*nx*ie]

for i in range(0,10):
	print(cube_img[0][0][i])

