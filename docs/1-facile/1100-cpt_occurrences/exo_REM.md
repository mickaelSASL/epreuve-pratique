# Commentaires

## Itération sans indice

Version recommandée

{{ py('exo_corr') }}

## Itération avec indice

Version possible

```python
def compte_occurrences(caractere, mot):
    nb_occurrences = 0
    for i in range(len(mot)):
        if mot[i] == caractere:
            nb_occurrences += 1
    return nb_occurrences
```

## Version fonctionnelle

Pour les bons élèves ; n'est pas hors programme.

```python
def compte_occurrences(caractere, mot):
    return sum(1 for lettre in mot if lettre == caractere)
```

## Version non autorisée

Avec la facilité du langage Python (`count`).

```python
def compte_occurrences(caractere, mot):
    return mot.count(caractere)
```
