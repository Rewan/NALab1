EPSILON = 0.000001

def formPolinom(roots):
    if len(roots)==0: return []
    
    polinom = [0.0 for i in range(len(roots)+1)]
    
    for i in range(2**len(roots)):
        multy = 1.0
        t = 0
        for k in range(len(roots)):
            if i&(1<<k):
                multy *= (-roots[k])
                t += 1
        polinom[t] += multy
        
    return polinom


def polinomValue(polinom, x):
    sum = 0.0
    
    if len(polinom)==1: return polinom[0]
    
    for i in range(len(polinom)):
        sum += polinom[-i-1]*(x**i)
        
    return sum

def d(polinom):
    ans = []

    n = len(polinom)-1

    for i in range(n):
        ans.append(polinom[i]*(n-i))

    return ans

def setPoli(polignom):
    global poli
    poli = polignom

def f(x):
    global poli
    return polinomValue(poli,x)


if __name__ == "__main__":
    assert (formPolinom([]) == []), "Test: Empty list fail"
    assert (formPolinom([0.0]) == [1.0, 0.0]), "Test: Polinom (x - 0) fail"
    assert (formPolinom([2.5, -1.5]) == [1.0, -1.0, -3.75]), "Test: Polinom (x - 2.5)(x + 1.5) fail"
    
    assert (polinomValue([],1.0) == 0.0), "Test: Empty polinom fail"
    assert (polinomValue([3.0],6.0) == 3.0), "Test: f(x)=c fail"
    assert (polinomValue([4.0,2.0,1.0],2.0) == 21.0), "Test: f(x) = 4*x^2+2*x+1, f(2) fail"
    assert (polinomValue([2.0,-12.0,23.0,64.0],0.0) == 64.0), "Test: f(x) = x(g(x))+64, f(0) fail"

    assert (d([1., 3., 3., 1.]) == [3., 6., 3.]), "Test: d (x+1)^3 fail"
    assert (d([1., 0, 0, 1.]) == [3., 0., 0.]), "Test: d (x^4+1) fail"
