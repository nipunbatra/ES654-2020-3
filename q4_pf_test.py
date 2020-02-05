import numpy as np
from preprocessing.polynomial_features import PolynomialFeatures



X = np.arange(50).reshape(10, 5)
poly = PolynomialFeatures(2)
poly.transform(X)
