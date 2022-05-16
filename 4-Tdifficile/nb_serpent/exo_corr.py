serpent = [0, 10]
serpent_croissant = [0] + [1] * 9
serpent_decroissant = [0] + [1] * 9

for _ in range(2, 100):
    new_croissant = [0] * 10
    new_decroissant = [0] * 10
    for i in range(10):
        new_croissant[i] = sum(serpent_decroissant[j] for j in range(0, i))
        new_decroissant[i] = sum(serpent_croissant[j] for j in range(i+1, 10))
    serpent_croissant = new_croissant
    serpent_decroissant = new_decroissant
    serpent.append(sum(serpent_croissant) + sum(serpent_decroissant))

# tests

assert serpent[0] == 0
assert serpent[1] == 10
assert serpent[2] == 81
assert serpent[3] == 525
assert len(serpent) >= 100
