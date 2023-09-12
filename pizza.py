
def main():
    print("==== PIZZERIA DEVELOPER ====")

    deposit = float(input("Por favor ingrese saldo a depositar: "))
    balance = deposit
    total = 0
    ticket = []

## Menu ##
    margarita = 7.50
    rustica = 10.20
    charcutera = 12.60
    extras = {"Jalapeños": 0.80, "Anchoas": 0.50, "Salchichon": 1.25}
    extra_ing_chosen = None

    if deposit > 0:
        print(f"Su balance es de {balance}$.")
        print("Escoja la opcion de la pizza que desea ordenar a continuacion:")
        print(f"OPCION ==== NOMBRE ==== PRECIO \n1)   Margarita    {margarita}$\n2)   Rustica  {rustica}$\n3)   Charcutera  {charcutera}$ ")

        write_opt =int(input("Escriba la opcion de su preferencia aqui: "))

        if write_opt == 1:
            if balance - margarita >= 0:
                balance -= margarita
                total += margarita
                print(f"Ha escogido la pizza Margarita. Su saldo restante es: {balance}$")
                ticket.append(f"Margarita ----- {margarita}$")
                print("¿Desea añadir algun extra a su pizza?")
                print("1) Si \n2) No")
                write_opt_extra =int(input())
                
                if write_opt_extra == 1:
                    while write_opt_extra == 1:
                            print("Puede elegir entre las siguientes opciones:")
                            print("OPCION ==== NOMBRE ==== PRECIO \n1)   Jalapeños  {Jalapeños}$\n2)   Anchoas  {Anchoas}$\n3)   Salchichon  {Salchichon}$ ".format(Jalapeños = extras["Jalapeños"], Anchoas = extras["Anchoas"], Salchichon = extras["Salchichon"]))
                            write_opt =int(input("Escriba la opcion de su preferencia aqui: "))

                            if write_opt == 1:
                                extra_ing_chosen = extras.get("Jalapeños")
                                if balance - extra_ing_chosen >= 0:
                                    balance -= extra_ing_chosen
                                    total += extra_ing_chosen
                                    print("Ha añadido correctamente su extra de Jalapeño")
                                    print(f"Su saldo restante es: {balance}$")
                                    ticket.append("Jalapeño ----- {Jalapeños}$".format(Jalapeños = extras["Jalapeños"]))
                                    print("¿Desea añadir otro ingrediente extra a su pizza?")
                                    print("1) Si \n2) No")
                                    write_opt_extra =int(input())
                                else:
                                    print("Su saldo es insuficiente, por favor vuelva a realizar su orden")
                                    main()
                                    
                
                            elif write_opt == 2:
                                extra_ing_chosen = extras.get("Anchoas")
                                if balance - extra_ing_chosen >= 0:
                                    balance -= extra_ing_chosen
                                    total += extra_ing_chosen
                                    print("Ha añadido correctamente su extra de Anchoas")
                                    print(f"Su saldo restante es: {balance}$")
                                    ticket.append("Anchoas -----{Anchoas}$".format(Anchoas = extras["Anchoas"]))
                                    print("¿Desea añadir otro ingrediente extra a su pizza?")
                                    print("1) Si \n2) No")
                                    write_opt_extra =int(input())
                                else:
                                    print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                    main()
                                    
                            elif write_opt == 3:
                                extra_ing_chosen = extras.get("Salchichon")

                                if balance - extra_ing_chosen >= 0:
                                    balance -= extra_ing_chosen
                                    total += extra_ing_chosen
                                    print("Ha añadido correctamente su extra de Salchichon")
                                    print(f"Su saldo restante es: {balance}$")
                                    ticket.append("Salchichon ----- {Salchichon}$".format(Salchichon = extras["Salchichon"]))
                                    print("¿Desea añadir otro ingrediente extra a su pizza?")
                                    print("1) Si \n2) No")
                                    write_opt_extra =int(input())
                                else:
                                    print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                    main()
                            else:
                                print(f"\"{write_opt}\" no es una opcion valida")
                                print("Por favor vuelva a realiza su orden")
                                main()
                    else:
                        print("------ SU PEDIDO ------")
                        for i in ticket:
                            print(i)
                        print(f"Total ------ {total}$")
                        print("¿Es su pedido correcto?\n 1) SI \n 2) NO")
                        write_opt = int(input())
                        if write_opt == 1:
                            print("Su orden ha sido procesada correctamente.")
                        else: 
                            print("Orden no confirmada. Vuelva a realizar su orden")
                            main()

                

            else:
                print("Su saldo no es suficiente, por favor agregue mas saldo a su balance.")
                main()


        elif write_opt == 2:
            if balance - rustica >=0:
                balance -= rustica
                total += rustica
                print(f"Ha escogido la pizza Rustica. Su saldo restante es: {balance}$")
                ticket.append(f"Rustica ----- {rustica}$")
                print("¿Desea añadir algun extra a su pizza?")
                print("1) Si \n2) No")
                write_opt_extra =int(input())

                if write_opt_extra == 1:
                    while write_opt_extra == 1:
                        print("Puede elegir entre las siguientes opciones:")
                        print("OPCION ==== NOMBRE ==== PRECIO \n1)   Jalapeños  {Jalapeños}$\n2)   Anchoas  {Anchoas}$\n3)   Salchichon  {Salchichon}$ ".format(Jalapeños = extras["Jalapeños"], Anchoas = extras["Anchoas"], Salchichon = extras["Salchichon"]))
                        write_opt =int(input("Escriba la opcion de su preferencia aqui: "))
                
                        if write_opt == 1:
                            extra_ing_chosen = extras.get("Jalapeños")
                            if balance - extra_ing_chosen >= 0:
                                balance -=extra_ing_chosen
                                total += extra_ing_chosen
                                print("Ha añadido correctamente su extra de Jalapeño")
                                print(f"Su saldo restante es: {balance}$")
                                ticket.append("Jalapeño ----- {Jalapeños}$".format(Jalapeños = extras["Jalapeños"]))
                                print("¿Desea añadir otro ingrediente extra a su pizza?")
                                print("1) Si \n2) No")
                                write_opt_extra =int(input())
                            else:
                                print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                main()

                        elif write_opt == 2:
                            extra_ing_chosen = extras.get("Anchoas")
                            if balance - extra_ing_chosen >= 0:
                                balance -= extra_ing_chosen
                                total += extra_ing_chosen
                                print("Ha añadido correctamente su extra de Anchoas")
                                print(f"Su saldo restante es: {balance}$")
                                ticket.append("Anchoas -----{Anchoas}$".format(Anchoas = extras["Anchoas"]))
                                print("¿Desea añadir otro ingrediente extra a su pizza?")
                                print("1) Si \n2) No")
                                write_opt_extra =int(input())
                            else:
                                print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                main()
                        elif write_opt == 3:
                            extra_ing_chosen = extras.get("Salchichon")
                            if balance - extra_ing_chosen >= 0:
                                balance -= extra_ing_chosen
                                total += extra_ing_chosen
                                print("Ha añadido correctamente su extra de Salchichon")
                                print(f"Su saldo restante es: {balance}$")
                                ticket.append("Salchichon ----- {Salchichon}$".format(Salchichon = extras["Salchichon"]))
                                print("¿Desea añadir otro ingrediente extra a su pizza?")
                                print("1) Si \n2) No")
                                write_opt_extra =int(input())
                            else:
                                print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                main()
                        else:
                            print(f"\"{write_opt}\" no es una opcion valida")
                            print("Por favor vuelva a realiza su orden")
                            main()
                    else:
                        print("------ SU PEDIDO ------")
                        for i in ticket:
                            print(i)
                        print(f"Total ------ {total}$")
                        print("¿Es su pedido correcto?\n 1) SI \n 2) NO")
                        write_opt = int(input())
                        if write_opt == 1:
                            print("Su orden ha sido procesada correctamente.")
                        else: 
                            print("Orden no confirmada. Vuelva a realizar su orden")
                            main()
                    
            else:
                print("Su saldo no es suficiente, por favor agregue mas saldo a su balance.")
                main()


        elif write_opt == 3:
            if balance - charcutera >= 0:
                balance -= charcutera
                total += charcutera
                print(f"Ha escogido la pizza Charcutera. Su saldo restante es: {balance}$")
                ticket.append(f"Charcutera ----- {charcutera}$")
                print("¿Desea añadir algun extra a su pizza?")
                print("1) Si \n2) No")
                write_opt_extra =int(input())
                if write_opt_extra == 1:
                    while write_opt_extra == 1:
                        print("OPCION ==== NOMBRE ==== PRECIO \n1)   Jalapeños  {Jalapeños}$\n2)   Anchoas  {Anchoas}$\n3)   Salchichon  {Salchichon}$ ".format(Jalapeños = extras["Jalapeños"], Anchoas = extras["Anchoas"], Salchichon = extras["Salchichon"]))
                        write_opt =int(input("Escriba la opcion de su preferencia aqui: "))
                
                        if write_opt == 1:
                            extra_ing_chosen = extras.get("Jalapeños")
                            if balance - extra_ing_chosen >= 0:
                                balance -=extra_ing_chosen
                                total += extra_ing_chosen
                                print("Ha añadido correctamente su extra de Jalapeño")
                                print(f"Su saldo restante es: {balance}$")
                                ticket.append("Jalapeño ----- {Jalapeños}$".format(Jalapeños = extras["Jalapeños"]))
                                print("¿Desea añadir otro ingrediente extra a su pizza?")
                                print("1) Si \n2) No")
                                write_opt_extra =int(input())
                            else:
                                print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                main()

                        elif write_opt == 2:
                            extra_ing_chosen = extras.get("Anchoas")
                            if balance - extra_ing_chosen >= 0:
                                balance -= extra_ing_chosen
                                total += extra_ing_chosen
                                print("Ha añadido correctamente su extra de Anchoas")
                                print(f"Su saldo restante es: {balance}$")
                                ticket.append("Anchoas -----{Anchoas}$".format(Anchoas = extras["Anchoas"]))
                                print("¿Desea añadir otro ingrediente extra a su pizza?")
                                print("1) Si \n2) No")
                                write_opt_extra =int(input())
                            else:
                                print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                main()
                        elif write_opt == 3:
                            extra_ing_chosen = extras.get("Salchichon")
                            if balance - extra_ing_chosen >= 0:
                                balance -= extra_ing_chosen
                                total += extra_ing_chosen
                                print("Ha añadido correctamente su extra de Salchichon")
                                print(f"Su saldo restante es: {balance}$")
                                ticket.append("Salchichon ----- {Salchichon}$".format(Salchichon = extras["Salchichon"]))
                                print("¿Desea añadir otro ingrediente extra a su pizza?")
                                print("1) Si \n2) No")
                                write_opt_extra =int(input())
                            else:
                                print("Su saldo es insuficiente, por favor vuelva a realiza su orden")
                                main()
                        else:
                            print(f"\"{write_opt}\" no es una opcion valida")
                            print("Por favor vuelva a realiza su orden")
                            main()
                    else:
                        print("------ SU PEDIDO ------")
                        for i in ticket:
                            print(i)
                        print(f"Total ------ {total}$")
                        print("¿Es su pedido correcto?\n 1) SI \n 2) NO")
                        write_opt = int(input())
                        if write_opt == 1:
                            print("Su orden ha sido procesada correctamente.")
                        else: 
                            print("Orden no confirmada. Vuelva a realizar su orden")
                            main()
            else:
                print("Su saldo no es suficiente, por favor agregue mas saldo a su balance.")
                main()
                
        else:
            print(f"\"{write_opt}\" no es una opcion valida.")
            print("Por favor vuelva a realiza su orden")
            main()


    else:
        print("Por favor ingrese un numero valido o mayor que 0")
        main()

main()


                    