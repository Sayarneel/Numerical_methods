import numpy as np
x=[0,1,2]
y=[1,2,4]     
xp=1.5  
yp=0       
for i in range (3):    
  p=1                     
  for j in range (3):   
    if i!=j:    
      p=p*(xp-x[j])/(x[i]-x[j])   
   yp=yp+p*y[i]      
print('Interpolated value=',yp) 
print('Exact Value=', 2**xp)  
d=2**xp-yp                                                                                              
print('Difference=',d)
