'''
A Tale of Two Fits
------------------

    This simple example demonstrates the fitting of a linear function to
    two Datasets and plots both Fits into the same Plot.
'''

###########
# Imports #
###########

# import everything we need from kafe
import kafe
from kafe import ASCII, LaTeX, FitFunction
from PhyPraKit import odFit, labxParser, readColumnData
# additionally, import the model function we
# want to fit:
from kafe.function_library import linear_2par
import numpy as np

####################
# Helper functions #
####################

# -- define test configuration 
fname='Aufg2_2.dat'
ncols=3
data_array, info_dict =\
  readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
xdata=data_array[:,0] # 1st column
ydataA=data_array[:,1] # 2nd column
ydataB=data_array[:,2]

yer=0.0000001

def generate_datasets(output_file_path1,output_file_path2):
    '''The following block generates the Datasets and writes a file for
    each of them.'''

    import numpy as np  # need some functions from numpy

    my_datasets = []


    my_datasets.append(kafe.Dataset(data=(xdata, ydataA)))
    my_datasets[-1].add_error_source('y', 'simple', yer)
    
    my_datasets.append(kafe.Dataset(data=(xdata, ydataB)))
    my_datasets[-1].add_error_source('y', 'simple', yer)
    
    my_datasets[0].write_formatted(output_file_path1)
    my_datasets[1].write_formatted(output_file_path2)    

############
# Workflow #
############

# Generate the Dataseta and store them in files

generate_datasets('datasetb1.dat',
                  'datasetb2.dat')

# Initialize the Datasets
my_datasets = [kafe.Dataset(title=r'$d=5.4cm$'),
               kafe.Dataset(title=r'$d=7.8cm$')]

# Load the Datasets from files
my_datasets[0].read_from_file(input_file='datasetb1.dat')
my_datasets[1].read_from_file(input_file='datasetb2.dat')
# Create the Fits
my_fits = [kafe.Fit(dataset,
                    linear_2par,
                    fit_label="Ausgleichsgerade" )
           for dataset in my_datasets]

# Do the Fits
for fit in my_fits:
    fit.do_fit()

# Create the plots
my_plot = kafe.Plot(my_fits[0],my_fits[1])

mnA  = my_fits[0].get_parameter_values(rounding=False)
mnB  = my_fits[1].get_parameter_values(rounding=False)


mnA=np.around(mnA[0], decimals=4)
mnB=np.around(mnB[0], decimals=4)

#my_plot.axes.annotate(r'$m_{U_A=125V}= \  $' + str(mnA), xy=(0.8, 0.045), #size=15, ha='left')
#my_plot.axes.annotate(r'$m_{U_A=250V}= \  $' + str(mnB), xy=(0.8, 0.043), #size=15, ha='left')

my_plot.axis_labels = ['$Staudruck$ (Pa)', '$Stroemungswiderstand$ (N)']


# Draw the plots
my_plot.plot_all(show_info_for=None, show_data_for='all', show_function_for='all', show_band_for='meaningful')


###############
# Plot output #
###############

# Save the plots
my_plot.save('Aufg2_2.pdf')




# Show the plots
my_plot.show()
