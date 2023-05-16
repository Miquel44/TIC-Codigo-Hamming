import numpy as np
import math

def generarCodis(n):
    ldc = []
    for a in [ str('{0:0'+str(n)+'b}').format(x) for x in range(2**n)]:
        a = " ".join(a).split()
        z = []
        for j in a:
            z.append(int(j))
        ldc.append(z)
    return np.matrix(ldc)

def longitudCodi(C):
    return C.shape[1]

def dimensioCodi(C):
    return math.log(C.shape[0], 10)/math.log(2, 10)

def distanciaMinima(C):
    dH = set()
    for u in C:
        for v in C:
            if not np.array_equal(u, v):
                dH.add(np.count_nonzero(np.bitwise_xor(u,v) == 1))
    return min(dH)

def capacitatCorrectora(C):
    d = distanciaMinima(C)
    return abs(d-1)/2


H = np.matrix([(1, 1, 0, 1, 1, 0, 0), (1, 1, 1, 0, 0, 1, 0), (1, 0, 1, 1, 0, 0, 1)]) 
C = np.matrix([
    (0, 0, 0, 0, 0, 0, 0), 
    (0, 0, 0, 1, 1, 0, 1),            
    (0, 0, 1, 0, 0, 1, 1),
    (0, 0, 1, 1, 1, 1, 0),
    (0, 1, 0, 0, 1, 1, 0),
    (0, 1, 0, 1, 0, 1, 1),
    (0, 1, 1, 0, 1, 0, 1),
    (0, 1, 1, 1, 0, 0, 0),
    (1, 0, 0, 0, 1, 1, 1),
    (1, 0, 0, 1, 0, 1, 0),
    (1, 0, 1, 0, 1, 0, 0),
    (1, 0, 1, 1, 0, 0, 1),
    (1, 1, 0, 0, 0, 0, 1),
    (1, 1, 0, 1, 1, 0, 0),
    (1, 1, 1, 0, 0, 1, 0),
    (1, 1, 1, 1, 1, 1, 1)])

sequenciaCodificar = np.matrix([(1, 1, 1, 0), (0, 0, 0, 1), (1, 1, 0, 1)])
sequenciaDescodificar = np.matrix([(1, 1, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 1, 1), (1, 1, 0, 1, 0, 0, 0)])

print('La meva matriu de control es: \n', H)
print('El meu codi es: \n', C)


def ParametresCodi(C):
    n=longitudCodi(C)
    k=dimensioCodi(C)
    d=distanciaMinima(C)
    t=capacitatCorrectora(C)
    return n,k,d,t
    raise NotImplementedError("Cal que implementis ParametresCodi")

parametres = ParametresCodi(C)
corrector = capacitatCorrectora(C)
print(parametres)
print(corrector)



def longitudCodiHamming(r):
    x= 2**r -1
    return x
    raise NotImplementedError("Cal que implementis longitudCodiHamming")

def dimensioCodiHamming(r):
    x=longitudCodiHamming(r)
    y=x-r
    return y
    raise NotImplementedError("Cal que implementis dimensioCodiHamming")

def distanciaCodiHamming():
    z=3
    return z
    raise NotImplementedError("Cal que implementis distanciaCodiHamming")

assert(longitudCodiHamming(3) == longitudCodi(C))
assert(dimensioCodiHamming(3) == dimensioCodi(C))
assert(distanciaCodiHamming() == distanciaMinima(C))
print("Tot correcte!")
