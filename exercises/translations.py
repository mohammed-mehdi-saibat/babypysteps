# T2.1 — Exercice A : Variables et conditions
def check_score(score: int):
    if score >= 14:
        print("Admis")
    else: 
        print("Recalé")


# T2.2 — Exercice B : Boucle et accumulation

def sum_prices(prices: list):
    total = 0
    for price in prices:
        total += price
    print(total)

#T2.3 — Exercice C : Tableau associatif

def describe_user(user: dict):
    print(f"{user['name']} habite à {user['city']}")

# T2.4 — Exercice D : Filtrer une liste

# Using filter()

def is_positive1(array: list):
    return list(filter(lambda x: x > 0, array))  # lambda is name of an anynymous function in python
    
# Without filter()

def is_positive2(array: list):
    return [num for num in array if num > 0]

# T2.5 — Exercice E : Compter des occurrences

def count_words(words: list):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

