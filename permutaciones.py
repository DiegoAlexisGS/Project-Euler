
def inserta(x,lst,i):
    """
    Devuelve una nueva lista resultado de insertar x adentro de lst
    la posición i
    """
    return lst[:i]+[x]+lst[i:]

def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista contodas las permutaciones
    posibles que se pueden hacer con los elementos en c.
    """
    if len(c)==0:
        return[[]]
    return sum([inserta_multiple(c[0],s)
    for s in permuta(c[1:])],[])
