# Commentaires

{{ py('exo_corr', 0, "# TESTS") }}

Il n'y a pas de difficultés majeures si ce n'est prendre soin de ne pas modifier la liste initiale.

On crée donc une seconde liste que l'on complète au fur et à mesure en parcourant les valeurs de `valeurs`.

On aurait aussi pu utiliser une liste par compréhension et un *opérateur ternaire* :

```python
def remplacer(valeurs, valeur_cible, nouvelle_valeur):
    return [val if val != valeur_cible else nouvelle_valeur for val in valeurs]
```