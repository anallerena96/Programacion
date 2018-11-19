productos = []
productos.append((1," Wraps                        "))
productos.append((2," Sandwiches                   "))
productos.append((3," Huevos                       "))
productos.append((4," Bebidas calientes            "))
productos.append((5," Jugos de frutas              "))
productos.append((6," Gaseosas y jugos embotellados"))
productos.append((7," Especiales                   " ))
productos.append((8," Finalizar orden              "))


Wraps = []
Wraps.append ((1, "Wrap doble queso pina albaca",8500))
Wraps.append ((2, "Wrap de pollo arandano      ",9500))
Wraps.append ((3, "Wrap de pollo manzana       ",9500))
Wraps.append ((4, "Wrap de queso pepperoni     ",8500))

Sandwich = []
Sandwich.append((1,"Sandwich mortadela y queso  ",2500))
Sandwich.append((2,"Sandwich jamon y queso      ",2500))
Sandwich.append((3,"Sandwich de pollo           ",4500))
Sandwich.append((4,"Sandwich de cerdo           ",4500))

Huev = []
Huev.append((1, "Huevo frito                 ",1000))
Huev.append((2, "Huevo revuelto              ",1000))
Huev.append((3, "Huevo perico                ",1500))
Huev.append((4, "Huevo cocido                ",1000))
Huev.append((5, "Huevo ranchero              ",2500))
 
Bebi_cal = []
Bebi_cal.append((1, "Chocolate                   ",1500))
Bebi_cal.append((2, "Cafe con leche              ",1000))
Bebi_cal.append((3, "Agua de panela              ",1000))
Bebi_cal.append((4, "Tinto                       ", 700))
Bebi_cal.append((5, "Aromatica                   ", 700))
Bebi_cal.append((6, "Te verde                    ", 900))
Bebi_cal.append((7, "Te negro                    ", 900))

frutas = []
frutas.append((1, "Jugo de naranja             ",2500))
frutas.append((2, "Jugo de maracuya            ",3500))
frutas.append((3, "Jugo de mandarina           ",2500))
frutas.append((4, "Jugo de papaya              ",3500))

Gase_jug = []
Gase_jug.append((1, "Coca-Cola                   ",1500))
Gase_jug.append((2, "Cuatro                      ",1500))
Gase_jug.append((3, "Sprite                      ",1500))
Gase_jug.append((4, "Fanta naranja               ",1500))
Gase_jug.append((5, "Fanta uva                   ",1500))
Gase_jug.append((6, "Fanta manzana               ",1500))
Gase_jug.append((7, "Jugos Hit                   ",1500))

Espe = []
Espe.append((1, "Caldo de costilla           ",3500))
Espe.append((2, "Caldo de pajarilla          ",3500))
Espe.append((3, "Tamal                       ",3000))
Espe.append((4, "Lechona                     ",4500))


class Inicio():
    def __init__(self):
        self.prod=productos
        self.subprod=productos
        self.name=productos
        self.subtotal=0
        self.factura=[]
        self.total=0
        self.acumcant=0


    def introduccion(self):
        print( "===============================================================")
        print( "              BIENVENIDO A ELIZANA DESAYUNOS                   ")
        print( "===============================================================")
        print( "LISTA DE PRODUCTOS")
        print( "_______________________________________________________________")
    
    def mostrar_productos(self):
        for (v,w) in self.prod:
            print(str(v)+". "+str(w))
    
    def opcion(self):
        while True:
            try:
                print("===============================================================")
                self.b=int(input("Ingresa el numero del producto que deseas: "))
                print("_______________________________________________________________")
                break
            except ValueError:
                print("El valor ingresado es invalido. Intentalo nuevamente") 			

class subclase(Inicio):
    
    def seleccion(self):
        if self.b==1:
            print("·····························WRAPS·····························")
            self.sub_prod=Wraps
            
        elif self.b==2:
            print("···························SANDWICHES··························")
            self.sub_prod=Sandwich
            
        elif self.b==3:
            print("····························HUEVOS·····························")
            self.sub_prod=Huev
            
        elif self.b==4:
            print("·······················BEBIDAS CALIENTES·······················")
            self.sub_prod=Bebi_cal
            
        elif self.b==5:
            print("························JUGOS DE FUTAS·························")
            self.sub_prod=frutas
            
        elif self.b==6:
            print("····················GASEOSAS Y JUGOS EMBOT·····················")
            self.sub_prod=Gase_jug
            
        elif self.b==7:
            print("··························ESPECIALES···························")
            self.sub_prod=Espe
            
        elif self.b==8:
            print("····························FACTURA····························")
            print("     _____________________________________________________")
            print("                       ELIZANA DESAYUNOS                  ")
            print("     _____________________________________________________")
            self.e=print("          Cantidad     "+"     Producto     "+"      Precio     ")
            
            for (x,y,z) in self.factura:
                 print("          "+str(x)+"        "+str(y)+"$ "+str(z))
                 
            print("     _____________________________________________________")
            print("        Total a pagar....................."+"$ " +str(self.total))
            print("        Cantidad de productos comprados........"+str(self.acumcant))
            print("                     GRACIAS POR SU COMPRA")
            print("")
            self.factura=[]
            self.total=0
            self.acumcant=0
            
        else: 
            None    


    def mostrar_sub(self):
        for (x,y,z) in self.sub_prod:
            print(str(x)+". "+str(y)+ "...." +"$ "+ str(z))

    def a_comprar(self):
        while True:
            try:
                print("·······························································")
                print("Para regresar al menú principal ingresa 0 (cero)")
                self.c=int(input("Ingresa el número de la opción que deseas: "))
                break
            except ValueError:
                print("El valor ingresado es invalido. Intentelo nuevamente")
        if self.c==0:
            print("")
    def cantidad(self):
        while True:
            try:
                if self.c!=0:
                    self.cant=int(input("¿Cuántas unidades deseas? "))
                    break
                else:
                    return
            except ValueError and IndexError:
                print("El valor ingresado es invalido. Intentalo nuevamente")

    
    def eleccion(self):
        for (x,y,z) in self.sub_prod:
            while x==self.c:
                self.name=y
                self.precio=z
                self.subtotal=self.precio*self.cant
                self.total=self.subtotal+self.total
                self.acumcant=self.cant+self.acumcant
                print("Subtotal:   $" + str(self.subtotal))
                print("Cantidad:    " + str(self.cant))
                self.factura.append((self.cant,self.name,self.subtotal))
                break

p=subclase()            
       
while True:
    p.introduccion()
    p.mostrar_productos()
    p.opcion()
    p.seleccion()
    p.mostrar_sub()
    p.a_comprar()
    p.cantidad()
    p.eleccion()


