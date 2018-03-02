import numpy as np
import sys

def getbeta(sigmar,sigmatheta,sigmaphi):
    if (sigmar<0):
        print "Negative sigmar not allowed"
        sys.exit()
    if (sigmatheta<0):
        print "Negative sigmatheta not allowed"
        sys.exit()
    if (sigmaphi<0):
        print "Negative sigmaphi not allowed"
        sys.exit()
    sigmat = np.sqrt(sigmatheta**2 + sigmaphi**2)
    return 1.0 - (sigmar/sigmat)**2
    
def sigmabeta(sigmar,sigmatheta,sigmaphi,esigmar,esigmatheta,esigmaphi):
    beta0 = getbeta(sigmar,sigmatheta,sigmaphi)
    beta = np.zeros(1000)
    for i in range(len(beta)):
        sr = sigmar + np.random.normal(0.0,esigmar)
        stheta = sigmatheta + np.random.normal(0.0,esigmatheta)
        sphi = sigmaphi + np.random.normal(0.0,esigmaphi)
        beta[i] = getbeta(sr,stheta,sphi)
        #print i, beta[i]
    return beta0, np.std(beta)
        
sigmar = 80.0
sigmatheta = 120.0
sigmaphi = 120.0
esigmar = 10.0
esigmatheta = 10.0
esigmaphi = 10.0
        
beta0, sigmabeta = sigmabeta(sigmar,sigmatheta,sigmaphi,esigmar,esigmatheta,esigmaphi)

print beta0, sigmabeta


    
        
    
