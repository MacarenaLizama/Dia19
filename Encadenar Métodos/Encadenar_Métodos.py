class Usuario(): #creo la clase usuario

    def __init__(self, nombre , apellido):
        self.nombre= nombre
        self.apellido=apellido
        self.balance_cuenta=0
        self.cantidad=0
    
    def hacer_deposito(self,amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro (self,amount):
        self.balance_cuenta -= amount
        return self
    
    def mostrar_balance_usuario(self):
        print()
        print(f"Sr(a) {self.nombre} {self.apellido}, el balance de su cuenta es:$ {self.balance_cuenta}")
        print()
        return self

    def transfer_dinero(self, other_user, cantidad):
        self.cantidad=cantidad
        self.other_user=other_user
        self.balance_cuenta -= cantidad
        other_user.balance_cuenta += cantidad
        print()
        print(f"Se realizó una transferencia por ${self.cantidad}")
        print()
        print("Saldo actual de Sr(a)", self.nombre +" " + self.apellido , "es: $", self.balance_cuenta)
        print("Saldo actual de Sr(a)", other_user.nombre + " " + other_user.apellido, "es: $", other_user.balance_cuenta)
        print()


#instancias
persona1= Usuario("Juan", "Gutierrez")
persona2= Usuario("Claudia", "Ramirez")
persona3=Usuario ("Carlos", "Sanchez")

#depositos, retiros y balances
persona1.hacer_deposito(1500).hacer_deposito(1000).hacer_deposito(2150).hacer_retiro(980).mostrar_balance_usuario()
persona2.hacer_deposito(500).hacer_deposito(1143).hacer_retiro(100).hacer_retiro(381).mostrar_balance_usuario()
persona3.hacer_deposito(5487).hacer_retiro(150).hacer_retiro(500).hacer_retiro(333).mostrar_balance_usuario()




print("____________________________________________________________")
#transferencia

persona1.transfer_dinero(persona3, 300)






