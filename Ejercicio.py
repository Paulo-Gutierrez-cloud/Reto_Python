#Desafio de obtener todos los numeros primos de 1 a 250

# Hemos separado la logica en una funcion para poder probarla mas facil.

def es_primo(numero):
    """
    Funcion que determina si un numero es primo.
    Recibe: un numero entero.
    Devuelve: True si es primo, False si no lo es.
    """
    # Los numeros menores o iguales a 1 no son primos.
    if numero <= 1:
        return False
    
    # Verificamos si el numero tiene algun divisor aparte de 1 y el mismo.
    # Probamos dividiendo por todos los numeros desde 2 hasta el numero - 1.
    for i in range(2, numero):
        if (numero % i) == 0:
            # Si el resto de la division es 0, significa que es divisible.
            # Por lo tanto, NO es un numero primo.
            return False
            
    # Si pasamos todas las pruebas y no encontramos divisores, es primo.
    return True

if __name__ == "__main__":
    print("Iniciando busqueda de numeros primos...")
    
    # Abrimos (o creamos) el archivo 'results.txt' en modo escritura ('w').
    with open('results.txt', 'w') as archivo:
        
        # Iteramos a traves de los numeros del 1 al 250.
        for numero in range(1, 251):
            
            # Usamos nuestra nueva funcion para verificar si es primo.
            if es_primo(numero):
                print(f"Encontrado primo: {numero}")
                archivo.write(f"{numero}\n")

    print("Proceso terminado. Los resultados estan en 'results.txt'.")
