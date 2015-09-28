import segmentation

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
        v = f(x)/sgn
        if v!=0: v = v/abs(v)
        dihLog.append([l,r,x,v]);
        
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
    
    for l in dihLog:
        if len(l)>=4:
            print("L = {0[0]: .10f}, R = {0[1]: .10f}, C = {0[2]: .10f}, sgn(f(c))/sgn(f(l)) = {0[3]: n}".format(l))

if __name__ == "__main__":
    print(dichotomy([1.0, 0.0, -1.0], -1.23423425, 3.265621616))
    printDihLog()
