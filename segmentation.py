import polinom

SEGMENT_QUANTITY = 1000
EPSILON = polinom.EPSILON

def f(x):
    return polinom.f(x)

def segmentation(a, b):
    if a>b: a,b = b,a
    
    segmentLen = (b-a)/SEGMENT_QUANTITY
    
    sgn = f(a)
    if sgn!=0: sgn = sgn/abs(sgn)

    points = [a]

    for i in range(SEGMENT_QUANTITY+1):
        x = a + i*segmentLen

        xsgn = f(x)
        if abs(xsgn)<EPSILON: xsgn = 0
        if xsgn!=0: xsgn = xsgn/abs(xsgn)

        if sgn!=xsgn or xsgn == 0:
            points.append(x)
            
        sgn = xsgn

    return points

def segmentationPoli(polignom, a, b):
    polinom.setPoli(polignom)
    return segmentation(a,b)
