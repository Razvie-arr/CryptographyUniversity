import random



class Player:
    secret_1 = 0
    secret_2 = 0
    cards = []

    def __init__(self, p):
        self.generate_secrets(p)

    def shuffle(self, deck):
        _deck = deck[:]
        random.shuffle(_deck)
        return _deck

    def encode(self, deck, p):
        _deck = []
        for card in deck:
            _deck.append(pow_h(card, self.secret_1, p))
        return _deck

    def decode(self, card, p):
        return pow_h(card, self.secret_2, p)

    def generate_secrets(self, p):
        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a
        found = False
        while not found:
            secret_1 = simple_num_gen(2)
            if gcd(secret_1, p - 1) != 1:
                continue
            secret_2 = 1
            while secret_2 < (p - 1):
                if ((secret_1 * secret_2) % (p - 1)) == 1:
                    self.secret_1 = secret_1
                    self.secret_2 = secret_2
                    return True
                secret_2 += 1


def simple_num_gen(start):
    for i, num in enumerate(simple_list):
        if num > start:
            start = i
            break
    num = simple_list[random.randint(start, len(simple_list))]
    return num


def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module

    return r


def gen_deck():
    houses = ['S', 'C', 'H', 'D']
    cards = ['0' + str(i) if len(str(i)) == 1 else str(i)
             for i in range(2, 11)]
    cards.extend(ord(face_card) for face_card in ['K', 'Q', 'J', 'A'])
    deck = []
    for house in houses:
        deck.extend([int((str(ord(house)) + str(card))) for card in cards])

    return deck


def read_card(card):
    card = str(card)
    house = chr(int((card[0:2])))
    num = card[2:]
    num = int(num) if int(num) <= 10 else chr((int(num)))
    houses = {'S': '\u2660', 'C': '\u2663', 'H': '\u2665', 'D': '\u2666'}
    return '%s%s' % (str(num), houses[house])


def gen_list():
    n = 200000
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

    return lst


deck = gen_deck()
print("Numeral deck:")
print(deck, '\n')
print("Graphic deck:")
cards = [read_card(card) for card in deck]

print(cards, '\n')

simple_list = gen_list()

P = simple_num_gen(max(deck)+2)

original_deck = deck[:]

print("Generating players")
players_num = random.randint(2, 23)
players = []
for i in range(players_num):
    print("Generating player %s of %s" % (i + 1, players_num))
    players.append(Player(P))

print("Encoding deck")
for i in range(len(players)):
    deck = players[i].encode(deck, P)
    deck = players[i].shuffle(deck)

#deck = deck[5:]
deck_cards, deck = deck[:5], deck[5:]
print(deck)


print("Moving cards")
for i in range(len(players)):
    players[i].cards = deck[:2]
    deck = deck[2:]

print("Decoding cards")
for i in range(len(players)):
    cards = players[i].cards[:]
    for j in range(len(players)):
        if i == j:
            continue
        _cards = []
        for card in cards:
            _cards.append(players[j].decode(card, P))
        cards = _cards[:]
    _cards = []
    for card in cards:
        _cards.append(players[i].decode(card, P))
    cards = _cards[:]
    players[i].cards = cards[:]

"""
for player in players:
    for i in range(len(deck_cards)):
        deck_cards[i] = player.decode(deck_cards[i], P)

#print(deck_cards)