# Commentaires

{{ py('exo_corr') }}

On pourrait écrire un code avec un style plus fonctionnel

```python
def occurrences_mini(donnees):
    mini = donnees[0]
    indices = []
    for i, valeur in enumerate(donnees):
        if valeur == mini:
            indices.append(i)
        elif valeur < mini:
            mini = valeur
            indices = [i]
    return (mini, indices)
```

`enumerate` est utile lorsqu'on a besoin de l'indice et de la valeur.
