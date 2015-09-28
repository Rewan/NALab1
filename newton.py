import segmentation
import polinom

EPSILON = segmentation.EPSILON

def newton(poli, a, b):
    segments = segmentation.segmentationPoli(poli, a, b)
    
    roots = []
    dpoli = polinom.d(poli);

    for i in range(len(segments)):
        x = segments[i]
        nextx = x - 1
        while abs(x-nextx)>=EPSILON:
            dfx = polinom.polinomValue(dpoli,x)
            fx = polinom.polinomValue(poli,x)

            nextx = x - fx/dfx
            nextx, x = x, nextx

        if len(roots)>0:
            if abs(roots[-1]-x)<EPSILON:
                continue

        roots.append(x)

    return roots;

if __name__ == "__main__":
    print(newton([1.0, 0.0, -1.0], -1.23423425, 3.265621616))
