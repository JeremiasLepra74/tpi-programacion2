from datos import pokemon_disponibles

class Entrenador:

    def __init__(self, nombre, gimnasio, edad):
        self._nombre = nombre
        self._gimnasio = gimnasio
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
   
    @property
    def gimnasio(self):
        return self._gimnasio

    @gimnasio.setter
    def gimnasio(self, valor):
        self._gimnasio = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:  
            self._edad = valor
        else:
            raise ValueError("La edad no puede ser negativa.")
        
    def __str__(self):
        return f"Entrenador: nombre={self.nombre}, gimnasio={self.gimnasio}, edad={self.edad}"
        
def obtener_datos_entrenador():
        # Solicitar datos del entrenador mediante inputs
        nombre = input("Ingrese el nombre del entrenador: ")
        gimnasio = input("Ingrese el gimnasio del entrenador: ")
        edad = int(input("Ingrese la edad del entrenador: "))

        # Crear una instancia de Entrenador con los datos proporcionados
        entrenador = Entrenador(nombre=nombre, gimnasio=gimnasio, edad=edad)
        return entrenador

def elegir_pokemon():
    # Mostrar los Pokémon disponibles
    print("Estos son los Pokémon disponibles:\n")
    for i, poke in enumerate(pokemon_disponibles, start=1):
        print(f"{i} - {poke.nombre} (Tipo: {poke.tipo})")

    while True:
        opcion = int(input(""))
        if 1 <= opcion <= len(pokemon_disponibles):
            pokemon_elegido  = pokemon_disponibles[opcion - 1]
            print(f"Has eligio a {pokemon_elegido.nombre}")
            return pokemon_elegido 
        else:
            print("Opción no válida. Inténtalo de nuevo.")




        