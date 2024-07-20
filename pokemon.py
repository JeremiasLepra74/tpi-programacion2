class Pokemon:

    id_counter = 1 # Variable de clase para contar los IDs

    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.id = Pokemon.id_counter  # Asignar el ID actual
        Pokemon.id_counter += 1  # Incrementar el contador de ID

    def __str__(self):
        return f"Pokemon: nombre={self.nombre}, tipo={self.tipo}, vida={self.vida}, ataque={self.ataque}, id={self.id_counter}"    

    def gano(self):
        print(f"\n== {self.nombre} == GANO LA BATALLA.\n")  
