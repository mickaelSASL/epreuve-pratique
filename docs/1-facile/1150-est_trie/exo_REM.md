On peut coder cette phrase logique :

> Le tableau est trié s'il a moins de 2 éléments ou alors si chacun des éléments à partir du 2e est supérieur ou égal à son prédécesseur.

```python
def est_trie(tab):
    return all(tab[i] >= tab[i-1] for i in range(1, len(tab)))
```

Notons, que pour la version du corrigé et la version ci-dessus, on tire parti du fait que la boucle dans les cas où le tableau à strictement moins de 2 éléments sera vide et `all([])` renvoie `True`.

