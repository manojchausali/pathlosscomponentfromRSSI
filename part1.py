import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
   
data=pd.read_csv(r”HW1_part1.csv”, header=None) 
#print(data.iloc[0,1:]) 
x = data.iloc[:, 0] #First column as x-axis 
x_log=np.log10(x) 
#print(x_log) 
y_columns = data.iloc[:, 1:] 
y_mean = y_columns.mean(axis=1) 
# Loop through each column starting from the second one 
for i in range(1, data.shape[1]): 
     y = data.iloc[:, i]  # Each remaining column as y-axis 
     plt.scatter(x_log, y)   
      
plt.scatter(x_log, y_mean, color=’black’, marker=’o’, label=’Mean of RSSI’) 
   
coefficients = np.polyfit(x_log, y_mean, 1)  # 1 indicates linear fit 
line_of_best_fit = np.polyval(coefficients, x_log) 
# Plot the best fit line 
plt.plot(x_log, line_of_best_fit, color=’red’, linestyle=’–', label=’Best Fit Line’) 
  
slope=coefficients[0] 
path_loss_component=abs(slope/10) 
print(f”Pass loss component: {path_loss_component}”) 
variance = np.var(y_mean – line_of_best_fit) 
print(“Variance:”, variance) 
plt.xlabel(‘X Axis (Distances in log)’) 
plt.ylabel(‘Y Axis (RSSI in dBm)’) 
plt.title(‘RSSI vs Distance’) 
plt.legend()  
plt.show()  
