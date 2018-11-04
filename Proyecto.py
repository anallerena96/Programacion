print("BIENVENIDO!")
print("PRODUCTOS")
print("JUGO DE FRUTAS")
frutas={}
frutas["1. Jugo de naranja"] = 2500 
frutas["2. Jugo de maracuya"] = 3500
frutas["3. Jugo de mandarina"] = 2500
frutas["4. Jugo de papaya"] = 3500
jugo_frutas=frutas.items()
for (x,y) in jugo_frutas:
    print(str(x)+"........"+str(y))
    
print("BEBIDAS CALIENTES")
cal={}
cal["1. Tinto "] = 1600 
cal["2. Capuccino"] = 2500
cal["3. Espresso"] = 1300
cal["4. Chocolate"] = 3500
calientes=cal.items()
for (x,y) in calientes:
    print(str(x)+"........"+str(y))


print("SANDWICHES")
sand={}
sand["1. Sandwich de jamon y queso"] = 3500 
sand["2. Sandwich de pavo"] = 6000
sand["3. Sandwich de pollo"] = 4500
sand["4. Sandwich de pollo y jamon"] = 5000
sandwiches=sand.items()
for (x,y) in sandwiches:
    print(str(x)+"........"+str(y))
