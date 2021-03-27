import numpy as np
import matplotlib.pyplot as plt

Nmeas = 100
Nexp  = 50
  
mu_true = []
mu_true_items = np.arange(-10,10,0.1)
sigma = 2;

plt.figure()
title1 = "Neyman Construction"

# loop through different mu_true
for i in mu_true_items:
    mu_true = i
    mu_best_items = []
    for exp in range(0,Nexp):
        mu_best = 0
# loop through measurements in experiment
        for meas in range(0,Nmeas):
            x = np.random.normal(mu_true,sigma)
            mu_best += x
          
# our "measurement" for mu best fit
        mu_best = mu_best / Nmeas
        mu_best_items.append(mu_best)
        
    x_array = np.zeros(Nexp)+mu_true
                   
    plt.scatter(x_array,mu_best_items,color='salmon',alpha=0.2,s=1)
      
plt.xlabel('$\\mu_{true}$')
plt.ylabel('$\\mu_{best}$')
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.tick_params(axis='both')
plt.title(title1)
plt.grid(True)

#Developed with help from Kim Conger