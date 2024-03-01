print("Bienvenido a la calculadora de IVA")
print("Permite extraer la cantidad de IVA y monto neto de un valor asignado")
print("Las opciones son \"neto\" y \"bruto\", para ello entregará el IVA correspondiente y el monto neto o bruto según corresponda")
print("Para salir, escribe \"salir\"")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese valor: $ ")
        if resultado.lower() == "salir":
            break
        iva = round(float(resultado))
        resultado = round(float(resultado))
        resultado1 = round(float(resultado))
        resultado2 = round(float(resultado))

    op = input("Ingresa tipo de valor: ")
    if op.lower() == "salir":
        break
    if op.lower() == "neto":
        resultado1 *= 0.19
        bruto = resultado * 1.19
    elif op.lower() == "bruto":
        resultado2 /= 1.19
        iva = resultado2 * 0.19
    else:
        print("Operación invalida")
        break

    if op.lower() == "neto":
        print(f"El IVA es $ {resultado1:,}")
        print(f"El monto bruto es $ {bruto:,}")
        break

    elif op.lower() == "bruto":
        print(f"El resultado neto es $ {resultado2:,}")
        print(f"El IVA es $ {iva:,}")
        break
