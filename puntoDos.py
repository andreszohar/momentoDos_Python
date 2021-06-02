Cesta = {}
n=int(input("Cuantos productos vas a comprar? ===>"))
for i in range(n):
    print('camisetas, pantalones, short, camisas, pantalonetas para hombres')
    print()
    clave= input('-introduccir el producto que deseas comprar  : ')
    print('ingrese el valor de la prenda')
    valor = int(input(clave+ '  :  '))
    Cesta[clave]= valor
    
total = 0
for null,precio in Cesta.items():
    total += precio

print(f"los productos son:  {Cesta}") 
print(f"El precio de la Compras es : {total}")