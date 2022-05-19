# Une solution possible

{{ py('exo_corr', 0, '# TESTS') }}

Même si on essaie d'être malin en ne parcourant que les éléments suivants pour voir si un élément apparaît plusieurs fois, cette fonction a un coût quadratique. En gros, avec un tableau de taille $n$ on va faire environ $n^2$ comparaisons.

L'optimisation de ne regarder que les éléments suivants permet de diviser par 2 le nombre de tests, mais cela reste beaucoup.

Avec un dictionnaire, la recherche d'un élément est en coût constant, ainsi l'exercice a un coût linéaire en sa taille.

```python3
def tous_differents(tableau):
    vus = dict()
    for v in tableau:
        if v in vus:
            return False
        else:
            vus[v] = 1
    return True
```
