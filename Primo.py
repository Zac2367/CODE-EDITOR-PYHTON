inf = int(input("Dame el límite inferior: "))
sup = int(input("Dame el limite superior: "))
print(f"Los numeros primos entre {inf} y {sup} son: ")
for num in range(inf,sup+1):
    for i in range (2, num):
        if num%i == 0:
            break
        elif i == num-1:
            print(num)
