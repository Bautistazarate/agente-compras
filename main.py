from crew import shopping_crew

def run():
    print("\nAgente de Compras Inteligente")
    print("==============================\n")

    producto = input("¿Qué querés comprar? ")
    presupuesto = input("¿Cuál es tu presupuesto máximo? ")

    print("\nAnalizando opciones, esto puede tardar 1-2 minutos...\n")

    resultado = shopping_crew.kickoff(inputs={
        "producto": producto,
        "presupuesto": presupuesto
    })

    print("\nINFORME FINAL DE COMPRA")
    print("========================")
    print(resultado)

    with open("informe_compra.txt", "w", encoding="utf-8") as f:
        f.write(str(resultado))

    print("\nInforme guardado en informe_compra.txt")

if __name__ == "__main__":
    run()