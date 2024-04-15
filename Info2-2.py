def verificar_rango_vlan(id_vlan):
    id_vlan = int(id_vlan)
    if 1 <= id_vlan <= 1005:
        return "Vlan de rango Normal"
    elif 1006 <= id_vlan <= 4095:
        return "Vlan de Rango Extendido"
    else:
        return "Vlan ingresado es desconocido"


def main():
    id_vlan = input("Introduce el ID de la Vlan: ")
    resultado = verificar_rango_vlan(id_vlan)
    print(resultado)


if __name__ == "__main__":
    main()