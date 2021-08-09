

lista = list(range(0,100,1))

def linear_search(n,lista):
    e = bool
    for number in lista:
        if n == number: 
            print("{} es igual a {}".format(n, number))
            e = True
            break
        elif e == False : 
            print("Element not found")


def binari_search(n, lista):

    length = len(lista)

    if n > list[(length / 2 )] : 
        if n > (length / 4 ):
            print("yes")
        else: 
            print("No")
    else:   
        if n < (length / 2 ): 
            print("hola")


#linear_search(110,lista) 

binari_search(51, lista)
        
