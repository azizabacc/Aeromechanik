'''
Comparison of two models for the same data
------------------------------------------

    In this example, two models (exponential and linear) are fitted
to data from a single Dataset.
'''

###########
# Imports #
###########

# import everything we need from kafe
import kafe
# script test_readColumnData.py
# -*- coding: utf-8 -*-

import sys, numpy as np, matplotlib.pyplot as plt
from PhyPraKit import odFit, labxParser, readColumnData
# additionally, import the two model functions we
# want to fit:
from kafe.function_library import linear_2par, exp_2par



fname='Aufgabe_21.dat'
ncols=7
data_array, info_dict =\
  readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
Abstand=data_array[:,0] # 1st column
rnull  =data_array[:,1] # 2nd column
reins  =data_array[:,2]
rzwei  =data_array[:,3]
rdrei  =data_array[:,4]
rvier  =data_array[:,5]
rfunf  =data_array[:,6]



x=(10.,20.,30.,35.)

plt.plot(x,rnull,'bs')
plt.plot(x,rnull,'b', label='r=0cm')
plt.plot(x,reins,'rs')
plt.plot(x,reins,'r', label='r=1cm')
plt.plot(x,rzwei,'gs')
plt.plot(x,rzwei,'g', label='r=2cm')
plt.plot(x,rdrei,'ms')
plt.plot(x,rdrei,'m', label='r=3cm')
plt.plot(x,rvier,'cs')
plt.plot(x,rvier,'c', label='r=4cm')
plt.plot(x,rfunf,'ys')
plt.plot(x,rfunf,'y', label='r=5cm')



plt.axis([5,45,0,130])
plt.grid()
plt.xlabel('$l$ (cm)',size='large')
plt.ylabel('$dynamischer Druck$ p (Pa)',size='large')

plt.legend(loc='best')

plt.savefig('Aufg1_1.pdf')


plt.show()
