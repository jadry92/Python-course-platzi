#/**************************/
#  Statistic measures
#  by Dorfell L. Parra Prada
#  2015/07/25 
#/**************************/

import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


#---------------------------
# Initializing...
#---------------------------
# Empty list
lt_aux = []; lt_tmp = []
lt_key = []; lt_val = []
# tmp variables
tmp = 0; lt_len = 0;
# Read the file
fin = open("test/log_3.tmp","r")
fin.seek(0)

# Creating a list with data
for line in fin:
    lt_aux.append(float(line.strip()))
lt_len = len(lt_aux)
print "Clock cycles from 1 warp up to %s warps: \n " %(lt_len) , lt_aux 
print " "


#---------------------------
# Histogram 
#---------------------------
def histogram(s):
	''' This function creates an histogram'''
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

stat_hist = histogram(lt_aux)
print "Clock cycles histogram: \n ", stat_hist
print " "


#---------------------------
# Figure 1: Clock cycles, iteration and  frequencies
#---------------------------
plt.figure(1)

# Subplot  1: clock cycles per iteration
plt.subplot(2, 1, 1)
#plt.suptitle('CLOCK CYCLES PER ITERATION AND HISTOGRAM')
plt.title('Clock cycles per iterations')
plt.ylabel('Clock cycles')
plt.xlabel('warps')
plt.grid(color='gray', linestyle='dotted', linewidth=0.5)
plt.plot(range(1, lt_len + 1), lt_aux, 'bo-')
plt.xticks(np.arange(1, lt_len + 1, 2)) # ticks resolution
plt.yticks(np.arange(0, max(lt_aux) + 10, 10))

# Subplot 2: plotting histogram 
for key in stat_hist:
	lt_key.append(key)
	lt_val.append(stat_hist[key])
lt_aux2 = [1,1,1,2,2,2,2,3]
plt.subplot(2, 1, 2)
plt.title('Histogram')
plt.ylabel('Frequency')
plt.xlabel('Clock cycles')
plt.grid(color='gray', linestyle='dotted', linewidth=0.5)
plt.hist(lt_aux, bins=50, facecolor='blue' )

plt.tight_layout() # space between subplots
plt.draw()  # Draw figure
plt.savefig("test/histogram.ps")

#---------------------------
# Mode 
#---------------------------
for key in stat_hist:
	lt_tmp.append(stat_hist[key])
stat_mode = list(stat_hist.keys())[list(stat_hist.values()).index(max(lt_tmp))]
print "Clock cycles mode of the %s warps: \n"  %(lt_len), stat_mode,"-->", max(lt_tmp), "times" 
print " "


#---------------------------
# Mean 
#---------------------------
stat_mean = sum(lt_aux)/(len(lt_aux))
print "Clock cycles mean of the %s warps: \n" %(lt_len), stat_mean
print " "


#---------------------------
# Variance  
#---------------------------
for idx in range(0,len(lt_aux)):
	tmp = tmp + (lt_aux[idx]-stat_mean)**2

stat_vari = float(tmp)/len(lt_aux) 
print "Clock cycles variance of the %s warps: \n" %(lt_len) , stat_vari
print " "


#---------------------------
# Standard deviation 
#---------------------------
stat_sdev = math.sqrt(stat_vari)
print "Clock cycles standard deviation of the %s warps: \n" %(lt_len) , stat_sdev
print " "


#---------------------------
# Done statistics measurements! 
#---------------------------
print "Statistics measurements-> Done! 8-) "
print " "
