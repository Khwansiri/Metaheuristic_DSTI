# Continuous Optimization (dimension 50 and 500)
## F5: Shifted Griewank's Function   

<image src = "https://user-images.githubusercontent.com/57988473/81316383-c8af3180-908b-11ea-9924-e8b141cb6d00.png" width = "600">

- ### Additional information  
[Function Description](https://github.com/Khwansiri/Metaheuristic_DSTI/blob/master/Shifted%20Sphere%20Function/CEC2008_TechnicalReport.pdf)    
[Code of the function](https://github.com/Khwansiri/Metaheuristic_DSTI/blob/master/Shifted%20Sphere%20Function/benchmark.c)      
[Shifts](https://github.com/Khwansiri/Metaheuristic_DSTI/blob/master/Shifted%20Sphere%20Function/data.h)    

- ### The chosen algorithm       
Dimension 50  :    Nelson-Mead method from SciPy package   
Dimension 500 :    Broyden-Fletcher-Goldfarb-Shanno method from SciPy package   

- ###	The parameters of the algorithm     
Tolerance for termination: 1E-04       

- ### The fitness     
Dimension 50  :    -138.32  
Dimension 500 :    -121.14   
     

- ###	The computational time     
Dimension 50   :   0.26    seconds  
Dimension 500 :    0.07    seconds  
