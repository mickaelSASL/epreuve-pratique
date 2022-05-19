# Commentaires

{{ py('exo_corr') }}

La fonction `limite_amplitude` est composée d'une structure conditionnelle, avec trois cas.

La fonction `ecrete` construit une liste vide qu'elle étend par accumulation. On aurait pu faire une liste en compréhension avec le code :

```py
def ecrete(valeurs, x_min, x_max):
    return [limite_amplitude(x, x_min, x_max) for x in valeurs]
```

!!! danger "Pour les experts"
    On peut avoir aussi un code avec un style fonctionnel

    ```py
    def ecrete(valeurs, x_min, x_max):
        filtre = lambda x: limite_amplitude(x, x_min, x_max)
        return list(map(filtre, valeurs))
    ```

    `filtre` est une fonction qui pourrait aussi être définie par

    ```python
    def filtre(x):
        return limite_amplitude(x, x_min, x_max)
    ```

    Le constructeur `#!py lambda` permet de définir une fonction anonyme, c'est parfois utile comme paramètre passé à une autre fonction.
