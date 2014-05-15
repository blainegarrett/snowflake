#######
# Similarity and distance calcs for binary and non binary asymetric data
# For more info see: http://www-users.cs.umn.edu/~kumar/dmbook/dmslides/chap2_data.pdf
########


'''
Similarity notes
Given similarity method **s** and binary vectors **p**, **q**
* Max similary = 1 only if p == q
* Similarity is symetric i.e. s(p, q) == s(q, p)
'''

import math

LENGTH_ERROR = 'Size of tuple arguments must be the same'

def dot_product(v1, v2):
    # TODO: Move to vector module
    assert len(v1) == len(v1), LENGTH_ERROR

    dot_prod = 0
    for i in xrange(0, len(v1)):
        dot_prod += v1[i] * v2[i]
    return dot_prod
    
def _calc_matrix(x, y):
    f11 = 0
    f00 = 0
    f01 = 0
    f10 = 0
    
    assert len(x) == len(y), LENGTH_ERROR
    
    for i in xrange(0, len(x)):
        if x[i] and y[i]:
            f11 += 1
        elif x[i]:
            f10 += 1
        elif y[i]:
            f01 += 1
        else:
            f00 += 1
    return float(f11), float(f00), float(f10), float(f01)
    
def jaccard_coefficient(x, y):
    # Calculate Jaccard Similarity Coefficient of 2 lists of binary data
    # J = Number of AND matches / number of OR (not-both-zero) attribute values
    f11, f00, f10, f01 = _calc_matrix(x, y)
    j = f11/(f01 + f10 + f11)
    return j


def jaccard_distance(x, y):
    # Calculate the "distance" between the two binary sets
    f11, f00, f10, f01 = _calc_matrix(x, y)
    return (f01 + f10) / (f01 + f10 + f11)


def smc(x, y):
    # Calculate Simple Matching Coefficient of 2 lists of binary data
    # smc = # of matching attribute values / number of attributes
    f11, f00, f10, f01 = _calc_matrix(x, y)
    return (f11 + f00)/(f01 + f10 + f11 + f00)


def cosine_similarity(x, y):
    # Good for comparing 2 very sparse sets (document similarity)
    # Ignores 0-0 matches like jaccard but also non-binary data
    # dotproduct(x, y) / len(vector(x)) * len(vector(y))
    
    dot_prod = 0
    vlenx = 0
    vleny = 0

    assert len(x) == len(y), LENGTH_ERROR

    dot_prod = dot_product(x, y)

    for i in xrange(0, len(x)):
        vlenx += x[i] * x[i]

    for i in xrange(0, len(y)):
        vleny += y[i] * y[i]
        
    vlenx = math.sqrt(vlenx)
    vleny = math.sqrt(vleny)

    return float(dot_prod) / float((vleny * vlenx))    

def tantimoto_coefficient(x, y):
    # aka Extended Jaccard
    # Good for continuous or count data - reduces to jaccard for binary data
    
    vlenx = 0
    vleny = 0
    dot_prod = dot_product(x, y)

    for i in xrange(0, len(x)):
        vlenx += x[i] * x[i]

    for i in xrange(0, len(y)):
        vleny += y[i] * y[i]
    
    return float(dot_prod) / float(((vlenx * vlenx) + (vleny *  vleny) - dot_prod))

def mean(v):
    x = 0
    n = len(v)
    for i in xrange(0, n):
        x += v[i]
    return float(x)/float(n)
    
def standard_deviation(v):
    meanv = mean(v)

    sumx = 0
    n = len(v)
    for i in xrange(0, n):
        j = (v[i] - meanv) * (v[i] - meanv) # Square so it is positive
        sumx += j

    sumx = float(sumx) / float(n)
    return math.sqrt(sumx)

def covarience(x, y):
    meanx = mean(x)
    meany = mean(y)
    sumx = 0
    n = len(x)
    for i in xrange(0, n):
        j =  (x[i] - meanx) * (y[i] - meany)
        sumx += j

    sumx = float(sumx) / float(n)

    return sumx
    
    
def correlation(x, y):
    # the linear relationship between objects
    # x, y are standardized by taking average
    # corr(x,y) = covariance(x,y)/std(x) * std(y)
    # Always in the range of [-1:1]

    return covarience(x, y)/(standard_deviation(x) *  standard_deviation(y))


x = (1,0,0,0,0,0,0,0,0,0)
y = (0,0,0,0,0,0,1,0,0,1)

x1 = (3,2,0,5,0,0,0,2,0,0)
y1 = (1,0,0,0,0,0,0,1,0,2)


x2 = (-3, 6, 0, 3, -6)
y2 = (1, -2, 0, -1, 2)

x3 = (3, 6, 0, 3, 6)
y3 = (1, 2, 0, 1, 2)

v = (2, 4, 4, 4, 5, 5, 7, 9)

'''
print 'Similarities'
print jaccard_coefficient(x, y)
print smc(x, y)
print tantimoto_coefficient(x, y) # Should be the same to jaccard since binary data

print 'Non Binary Data'
print cosine_similarity(x1, y1)
print tantimoto_coefficient(x1, y1)


print 'Distances'
print jaccard_distance(x, y)
'''

#print mean(v)
#print standard_deviation(v)
#print covarience(x, y)
#print 'Correlation'
#print standard_deviation(x3)
print mean(y3)
print standard_deviation(y3)

print correlation(x2, y2)
print correlation(x3, y3)