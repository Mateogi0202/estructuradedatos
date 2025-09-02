class Usuario:
    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self.contraseña = contraseña
    
    def iniciarSesion(self, nombre: str, contraseña: str) -> str:
        if self.nombre == nombre and self.contraseña == contraseña:
            return f" Bienvenido {self.nombre}, sesión iniciada correctamente."
        else:
            return " Credenciales incorrectas."

class Administrador(Usuario):
    def __init__(self, nombre: str, contraseña: str, gestionUsuarios: str):
        super().__init__(nombre, contraseña)
        self.gestionUsuarios = gestionUsuarios

    def gestionarUsuarios(self) -> str:
        return f" El administrador {self.nombre} está gestionando usuarios: {self.gestionUsuarios}"

class Cliente(Usuario):
    def __init__(self, nombre: str, contraseña: str, realizarCompras: str):
        super().__init__(nombre, contraseña)
        self.realizarCompras = realizarCompras

    def realizarCompra(self) -> str:
        return f" El cliente {self.nombre} está realizando una compra: {self.realizarCompras}"

admin = Administrador("Carlos", "1234", "Agregar y eliminar usuarios")
cliente1 = Cliente("Ana", "abcd", "Laptop y celular")
print(admin.iniciarSesion("Carlos", "1234"))  
print(admin.gestionarUsuarios())

print(cliente1.iniciarSesion("Ana", "abcd"))  
print(cliente1.realizarCompra())

print(cliente1.iniciarSesion("Ana", "12345"))  

        
    
