import numpy as np
from preprocessing.polynomial_features import PF



X = np.arange(50).reshape(10, 5)
poly = PF(2)
poly.fit_transform(X)

# Test all the functions defined in PF class
