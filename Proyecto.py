def inicio():
    print ("===============================================================")
    print("              BIENVENIDO A ELIZANA DESAYUNOS")
    print ("===============================================================")
    print("LISTA DE PRODUCTOS")
    print ("---------------------------------------------------------------")
    print ("1. Wraps")
    print ("2. Sandwiches")
    print ("3. Huevos")
    print ("4. Bebidas calientes")
    print ("5. Jugos de frutas")
    print ("6. Gaseosas y jugos embotellados")
    print ("7. Especiales")
    print ("---------------------------------------------------------------")
    n = int(input("Ingresa el numero del producto que deseas: "))
    print ("---------------------------------------------------------------")
    total=0
    acumcant=0
    if n==1 :
        print ("WRAPS")
        Wraps={}
        Wraps["1. Wrap doble queso pina albaca"]="$8.500"
        Wraps["2. Wrap de pollo arandano      "]="$9.500"
        Wraps["3. Wrap de pollo manzana       "]="$9.500"
        Wraps["4. Wrap queso pepperoni        "]="$8.500"
        Wraps["0. Regresar                    "]=""

        wraps_d = Wraps.items()

        for (x,y) in wraps_d:
            print(str(x)+"........"+str(y))
            
        a=int(input("Marca la opcion de wrap que deseas: "))
        
        if a==1:
            cant=int(input("¿Cuantas unidades desea? "))
            price=8500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("¿Cuantas unidades desea? "))
            price=9500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("¿Cuantas unidades desea? "))
            price=9500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("¿Cuantas unidades desea?: "))
            price=8500
            total=total+(cant*price)
            acumcant=acumcant+cant

        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
            a=int(input("Marca la opcion de wrap que deseas: "))
            
        print("Subtotal: $" + str(total))
        
    if n==2 :
        print ("SANDWICHES")
        Sandwich ={}
        Sandwich["1. Sandwich mortadela y queso"]="$2.500"
        Sandwich["2. Sandwich jamon y queso    "]="$2.500"
        Sandwich["3. Sandwich de pollo         "]="$4.500"
        Sandwich["4. Sandwich de cerdo         "]="$4.500"
        Sandwich["0. Regresar                  "]=""

        sandwiches = Sandwich.items()

        for (x,y) in sandwiches:
            print(str(x)+"........"+str(y))
            
        a=int(input("Marca la opcion de sandwich que deseas: "))
        
        if a==1:
            cant=int(input("¿Cuantas unidades desea? "))
            price=2500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("¿Cuantas unidades desea? "))
            price=2500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("¿Cuantas unidades desea? "))
            price=4500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("¿Cuantas unidades desea? "))
            price=4500
            total=total+(cant*price)
            acumcant=acumcant+cant

        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
                
            a=int(input("Marca la opcion de sandwich que deseas: "))
            
        print("Subtotal: $" + str(total))
        
    if n==3:
        print ("HUEVOS")
        Huev={}
        Huev["1. Huevo frito   "]="$1.000"
        Huev["2. Huevo revuelto"]="$1.000"
        Huev["3. Huevo perico  "]="$1.500"
        Huev["4. Huevo cocido  "]="$1.000"
        Huev["5. Huevo ranchero"]="$2.500"
        Huev["0. Regresar      "]=""

        huevos= Huev.items()

        for (x,y) in huevos:
            print(str(x)+"........"+str(y))
            
        a=int(input("Marca la opcion de huevos que deseas: "))
        
        if a==1:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1000
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1000
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1000
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==5:
            cant=int(input("¿Cuantas unidades desea? "))
            price=2500
            total=total+(cant*price)
            acumcant=acumcant+cant

        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
                
            a=int(input("Marca la opcion de huevos que deseas: "))
            
        print("Subtotal: $" + str(total))
        
    if n==4:
        print ("BEBIDAS CALIENTES")
        Bebi_cal={}
        Bebi_cal["1. Chocolate     "]="$1.500"
        Bebi_cal["2. Café con leche"]="$1.000"
        Bebi_cal["3. Agua de panela"]="$1.000"
        Bebi_cal["4. Tinto         "]="$700"
        Bebi_cal["5. Aromatica     "]="$700"
        Bebi_cal["6. Té verde      "]="$900"
        Bebi_cal["7. Té negro      "]="$900"
        Bebi_cal["0. Regresar      "]=""

        bebidas_calientes = Bebi_cal.items()

        for (x,y) in bebidas_calientes:
            print(str(x)+"........"+str(y))
            
        a=int(input("Marca la opcion de Bebidas calientes que deseas: "))
        
        if a==1:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1000
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1000
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("¿Cuantas unidades desea? "))
            price=700
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==5:
            cant=int(input("¿Cuantas unidades desea? "))
            price=700
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==6:
            cant=int(input("¿Cuantas unidades desea? "))
            price=900
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==7:
            cant=int(input("¿Cuantas unidades desea? "))
            price=900
            total=total+(cant*price)
            acumcant=acumcant+cant

        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
                
            a=int(input("Marca la opcion de bebidas calientes que deseas: "))
            
        print("Subtotal: $" + str(total))
        
    if n==5:
        print("JUGO DE FRUTAS")
        frutas={}
        frutas["1. Jugo de naranja  "] = "$2.500"
        frutas["2. Jugo de maracuya "] = "$3.500"
        frutas["3. Jugo de mandarina"] = "$2.500"
        frutas["4. Jugo de papaya   "] = "$3.500"
        frutas["0. Regresar         "] = ""

        jugo_frutas = frutas.items()

        for (x,y) in jugo_frutas:
            print(str(x)+"........"+str(y))
            
        a=int(input("Marca la opcion de jugo de frutas que deseas: "))
        
        if a==1:
            cant=int(input("¿Cuantas unidades desea? "))
            price=2500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("¿Cuantas unidades desea? "))
            price=3500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("¿Cuantas unidades desea? "))
            price=2500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("¿Cuantas unidades desea? "))
            price=3500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
            a=int(input("Marca la opcion de jugo de frutas que deseas: "))
        print("Subtotal: $" + str(total))
        
    if n==6:
        print ("GASEOSAS Y JUGOS EMBOTELLADOS")
        Gase_jug={}
        Gase_jug["1. Coca-Cola    "]="$1.500"
        Gase_jug["2. Cuatro       "]="$1.500"
        Gase_jug["3. Sprite       "]="$1.500"
        Gase_jug["4. Fanta naranja"]="$1.500"
        Gase_jug["5. Fanta uva    "]="$1.500"
        Gase_jug["6. Fanta manzana"]="$1.500"
        Gase_jug["7. Jugos Hit    "]="$1.500"
        Gase_jug["0. Regresar     "]=""

        gaseosas_jugos = Gase_jug.items()

        for (x,y) in gaseosas_jugos:
             print(str(x)+"........"+str(y))
        a=int(input("Marca la opcion de jugo de gaseosas y jugos embotellados que deseas: "))
        if a==1:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==5:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==6:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==7:
            cant=int(input("¿Cuantas unidades desea? "))
            price=1500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
            a=int(input("Marca la opcion de Jugo de frutas que deseas: "))
            
        print("Subtotal: $" + str(total))
    if n==7:
        print("ESPECIALES")
        Espe={}
        Espe["1. Caldo de costilla "]="$3.500"
        Espe["2. Caldo de pajarilla"]="$3.500"
        Espe["3. Tamal             "]="$3.000"
        Espe["4. Lechona           "]="$4.500"
        Espe["0. Regresar          "]=""

        especiales= Espe.items()

        for (x,y) in especiales:
            print(str(x)+"........"+str(y))
        a=int(input("Marca la opcion de Especiales que deseas: "))
        
        if a==1:
            cant=int(input("¿Cuantas unidades desea?: "))
            price=3500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==2:
            cant=int(input("Cuantas unidades desea?"))
            price=3500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==3:
            cant=int(input("Cuantas unidades desea?"))
            price=3000
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==4:
            cant=int(input("Cuantas unidades desea?"))
            price=4500
            total=total+(cant*price)
            acumcant=acumcant+cant
            
        elif a==0:
            return (inicio())
        
        else:
            print("Opcion invalida")
            for (x,y) in jugo_frutas:
                print(str(x)+"........"+str(y))
            a=int(input("Marca la opcion de gaseosas y jugos embotellados que deseas: "))
        print("Subtotal: $" + str(total))
        
    if n>7:
        print ("EL NÚMERO INGRESADO NO CORRESPONDE A NINGUN MENÚ.")
        return (inicio())
    if n<1:
        print ("EL NÚMERO INGRESADO NO CORRESPONDE A NINGUN MENÚ.")
        return (inicio())
    
    print("RESUMEN DE COMPRA")
    
    print("Cantidad de productos: " + str(acumcant))
    
    print("Total a pagar: $" + str(total))

inicio()



