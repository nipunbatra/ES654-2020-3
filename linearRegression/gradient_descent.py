class GD():
    def __init__(self, alpha=0.01, n_iter=100, n_restarts =1, learning_rate='constant', 
                batch_size='N'):
        '''
        Parameters
        1. Alpha (learning rate, default: 0.01)
        2. number of iterations (default: 100)
        3. Num_restarts (default: 1) We initialise \theta_i’s randomly `num_restarts` number of times. We choose the solution which gives the least cost amongst the different initialisation. 
        4. Learning rate function over time:
           ‘Constant’:  (default) learning rate does not change over time
           ‘Inverse’: learning rate is alpha/t where t is the iteration number
        
        5. Batch_size (default: N, setting to 1 converts to SGD, setting to some number between 1 and N converts to mini-batch GD

        '''
        pass
    
    def non_vectorized_gd():
        
        '''
        
        return theta
        ''' 
        
        pass
    
    def vectorised_gd():
        
        
        '''
        
        
        return theta
        '''
        
        pass
    
    def autograd_regression_gd():
        
        
        '''
        
        
        return theta
        '''
        
        return
        
        pass