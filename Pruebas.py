# Este archivo contiene las pruebas para nuestro script de numeros primos.
# Usaremos la libreria 'pytest' para ejecutar estas pruebas automaticamente.

# Primero, importamos la funcion que queremos probar desde nuestro archivo 'ejercicio.py'.
from Ejercicio import es_primo

def test_numeros_primos_basicos():
    """
    Prueba que verifica si detecta correctamente numeros primos conocidos.
    """
    
    assert es_primo(2) == True  # 2 es el primer numero primo
    assert es_primo(3) == True  # 3 es primo
    assert es_primo(5) == True  # 5 es primo
    assert es_primo(7) == True  # 7 es primo
    assert es_primo(11) == True # 11 es primo
    assert es_primo(13) == True # 13 es primo

def test_numeros_no_primos():
    """
    Prueba que verifica si detecta correctamente numeros que NO son primos.
    """
    assert es_primo(1) == False # 1 no es primo por definicion
    assert es_primo(4) == False # 4 es divisible por 2
    assert es_primo(6) == False # 6 es divisible por 2 y 3
    assert es_primo(8) == False # 8 es divisible por 2 y 4
    assert es_primo(9) == False # 9 es divisible por 3
    assert es_primo(10) == False # 10 es divisible por 2 y 5

def test_numeros_negativos_y_cero():
    """
    Prueba casos borde como numeros negativos y cero.
    """
    assert es_primo(0) == False
    assert es_primo(-1) == False
    assert es_primo(-5) == False

def test_numero_grande_primo():
    """
    Prueba con un numero primo un poco mas grande.
    """
    assert es_primo(241) == True # Sabemos que 241 es primo (esta en nuestro rango)

def test_numero_grande_no_primo():
    """
    Prueba con un numero no primo un poco mas grande.
    """
    assert es_primo(250) == False # 250 es divisible por muchos numeros
