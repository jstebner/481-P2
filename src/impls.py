import numpy as np
from math import exp

def load_proj_data():
    """returns X_train, y_train, X_test, y_test
    """
    train = np.loadtxt('../data/optdigits_train.dat')
    test = np.loadtxt('../data/optdigits_test.dat')
    trial = np.loadtxt('../data/optdigits_trial.dat')

    X_train = train[:,:-1]
    y_train = train[:,-1]
    
    X_test = test[:,:-1]
    y_test = test[:,-1]
    
    X_trial = trial[:,:-1]
    y_trial = trial[:,-1]
    
    return X_train, y_train, X_test, y_test, X_trial, y_trial

# REVIEW: funcs below
def mse(y_true, y_pred) -> float:
    n = len(y_true)
    

def sigmoid(x) -> float:
    return (1 + exp(-x))**-1

def sigmoid_deriv(x) -> float:
    return sigmoid(x) * (1 - sigmoid(x))

class Layer:
    def __init__(self, units, activation):
        self.units = units
        self.activ = activation


class Network:
    def __init__(self, layers, ):
        self.layers = layers

    def fit(self, X, y, ):
        pass
