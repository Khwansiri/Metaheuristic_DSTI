# Travelling Salesman Problem with Simulated Annealing Algorithm
# Qatar 194 cities

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import random
import time


start_time = time.time() # To evaluate computational time

# Download data
cities = pd.read_csv("E:\DataScience\DSTI\Metaheuristic\Exam\TSP\Qatar_194.csv")
cities.index +=1



# Simulated Annealing Algorithm (SA)
# Input parameter for SA
T0 = 1500       # Starting temperature (should start with a large temperature)
M = 250         # Total iteration for temperature decreaing  
N = 20          # Total neighborhood to be searched before chaging the temperature  (In general, 15 - 20)
alpha = 0.9     # Level of temperature decresing in each iteration (In general, 0.8-0.95)


# Initial random cities combination
index_list = cities.index.values.tolist()
X0 = index_list[:]
random.shuffle(X0)

Temp = []
Min_Cost = []

for i in range(M):
    for j in range(N):
        
        xt= index_list[:]
        random.shuffle(xt)
        
        cities_init = cities.reindex(index=X0)  # Reindex dataframe with the arrangement as X0
        cities_new  = cities.reindex(index=xt)
        
        # Define euclidean distance
        def euclidean(list_of_city): 
            # Step 1: Create new df as the copy of list_of_city
            list_for_dist = list_of_city.copy()
            # Step 2: Create new column as difference between x and y in each row 
            list_for_dist["diff_X"] = list_for_dist["X"]-list_for_dist["X"].shift(-1)
            list_for_dist["diff_Y"] = list_for_dist["Y"]-list_for_dist["Y"].shift(-1)
            # Step 3: Create new column as square difference 
            list_for_dist["pow_diff_X"] = list_for_dist["diff_X"]**2
            list_for_dist["pow_diff_Y"] = list_for_dist["diff_Y"]**2
            # Step 4: Create new colum as root of sum of square 
            list_for_dist["Euclidean Distance"] = (list_for_dist["pow_diff_X"]+list_for_dist["pow_diff_Y"])**.5
                # Objective function = minimize the sum of Euclidean Distance in this combination
            return sum(list_for_dist["Euclidean Distance"][0:-1])

    dist_init = euclidean(cities_init)
    dist_new = euclidean(cities_new)
        
        
    # In case the new solution is worse, we need to figure out if we should take it or not 
    # The closer we get to the end of our search (the lower temp.), it will be less likely to take the worse solution 
    rand1 = np.random.rand()
    form = 1/(np.exp(dist_new-dist_init)/T0)
        
    if dist_new <= dist_init :   # If the new solution is better, we take it and make it our new solution
        X0 = xt
    elif rand1 <= form:        # If the new solution is worse, but random number is lower than the formula, we take that new solution
        X0 = xt
    else:                    # If the new solution is worse and the random number is greater than the formula, we don't take it
        X0 = X0
        
    # Finish the inner loop (all neighbour of the same temp)
        
        
    Temp.append(T0)    # Append the temp. for plot
    Min_Cost.append(dist_init)
    
    T0 = alpha*T0      # After done with inner loop and already append the temp to the temp list, now we update the temperature


print()
print("Final Cities Order:",X0)
print("Minimized Distant: {:.2f}".format(dist_init))


plt.plot(Temp,Min_Cost)
plt.title("Cost vs. Temperature", fontsize=20,fontweight='bold')
plt.xlabel("Temperature", fontsize=18,fontweight='bold')
plt.ylabel("Cost", fontsize=18,fontweight='bold')
plt.xlim(1500,0)

plt.xticks(np.arange(min(Temp),max(Temp),100),fontweight='bold')
plt.yticks(fontweight='bold')
plt.show()

print("Computational time: {:.2f} seconds".format(time.time()-start_time))















