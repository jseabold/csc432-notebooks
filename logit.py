import numpy as np

def logit_func(x):
    return np.exp(x)/(1+np.exp(x))

def logit_loglikelihood(beta, y, X):
    q = 2*y - 1
    return -np.sum(np.log(logit_func(q*np.dot(X,beta))))

def logit_score(beta, y, X):
    q = 2*y - 1
    L = logit_func(np.dot(X, beta))
    return np.dot(y - L, X)
