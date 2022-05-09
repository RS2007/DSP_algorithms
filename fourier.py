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
f = lambda x,N: np.sin(2*np.pi*x/N)


def IDFT(a):
    sizeA = len(a)
    omega = np.exp(-2*np.pi*1j/sizeA)
    matrix = [[(omega**(x*y)) for y in range(0,sizeA) ] for x in range(0,sizeA)]
    return np.matmul(np.linalg.inv(matrix),a)

print(IDFT([1,0,1,0]))
