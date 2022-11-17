print(
    '''
    ********** CALCULATOR IN PYTHON **********
    
    Seleccione por favor la operación a realizar
    
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    ''')

oper = int(input("Ingrese una opción (1/2/3/4): "))
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

if oper == 1:
    final = sum(x,y)
    print (f"La suma de {x} y {y} es: {final}")
elif oper == 2:
    final = x - y
    print (f"La resta de {x} y {y} es: {final}")
elif oper == 3:
    final = x * y
    print (f"La multlipicación de {x} y {y} es: {final}")
else:
    final = x / y
    print (f"La división de {x} y {y} es: {final}")
    