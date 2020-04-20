i = 0
my_list = dict()
while i < 2:
    nombre = input("Dame el nombre de la moneda:      \n")
    cantidad = int(input("Cuantas monedas tienes?: \n"))
    precio = int(input("Cuanto vale tu moneda en USD$?:   \n"))
    final = cantidad * precio
    my_list[nombre]=final
    i+=1

print("\n")
for items in my_list:
     print (items)
