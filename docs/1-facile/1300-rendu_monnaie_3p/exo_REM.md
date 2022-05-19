# Commentaires

## Première version

```python
def rendu(somme_a_rendre):
    n_5 = somme_a_rendre // 5
    somme_a_rendre -= 5 * n_5

    n_2 = somme_a_rendre // 2
    somme_a_rendre -= 2 * n_2

    n_1 = somme_a_rendre
    
    return (n_5, n_2, n_1)
```

## Version, avec `divmod`

La fonction `divmod` renvoie le quotient **et** le reste d'une division entière.

```python
def rendu(somme_a_rendre):
    n_5, somme_a_rendre = divmod(somme_a_rendre, 5)
    n_2, somme_a_rendre = divmod(somme_a_rendre, 2)
    n_1 = somme_a_rendre

    return (n_5, n_2, n_1)
```


## Version avec une boucle

```python
VALEURS = (5, 2, 1)

def rendu(somme_a_rendre):
    resultat = [0, 0, 0]
    for i in range(3):
        resultat[i], somme_a_rendre = divmod(somme_a_rendre, VALEURS[i])

    return tuple(retour)
```

Cette dernière version est utile si on envisage un autre système de pièces avec de nombreuses valeurs.
