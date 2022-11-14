class pila:
    
    def __init__(self):
        self.cabeza = None
    
    def añadirR(self,nodo1,n):
        if nodo1 is not None:
            if self.añadirR(nodo1.puntero,n):
                nodo1.puntero = nodo(n)
        else:
            return True
            
        
    
    def añadir (self,dato):
        if self.cabeza is None:
            self.cabeza = nodo(dato)
        else:
            self.añadirR(self.cabeza,dato)
    
    def buscar(self,nodo1):
        if nodo1 is not None:
            print(nodo1.dato)
            self.buscar(nodo1.puntero)
    def Buscar(self):
        self.buscar(self.cabeza)
        
    def eliminarR(self,nodo1):
        if nodo1 is not None:
            if self.eliminarR(nodo1.puntero):   # 32
                nodo1.dato = None
                     # tengo que mandar mensaje al 123 que el 32 p esta vacio
            else:
                if nodo1.puntero.dato is None:
                    nodo1.puntero = None
        else:
            return True
    
    def eliminar(self):
        self.eliminarR(self.cabeza)
    
class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.puntero = None 

pilas = pila()
pilas.añadir(3)
pilas.añadir(6)
pilas.añadir(12)
pilas.añadir(123)
pilas.añadir(32)
#print(pilas.cabeza)
pilas.Buscar()
pilas.eliminar()
print("*----   se elimina el 32   ---------*")
pilas.Buscar()
print("----------   se elimina el 123    --------------")
pilas.eliminar()
pilas.Buscar()