MENSAJE = """
    ---Bienvenido a la calculadora de IVA---

    Permite extraer la cantidad de IVA y monto neto de un valor asignado.

    Las opciones son \"neto\" y \"bruto\", para ello indica el IVA correspondiente y el monto neto o bruto según corresponda.

    Para ayuda, escriba \"Help\"
    Para salir, escribe \"salir\"
    """
print(MENSAJE)

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese valor: $ ")
        if resultado.lower() == "salir":
            print("Ha finalizado el programa")
            break
        elif resultado.lower() == "help":
            AYUDA = """
            Neto = Valor sin el IVA 
            Bruto = Valor total con el IVA
            
            Neto + Neto * 0.19 = Bruto
            """
            print(AYUDA)
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
        print("Operación inválida")
        break

    if op.lower() == "neto":
        print(f"El IVA es $ {resultado1:,}")
        print(f"El monto bruto es $ {bruto:,}")
        break

    elif op.lower() == "bruto":
        print(f"El resultado neto es $ {resultado2:,}")
        print(f"El IVA es $ {iva:,}")
        break
