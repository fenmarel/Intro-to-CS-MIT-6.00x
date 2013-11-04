# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *


#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    wait_time = (300, 150, 75, 0)
    finals = [[] for i in wait_time]
    for wait in wait_time:
        results = []
        print "\ntrial (wait time = " + str(wait) + ") working",
        for i in range(numTrials):
            tmp = simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
                                     0.005, 1, before_drug=wait, after_drug=150, plot=False)
            results.append(tmp[-1])
            if i%2: print ".",
        finals[wait_time.index(wait)] += results
    for results in finals:    
        pylab.hist(results, [x for x in range(1000) if x % 50 == 0])
        pylab.title("Wait Time = " + str(wait_time[finals.index(results)]))
        pylab.xlabel("Final Virus Populations")
        pylab.ylabel("Trials")
        pylab.ylim(0, numTrials)
        pylab.show()

#simulationDelayedTreatment(5)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # simulation incorrect...
    
    wait_time = (300, 150, 75, 0)
    finals = [[] for i in wait_time]
    for wait in wait_time:
        results = []
        print "\ntrial (wait time = " + str(wait) + ") working",
        for i in range(numTrials):
            tmp = simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
                                     0.005, 1, before_drug=150, after_drug=wait, plot=False)
            sec_tmp = simulationWithDrug(int(tmp[-1]), 1000, 0.1, 0.05, {'grimpex': False},
                                         0.005, 1, before_drug=0, after_drug=150, plot=False)
            results.append(tmp[-1])
            if i%2: print ".",
        finals[wait_time.index(wait)] += results
    for results in finals:    
        pylab.hist(results, [x for x in range(1000) if x % 50 == 0])
        pylab.title("Wait Time = " + str(wait_time[finals.index(results)]))
        pylab.xlabel("Final Virus Populations")
        pylab.ylabel("Trials")
        pylab.ylim(0, numTrials)
        pylab.show()
        
