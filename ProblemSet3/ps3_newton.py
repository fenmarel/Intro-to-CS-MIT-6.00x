# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    result = 0
    while i < len(poly):
        result += poly[i] * x**i
        i += 1
    return float(result)
 



# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    #f(x)=ax**b is f?(x)=abx**b?1
    if len(poly) <= 1:
        return [0.0]
    result = []
    i = 1
    while i < len(poly):
        result.append(float(poly[i] * i))
        i += 1
    return result




# Problem 3: Newton's Method

def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    global runcount
    runcount = 0
    def root(poly, x_0, epsilon):
        global runcount
        if abs(evaluatePoly(poly, x_0)) < epsilon:
            return [x_0, runcount]
        runcount += 1
        return root(poly, (x_0-(evaluatePoly(poly, x_0)/evaluatePoly(computeDeriv(poly), x_0))), epsilon)
    return root(poly, x_0, epsilon)
    