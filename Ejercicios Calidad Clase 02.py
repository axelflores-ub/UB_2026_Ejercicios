# Ejercicio 1
def calcular_area(base: float, altura: float) -> float:
    res = base * altura
    print(res)
    return res


# Ejercicio 2
def conectar():
    raise ConnectionError("No se pudo establecer la conexión")


try:
    conectar()
except ConnectionError as error:
    print(f"Error de conexión: {error}")


# Ejercicio 3
def mostrar_usuario(nombre: str) -> None:
    print(nombre)
    print("-------")


mostrar_usuario("User A")
mostrar_usuario("User B")


# Ejercicio 4
def suma(a: int, b: int) -> int:
    return a + b


# Ejercicio 5
class MiClase:
    def __init__(self, n: int):
        self.n = n


# Ejercicio 6
x = 10 + 5 * 2 / (1 + 1)


# Ejercicio 7
def obtener_inicial_dia(dia: int) -> str:
    dias = {
        1: "L",
        2: "M",
        3: "X",
        4: "J",
        5: "V",
        6: "S",
        7: "D"
    }
    return dias.get(dia, "Día inválido")


# Ejercicio 8
def login(user: str, password: str, admin: bool) -> None:
    if not user:
        print("Falta el usuario")
        return

    if not password:
        print("Falta la contraseña")
        return

    if not admin:
        print("No tiene permisos de administrador")
        return

    print("Login exitoso")


# Ejercicio 9
def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18


# Ejercicio 10
import os

api_key = os.getenv("API_KEY")


# Ejercicio 11
db = os.getenv("DB_URL")


# Ejercicio 12
debug = os.getenv("DEBUG", "False").lower() == "true"
