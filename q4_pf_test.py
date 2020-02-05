import numpy as np
from preprocessing.polynomial_features import PolynomialFeatures



X = np.arange(6).reshape(3, 2)
poly = PolynomialFeatures(2)
assert((poly.transform(X) == np.array([[ 1.,  0.,  1.,  0.,  0.,  1.],[ 1.,  2.,  3.,  4.,  6.,  9.], [ 1.,  4.,  5., 16., 20., 25.]])).all())
