import pokemon
import gimnasios

p1 = pokemon.Pokemon(nombre="Pikachu", tipo="electrico", vida=100, ataque=35)
p2 = pokemon.Pokemon(nombre="Bulbasaur", tipo="planta", vida=100, ataque=35)
p3 = pokemon.Pokemon(nombre="Charmander", tipo="fuego", vida=100, ataque=35)
p4 = pokemon.Pokemon(nombre="Squirtle", tipo="agua", vida=100, ataque=35)
p5 = pokemon.Pokemon(nombre="Onix", tipo="tierra", vida=100, ataque=35)

gim1 = gimnasios.Gimnasios(nombre="Gimnasio de Brock", region="Kanto", ciudad="Ciudad Plateada")
gim2 = gimnasios.Gimnasios(nombre="Gimnasio de Misty", region="Kanto", ciudad="Ciudad Celeste")
gim3 = gimnasios.Gimnasios(nombre="Gimnasio de Giovanni", region="Kanto", ciudad="Ciudad Verde")
gim4 = gimnasios.Gimnasios(nombre="Gimnasio de Bugsy", region="Johto", ciudad="Ciudad Azalea")
gim5 = gimnasios.Gimnasios(nombre="Gimnasio de Morty", region="Johto", ciudad="Ciudad Ecruteak")
gim6 = gimnasios.Gimnasios(nombre="Gimnasio de Chuck", region="Johto", ciudad="Ciudad Cianwood")

gimnasios_disponibles = [gim1, gim2, gim3, gim4, gim5, gim6]

pokemon_disponibles  = [p1, p2, p3, p4, p5]