# Continuous Optimization (dimension 50 and 500)
## F3: Shifted Rosenbrock's Function

<image src = "https://user-images.githubusercontent.com/57988473/81186391-055b2a00-8fb3-11ea-984a-021ea5000d39.png" width = "550">

- ### Additional information  
[Function Description](https://github.com/Khwansiri/Metaheuristic_DSTI/blob/master/Shifted%20Sphere%20Function/CEC2008_TechnicalReport.pdf)    
[Code of the function](https://github.com/Khwansiri/Metaheuristic_DSTI/blob/master/Shifted%20Sphere%20Function/benchmark.c)      
[Shifts](https://github.com/Khwansiri/Metaheuristic_DSTI/blob/master/Shifted%20Sphere%20Function/data.h)    

- ### The chosen algorithm       
  Evolutionary Algorithm with Global Discrete Strategy
  
  
  <img src="https://user-images.githubusercontent.com/57988473/81186672-5d922c00-8fb3-11ea-99b6-887b3a503dbb.png" width="700">   


- ### The parameters of the algorithm   
  Number of parent (µ) = 120   
  Number of children (λ) = µ*6   
  Number of iterations (M) = 30   
  Increase sigma with 1/5th rule (a)   
  Next generation = 10% from parent’s pool, 90% from children‘ pool of each generation  


- ### The fitness   
  Dimension 50 :   1E+08  
  Dimension 500:   1E+08

- ### The computational time  
  Dimension 50 :   18    seconds  
  Dimension 500:   48.95 seconds
