from sympy import isprime
import time

def list_premier(max=31):
    """
    renvoie une liste de nombre premier inférieur à max
    """
    nombre=1
    premiers=[]
    if max < 2 : 
        return premiers
    else :
        while nombre < max :
            if isprime(nombre) :
                premiers.append(nombre)
            nombre = nombre +1
        return premiers    

def mersenner(p=10):
    """
    nombre de mersenner d'ordre p
    """
    return 2**p -1

if __name__ == '__main__' :

    debut = time.time()
    liste=list_premier(10000)

    for n in liste :
        M=mersenner(n)
        if isprime(M) :
            print(f'{n}  {M}')

    fin = time.time()

    print(f'temps de calcul {fin -debut} secondes') 