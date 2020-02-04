# Assignment -3 
1. Solve linear regression via gradient descent for ‘d’ dimensional input and N samples using individual parameter updates
(theta_i's) in a non-vectorised setting.\
  Method should include: \
    a. Alpha (learning rate, default: 0.01) \ 
    b. number of iterations (default: 100) \
    c. Num_restarts (default: 1) We initialise theta_i’s randomly num_restarts number of times. We choose the
       solution which gives the least cost amongst the different initialisation. \
    d. Learning rate function over time: \
      (i) ‘Constant’: (default)learning rate does not change over time \
      (ii) ‘Inverse’: learning rate is alpha/t where t is the iteration number \
    e. Batch_size (default:N, setting to 1 converts to SGD, setting to some number between 1 and N converts to mini-batch GD. 
     Edit linearRegression/gradient_descent (non_vectorized_gd()) [3 marks]
     
2. Solve the above using gradient descent in vectorised form with all the same set of parameters. Edit linearRegression/
gradient_descent (vectorized_gd()) [2 marks]

3. Write a function gradientDescentAutogradRegression() to learn the regression coefficients using gradient descent. Instead
of writing the formulae for computing gradients by yourself, you will use Autograd to automatically do that for you. All other
parameters remain the same. Edit linearRegression/gradient_descent (autograd_regression_gd()) [1 mark]


4. Write a function inspired by sklearn’s polynomial preprocessing: (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html) your function should have: degree and include bias parameters only.Edit
preprocessing/polynomial_features [1 mark]

5. Create a data set as follows: 
```python
x = np.array([i*np.pi/180 for i in range(60,300,4)]) 
np.random.seed(10) #Setting seed for reproducibility 
y = 4*x + 7 + np.random.normal(0,3,len(x)) 
```
Now, using your newly created function for polynomial feature generation above, plot magnitude of theta v/s degree when you fit
linear regression using the polynomial of degree d. What can you conclude? Edit q5_plot.py [1 mark] 


6. Now, use the above code and for degree = 1, 3, 5, 7, 9, plot magnitude of theta v/s degree for varying N, where N is the size of
the data set (size of x, and thus y). What can you conclude? Edit q6_plot.py [1 mark]


7. For gradient descent (any of the above implementation) plot the contour and update in 2 parameters (theta_0 and theta_1).Write a function to plot three views of gradient descent update. First being: the surface plot of RSS in 3D, second being the
line fit, and the third being the contour. The first two would like the following: https://giphy.com/gifs/gradient-O9rcZVmRcEGqI and the third would look like the following: https://giphy.com/gifs/gradient-6QlTwkigqg4yk. You can create
a GIF using any online services (after you have created the images) and need to show only the first 10 iterations. Edit
q7_plot.py [3 marks]
8. Compare time required for gradient descent v/s normal and see if it matches theoretical numbers. Edit q8_compare_time.py
[1 mark]
9. Create a data set that suffers from multicollinearity and check if your gradient descent implementation works. Edit
q9_dataset.py [1 mark]
