import pandas as pd 
import numpy as np 
import matplotlib 
from prettytable import PrettyTable 
  
data=pd.read_csv(r"HW1_part2.csv", header=None) 
   
distances=data.iloc[:, 0] 
   
given_distances=[] 
for i in range(1, len(distances)): 
     
     
given_distances.append(float(distances[i])) 
print(given_distances) 
   
pd0=data.iloc[0,1:].mean() #pd0 value is mean of B1 through N1 
   
y_columns=data.iloc[:, 1:]  
mean_of_remaining=y_columns.mean(axis=1) #mean of other rows 
   
calculated_distances=[] #Calculated distances will be stored here 
   
n=5.75 #Path Loss component calculated in step 1 
   
   
#print(mean_of_remaining) 
for i in range(1, len(mean_of_remaining)): 
     
exponent = (pd0-mean_of_remaining[i])/(10*n) 
    
      
calculated_distances.append(round(float(pow(10, exponent)),3)) 
print(calculated_distances) 
   
calculated_distances_table=PrettyTable(["Calcaulated Distances"]) 
for i in range(0,5): 
     
calculated_distances_table.add_row([f"{calculated_distances[i]}"]) 
      
print(calculated_distances_table) 
      
error_row=[] 
for i in range(0,5): 
     
error_row.append(round(calculated_distances[i]-given_distances[i],3)) 
      
print(error_row) 
   
avg_error=round(np.average(error_row),3) 
print(f"Average Error: {avg_error}") 
   
myTable=PrettyTable(["Calculated Distances", "Given Distances", "Error"]) 
   
for i in range(0,5): 
    
myTable.add_row([f"{calculated_distances[i]}", f"{given_distances[i]}", 
f"{error_row[i]}"]) 
     
print(myTable) 
      
   
average_error = PrettyTable(['Average Error'])  
average_error.add_row([f"{avg_error}"]) 
print(average_error) 
