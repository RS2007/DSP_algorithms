import numpy as np
def DFTwithoutFFT(a):
    N = len(a)
    result = np.zeros(N)+np.zeros(N)*1j
    nthRoot = np.exp(-2*np.pi*1j/N) 
    for i in range(0,N):
        for k in range(0,N):
            result[i] = result[i]+(nthRoot**(i*k))*a[k]
    return np.fromiter(map(returnZeroIfSmall,result),np.complex128)

def returnZeroIfSmall(n):
    print(n.real,n.imag)
    if(abs(n.real)<1e-10):
        n = 0+1j*n.imag
    if(abs(n.imag)<1e-10):
        n = n.real+0j 
    return n 

def FFT(a):
    return "hello"

a = [1,-1,2,2,4,2]
print(DFTwithoutFFT(a))
