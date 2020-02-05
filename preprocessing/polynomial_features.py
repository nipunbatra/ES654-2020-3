''' In this file, you will utilize two parameters degree and include_bias.
    Reference https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PolynomialFeatures():
    """
    Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree. 
    For example, if an input sample is two dimensional and of the form [a, b], the degree-2 polynomial features are [1, a, b, a^2, ab, b^2].
    """
    
    def __init__(self, degree=2,include_bias=True):
        """
        Inputs:
        param (int) degree : max degree of polynomial features
        param (boolean) include_bias : specifies wheter to include bias term in returned feature array.
        """
        
        
        pass

    
    def transform(self,X):
        """
        Transform data to polynomial features
        
        Inputs:
        param X : (np.ndarray) Dataset to be transformed
        
        Outputs:
        returns (np.ndarray) Tranformed dataset.
        """
        
        pass
    
        
        
        
        
        
        
        
        
    
                
                
