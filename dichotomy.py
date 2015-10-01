import segmentation
import polinom
import math
EPSILON = segmentation.EPSILON

def f(x):
    return segmentation.f(x)

def binsearch(l, r):
    global dihLog
    sgn = f(l)
    if sgn==0:
        dihLog.append([l,r,l,0]);
        return l
    sgn = sgn/abs(sgn)
    
    while(r-l>EPSILON):
        x = l + (r-l)/2
        vv = f(x)
        v = vv/sgn
        if v!=0: v = v/abs(v)
        dihLog.append([l,r,x,vv,v]);
        
        if v>0:
            l = x
        else:
            r = x
            
    return l + (r-l)/2

def dichotomy(polignom, a, b):
    global dihLog
    dihLog = []
    points = segmentation.segmentationPoli(polignom,a,b);

    roots = [];
    for i in range(len(points)-1):
        x, y = points[i],points[i+1]
        dihLog.append([]);
        p = binsearch(x,y)
        if len(roots)==0:
            roots.append(p)
        elif abs(roots[-1]-p)>=EPSILON:
            roots.append(p)

    return roots

def printDihLog():
    global dihLog
    if len(dihLog)==0:
        print("dihLog is empty")
        return
    
    i = 0
    for l in dihLog:
        if len(l)==5:
            i += 1
            print("{0:>2} | ".format(i)+"{0[0]: .10f} | {0[1]: .10f} | {0[2]: .10f} | {0[4]: 3n} | {0[3]: .10f}".format(l))
        else:
            i = 0
            print("\nIt | {0:^13} | {1:^13} | {2:^13} | {4:^3} | {3:^16}".format("L","R","Xn","f(Xn)","L/R"))
    return

if __name__ == "__main__":
    print(dichotomy(polinom.formPolinom([1.0, -1.0, 2.0, math.pi, math.e]), -4.23423425, 3.265621616))
    printDihLog()
