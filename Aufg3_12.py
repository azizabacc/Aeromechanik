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
z=data_array[:,2]*1000


def lin(a,b):
    f=a*b
    return f
xdata=np.linspace(0,15,100)

plt.plot(y, z, 'ks')
plt.plot(xdata,lin(xdata,30), 'r')
plt.axis([-1,80,-10,520])
plt.xlabel('$Stroemungswiderstand$ (mN) ', size='large')
plt.ylabel('$Auftriebskraft$ (mN)', size='large')
plt.grid()
plt.savefig('Aufg3_13.pdf')



plt.show()
