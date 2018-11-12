productos={}
productos["Wraps"]=1
productos["Sandwiches"]=2
productos["Huevos"]=3
productos["Bebidas calientes"]=4
productos["Jugo de frutas"]=5
productos["Gaseosas y jugos embotellados"]=6
productos["Especiales"]=7
productos["Finalizar orden"]=9
menu=productos.items()
menu_p=productos.values()

    
Wraps={}
Wraps["1. Wrap doble queso pina albaca"]=8500
Wraps["2. Wrap de pollo arandano      "]=9500
Wraps["3. Wrap de pollo manzana       "]=9500
Wraps["4. Wrap queso pepperoni        "]=8500
Wraps["0. Regresar                    "]=0

wraps_d = Wraps.items()
wraps_p=Wraps.values()


Sandwich ={}
Sandwich["1. Sandwich mortadela y queso"]=2500
Sandwich["2. Sandwich jamon y queso    "]=2500
Sandwich["3. Sandwich de pollo         "]=4500
Sandwich["4. Sandwich de cerdo         "]=4500
Sandwich["0. Regresar                  "]=0
sandwiches = Sandwich.items()
sandwiches_p=Sandwich.values()


Huev={}
Huev["1. Huevo frito   "]=1000
Huev["2. Huevo revuelto"]=1000
Huev["3. Huevo perico  "]=1500
Huev["4. Huevo cocido  "]=1000
Huev["5. Huevo ranchero"]=2500
Huev["0. Regresar      "]=0
huevos= Huev.items()
huevos_p=Huev.values()


Bebi_cal={}
Bebi_cal["1. Chocolate     "]=1500
Bebi_cal["2. Cafe con leche"]=1000
Bebi_cal["3. Agua de panela"]=1000
Bebi_cal["4. Tinto         "]=700
Bebi_cal["5. Aromatica     "]=700
Bebi_cal["6. Te verde      "]=900
Bebi_cal["7. Te negro      "]=900
Bebi_cal["0. Regresar      "]=0
bebidas_calientes = Bebi_cal.items()
bebidas_p=Bebi_cal.values()

frutas={}
frutas["1. Jugo de naranja  "] = 2500
frutas["2. Jugo de maracuya "] = 3500
frutas["3. Jugo de mandarina"] = 2500
frutas["4. Jugo de papaya   "] = 3500
frutas["0. Regresar         "] = 0
jugo_frutas = frutas.items()
jugo_p=frutas.values()

Gase_jug={}
Gase_jug["1. Coca-Cola    "]=1500
Gase_jug["2. Cuatro       "]=1500
Gase_jug["3. Sprite       "]=1500
Gase_jug["4. Fanta naranja"]=1500
Gase_jug["5. Fanta uva    "]=1500
Gase_jug["6. Fanta manzana"]=1500
Gase_jug["7. Jugos Hit    "]=1500
Gase_jug["0. Regresar     "]=0
gaseosas_jugos = Gase_jug.items()
gaseosas_p=Gase_jug.values()

Espe={}
Espe["1. Caldo de costilla "]=3500
Espe["2. Caldo de pajarilla"]=3500
Espe["3. Tamal             "]=3000
Espe["4. Lechona           "]=4500
Espe["0. Regresar          "]=0
especiales= Espe.items()
especiales_p=Espe.values()


class Inicio():
    def __init__(self):
        self.a=menu
        self.prices=menu_p
        self.acumcant=0
        self.total=0
    def introduccion(self):
        print( "===============================================================")
        print( "              BIENVENIDO A ELIZANA DESAYUNOS                   ")
        print( "===============================================================")
        print( "LISTA DE PRODUCTOS")
        print( "===============================================================")

    def mostrar_inicio(self):
        self.a=menu
        for (x,y) in self.a:            
            print(str(y)+". "+str(x))
    def opcion(self):       
        while True:
            try:
                self.b=int(input("Ingresa el numero del producto que deseas: "))
                break
            except ValueError:
                print("El valor ingresado es invalido. Intentelo nuevamente") 
    def cantidad(self):
        while True:
            try:
                self.cant=int(input("Cuantas unidades deseas? "))
                break   
            except ValueError and IndexError:
                print("El valor ingresado es invalido. Intentelo nuevamente") 

    def cantacum(self):
        self.acumcant=self.acumcant+self.cant
        print("Hasta el momento tiene: " + str(self.acumcant) + " unidades.")

            
    def precios_productos(self):
        self.precios=[]   
        for i in self.prices:
            self.precios.append(i)  
        for j in self.precios:
            self.precio=self.precios[self.b]
        self.subtotal=(self.precio*self.cant)
        self.total=self.subtotal+self.total
    
    def cat(self):
        if self.b==1:
            self.a=wraps_d
            self.prices=wraps_p
            for (x,y) in self.a:            
                print(str(x)+"........."+"$" + str(y))
        elif self.b==2:
            self.a=sandwiches
            self.prices=sandwiches_p
            for (x,y) in self.a:            
                print(str(x)+"........."+"$" + str(y))
        elif self.b==3:
            self.a=huevos
            self.prices=huevos_p
            for (x,y) in self.a:            
                print(str(x)+"........."+"$" + str(y))
        elif self.b==4:
            self.a=bebidas_calientes
            self.prices=bebidas_p
            for (x,y) in self.a:            
                print(str(x)+"........."+"$" + str(y))
        elif self.b==5:
            self.a=jugo_frutas
            self.prices=jugo_p
            for (x,y) in self.a:            
                print(str(x)+"........."+"$" + str(y))
        elif self.b==6:
            self.a=gaseosas_jugos
            self.prices=gaseosas_p
            for (x,y) in self.a:            
                print(str(x)+"........."+"$" + str(y))
        elif self.b==7:
            self.a=especiales
            self.prices=especiales_p
        else:
            print("Total a pagar: "+"$ " + str(self.total))
            print("Cantidad de productos: " + str(self.acumcant))
            print("GRACIAS POR SU COMPRA")

    def sub_total(self):  
        print("$ " + str(self.subtotal))
            
p=Inicio()
p.introduccion()   
while True:        
    p.mostrar_inicio()
    p.opcion()   
    p.cat()        
    p.opcion()
    p.cantidad()
    p.precios_productos()
    p.sub_total()
    p.cantacum()
    









