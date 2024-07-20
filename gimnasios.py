class Gimnasios:

    def __init__(self, nombre, region, ciudad):
        self.nombre = nombre
        self.region = region
        self.ciudad = ciudad
        
    def __str__(self):
        return f"Gimnasio: nombre={self.nombre}, region={self.region}, ciudad={self.ciudad}"