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

fname='Aufg3_1.dat'
ncols=3
data_array, info_dict =\
  readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
x=data_array[:,0] # 1st column
y=data_array[:,1]*1000 # 2nd column
z=data_array[:,2]


plt.plot(x, y, 'ks')
plt.axis([-22,22,0,80])
plt.xlabel('$Anstellwinkel$ ($^{\circ}$)', size='large')
plt.ylabel('$Stroemungswiderstand$ (mN) ', size='large')
plt.grid()
plt.savefig('Aufg3_11.pdf')



plt.show()
