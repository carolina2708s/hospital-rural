
pacientes = []

opcion = 0

while opcion != 3:

    print("\n===== HOSPITAL DE CAMPO =====")
    print("1. Ingresar paciente")
    print("2. Mostrar pacientes")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            if len(pacientes) < 10:

                print("\n--- INGRESO DE PACIENTE ---")

                nombre = input("Nombre completo: ")
                rut = input("RUT: ")
                enfermedad = input("Enfermedad: ")

                try:
                    edad = int(input("Edad: "))

                    if nombre.strip() == "" or rut.strip() == "" or enfermedad.strip() == "":
                        print("Error: debe completar todos los datos.")

                    elif edad < 0:
                        print("Error: la edad no puede ser negativa.")

                    else:
                        paciente = {
                            "nombre": nombre,
                            "rut": rut,
                            "edad": edad,
                            "enfermedad": enfermedad
                        }

                        pacientes.append(paciente)

                        print("Paciente ingresado correctamente.")

                except ValueError:
                    print("Error: ingrese una edad válida.")

            else:
                print("Se alcanzó el límite de 10 pacientes.")

        elif opcion == 2:

            print("\n--- PACIENTES REGISTRADOS ---")

            if len(pacientes) == 0:
                print("No hay pacientes registrados.")

            else:
                for paciente in pacientes:
                    print("--------------------------")
                    print("Nombre:", paciente["nombre"])
                    print("RUT:", paciente["rut"])
                    print("Edad:", paciente["edad"])
                    print("Enfermedad:", paciente["enfermedad"])

                print("Total:", len(pacientes), "pacientes")

        elif opcion == 3:
            print("Cerrando el sistema...")

        else:
            print("Opción incorrecta.")

    except ValueError:
        print("Error: debe ingresar una opción numérica.")
