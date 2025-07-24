palos = ['♠', '♥', '♦', '♣']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
mazo = [valor + palo for palo in palos for valor in valores]

for carta in mazo:
    print(carta)
