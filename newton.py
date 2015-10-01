import segmentation
import polinom
import math

EPSILON = segmentation.EPSILON
ANS_EPSILON = EPSILON

def newton(poli, a, b):
    segments = segmentation.segmentationPoli(poli, a, b)
    
    roots = []
    dpoli = polinom.d(poli);

    global newLog
    newLog = [];

    for i in range(len(segments)):
        log = [[]]
        x = segments[i]
        nextx = x - 1
        while abs(x-nextx)>=ANS_EPSILON:
            dfx = polinom.polinomValue(dpoli,x)
            fx = polinom.polinomValue(poli,x)

            nextx = x - fx/dfx

            log.append([abs(x-nextx),nextx,fx])
            
            nextx, x = x, nextx

        if len(roots)>0:
            if abs(roots[-1]-x)<EPSILON:
                continue
            
        roots.append(x)
        newLog += log

    return roots;

def printNewLog():
    if len(newLog)==0:
        print("newLog is empty")
        return

    i = 0
    for l in newLog:
        if len(l)==3:
            i += 1
            print("{0:2} | {1[0]: .10f} | {1[1]: .10f} | {1[2]: .10f}".format(i,l))
        else:
            i = 0
            print("\nIt | {0:13} | {1:13} | {2:13}".format("dXn", "Xn", "f(Xn)"))
    return
                  
if __name__ == "__main__":
    print(newton(polinom.formPolinom([1.0, -1.0, 2.0, math.pi, math.e]), -4.23423425, 3.265621616))
    printNewLog();
