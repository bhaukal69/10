import matplotlib.pyplot as plt
import numpy as np

def local_reg(xo,X,Y,tau):
    xo=[1,xo]
    X=[[1,i]for i in X]
    X=np.asarray(X)
    xw=(X.T)*np.exp(np.sum((X-xo)**2,axis=1)/(-2*tau))
    beta=np.linalg.pinv(xw @ X) @ xw @ Y @ xo
    return beta

def draw(tau):
    pred=[local_reg(xo,X,Y,tau) for xo in domain]
    plt.plot(X,Y,'o',color='red')
    plt.plot(domain,pred,color='black')
    plt.show()

X=np.linspace(-3,3,num=1000)
domain=X
Y=np.log(np.abs(X**2-1)+ .5)

draw(10)
draw(0.1)
draw(0.00001)
