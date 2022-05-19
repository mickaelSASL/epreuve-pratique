# Commentaires

Pour chaque couple `(cle, valeur)` il faut tester l'absence de `valeur` dans le dictionnaire des antécédents afin de lui associer la liste `[cle]` si tel est le cas, et de compléter la liste existante `dico_antecedents[valeur]` en invoquant la méthode `append` dans le cas contraire.

Voici une variante qui initialise une liste vide et procède systématiquement à l'ajout de `cle`.

```python
def antecedents(dico):
    dico_antecedents = {}
    for cle, valeur in dico.items():
        if valeur not in dico_antecedents:
            dico_antecedents[valeur] = []
        dico_antecedents[valeur].append(cle)
    return dico_antecedents
```
