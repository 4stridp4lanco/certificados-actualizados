# Lista para almacenar los diccionarios de empleados
empleados = []

while True:
    print("\n--- SISTEMA DE NÓMINA ---")
    print("1. Registrar Empleado")
    print("2. Calcular Nómina")
    print("3. Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        # Opción 1: Captura de datos
        nombre = input("Nombre del empleado: ")
        salario_base = float(input("Salario Base: "))
        dias_trabajados = int(input("Días trabajados: "))
        
        # Guardar en un diccionario y agregar a la lista
        nuevo_empleado = {
            "nombre": nombre,
            "salario": salario_base,
            "dias": dias_trabajados
        }
        empleados.append(nuevo_empleado)
        print("Empleado registrado con éxito.")

    elif opcion == "2":
        # Opción 2: Lógica de cálculos
        if not empleados:
            print("No hay empleados registrados.")
        else:
            print("\n--- PAGOS DE NÓMINA ---")
            for e in empleados:
                # Pago proporcional a los días trabajados
                sueldo_mes = (e["salario"] / 30) * e["dias"]
                
                # Regla de Auxilio de Transporte
                if e["salario"] < 2600000:
                    auxilio = (160000 / 30) * e["dias"]
                else:
                    auxilio = 0
                
                # Descuento de salud y pensión (8% en total)
                descuento = sueldo_mes * 0.08
                
                # Total final
                neto_pagar = sueldo_mes - descuento + auxilio
                
                print(f"Empleado: {e['nombre']}")
                print(f"  Pago Neto: ${neto_pagar:,.0f}")
                print("-" * 25)

    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")
