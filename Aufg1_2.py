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

fname='Aufg1_2.dat'
ncols=2
data_array, info_dict =\
  readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
x=data_array[:,0] # 1st column
y=data_array[:,1] # 2nd column

plt.plot(x,y,'ks')
plt.axis([0,3000,0,14])
plt.grid()
plt.xlabel('$Drehzahl$',size='large')
plt.ylabel('$Geschwindigkeit v (m/s^2)$',size='large')

plt.legend(loc='best')

plt.savefig('Aufg1_2.pdf')


plt.show()
