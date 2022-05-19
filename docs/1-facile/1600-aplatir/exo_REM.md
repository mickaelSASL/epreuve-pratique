Cet exercice demande de coder une fonction approchant la méthode `flatten` du module `numpy`.

# Commentaires

{{ py('exo_corr', 0, "# TESTS") }}


Dans la fonction `aplatir` on parcourt l'ensemble des lignes et des valeurs de `tableau` en l'on ajoute les valeurs au fur et à mesure dans une liste `resultat`.

On aurait pu aussi utiliser la méthode `#!py extend` de Python  :

```python
def aplatir(tableau):
    resultat = []
    for ligne in tableau:
        resultat.extend(ligne)
    return resultat
```