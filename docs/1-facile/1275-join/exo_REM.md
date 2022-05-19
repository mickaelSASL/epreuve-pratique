# Commentaires

## Version itérative

```python
def supprimheu(mots):
    discours = ""
    for mot in mots:
        if mot != "heu":
            if discours != "":
                # on a déjà mis un mot
                discours += " "
            discours += mot
    return discours
```

On ajoute une espace avant d'ajouter un mot au discours, sauf si c'est le premier ; chose que l'on détecte quand le discours est vide.

## Version fonctionnelle

> L'énoncé interdit d'utiliser `join`

Voici ce que ça aurait pu donner : 1 ligne !

```python
def supprimheu(mots):
    return " ".join(mot for mot in mots if mot != "heu")
```

Une version rigolote serait

```python
def supprimheu(heus):
    return " ".join(heu for heu in heus if heu != "heu")
```

## Version avec filtre avant collage

```python
def supprimeuh(mots):
    liste_mots = []
    for mot in mots:
        if mot != "heu":
            liste_mots.append(mot)
    if liste_mots == []:
        return ''
    chaine = liste_mots[0]
    for mot in liste_mots[1:]:
        chaine = chaine + ' ' + mot
    return chaine
```

## Autre version itérative

Dans la plupart des juges en ligne, la présence d'espaces supplémentaires en fin de ligne est acceptée. **Dans ce cas**, une solution est :


```python
def supprimheu(mots):
    discours = ""
    for mot in mots:
        if mot != "heu":
            discours += mot + " "
    return discours
```

Dernière remarque : si on souhaite après coup enlever les espaces en trop à la fin, on peut utiliser `rstrip` ainsi : `#! py return discours.rstrip()`

Mais, attention, cela coute une copie complète de la chaine de caractère.
