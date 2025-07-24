import random

# Palos y valores
palos = ['♠', '♥', '♦', '♣']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Crear el mazo
mazo = [valor + palo for palo in palos for valor in valores]

# Barajar el mazo
random.shuffle(mazo)

# Repartir 5 cartas (las primeras 5)
mano = mazo[:5]
print("Tu mano:", ' '.join(mano))


import random
from collections import Counter

# Crear el mazo
palos = ['♠', '♥', '♦', '♣']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
mazo = [valor + palo for palo in palos for valor in valores]

# Barajar el mazo
random.shuffle(mazo)

# Repartir una mano de 5 cartas
mano = mazo[:5]
print("Tu mano:", ' '.join(mano))

# Analizar la mano
# Extraer solo los valores (ignorar los palos por ahora)
solo_valores = [carta[:-1] for carta in mano]

# Contar cuántas veces aparece cada valor
conteo = Counter(solo_valores)

# Detectar combinaciones básicas
def evaluar_mano(conteo):
    if 4 in conteo.values():
        return "Póker"
    elif 3 in conteo.values() and 2 in conteo.values():
        return "Full House"
    elif 3 in conteo.values():
        return "Trío"
    elif list(conteo.values()).count(2) == 2:
        return "Doble par"
    elif 2 in conteo.values():
        return "Par"
    else:
        return "Carta alta"

resultado = evaluar_mano(conteo)
print("Tienes:", resultado)

# Repartir manos a 4 jugadores
num_jugadores = 4
cartas_por_mano = 5
manos = [mazo[i*cartas_por_mano:(i+1)*cartas_por_mano] for i in range(num_jugadores)]

for idx, mano in enumerate(manos):
    print(f"Mano jugador {idx+1}: {' '.join(mano)}")