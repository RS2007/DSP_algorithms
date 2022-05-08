import numpy as np

def convolveMe(a,b):
    """
        a: array
        b: array
        Input two arrays to find the convolution between them
        Disadvantage: in case of shifted indexes, you will have to manually find the base(or 0 index) of the convolved array
    """ 
    sizeA = len(a)
    sizeB = len(b)
    ans = np.zeros(sizeA+sizeB-1)
    for i in range(0,sizeA+sizeB-1):
        for j in range(0,sizeA):
            if(i-j>=0 and i-j<sizeB): ans[i] = ans[i] + b[i-j]*a[j]
        
    return ans



def make2Darray(a,b):
    """
        a: array
        b: array
        To get the 2D matrix for the tabular method, just print this result to get the table without the laborious process of multiplication
    """
    k = np.zeros((len(b),len(a)))
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            k[j][i] = a[i]*b[j]
    return k

def getConvolutionFrom2DArray(a):
    """
        a: output of make2Darray
        To find the convolution for two arrays from the 2D array
        Usage: getConvolutionFrom2DArray(make2Darray(a,b)) where a and b are the signal sample array
    """
    [rows,columns] = a.shape
    b = np.zeros(rows+columns-1)
    for i in range(0,rows+columns-1):
        for j in range(0,rows):
            for k in range(0,columns):
                if(j+k == i): 
                    b[i] = b[i] + a[j][k]
    return b 

def getBase(a,i,j):
    """
        a: output of make2Darray
        i: base(0-index) of the first signal array
        j: base(0-index) of the second signal array
        returns: 0-index of convolved array
        To find the base(0-index) of the convolved array
        Usage: getConvolutionFrom2DArray(make2Darray(a,b),i,j)
    """
    return i+j

def circularConvolve(a,b):
    N = max(len(a),len(b))
    sizeA = len(a)
    sizeB = len(b)
    ## padding
    while(len(a)<N):
        a[sizeA] = 0
        sizeA+=1 
    while(len(b)<N):
        b[sizeB] = 0
        sizeB+=1
    ## list comprehension magic
    matrix1 = [[a[k-i] for i in range(0,len(a))] for k in range(0,len(a))]
    print(matrix1)
    print(np.matmul(matrix1,[[b[i]] for i in range(0,len(b))])) # pyright: reportGeneralTypeIssues=false 

    return "circle"
a = [-1,2,0,1]
b = [3,1,0,-1]
c = [1,2,3,4]
d = [2,1,2,1]
e = [1,2,3,4]

print(circularConvolve(d,e))

print(convolveMe(a,b))
print(getConvolutionFrom2DArray(make2Darray(a,b)))
print(getBase(make2Darray(a,b),1,2))
