---
author: Nicolas Revéret
title: Aplatir
tags:
    - grille
status: validé par Franck, Vincent-Xavier
---

# Aplatir un tableau

On considère un tableau à deux dimensions, non vide, rempli de nombres, une matrice dit-on aussi, et l'on souhaite l'*aplatir*, c'est à dire le transformer en un tableau sur une seule ligne.

Par exemple, le tableau de dimensions $3 \times 4$ :

$$
\begin{array}{|c|c|c|c|}
\hline
1&2&3&4\\
\hline
5&6&7&8\\
\hline
9&10&11&12\\
\hline
\end{array}
$$

pourra être transformé en un nouveau tableau de dimensions $1 \times 12$

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
1&2&3&4&5&6&7&8&9&10&11&12\\
\hline
\end{array}
$$

Les tableaux *de départ* seront représentés par des listes de listes Python. Ainsi le premier tableau ci-dessus sera représenté par :

```python
tab1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

Les tableaux "aplatis",  sur une seule ligne, seront représentés par une simple liste Python. Le second tableau ci-dessus sera représenté par :

```python
tab2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```
Écrire la fonction `aplatir` prenant en argument une liste de listes `tableau` et renvoyant une liste dans laquelle toutes les valeurs de `tableau` sont données à la suite les unes des autres.

!!! example "Exemples"

    ```pycon
    >>> aplatir([[1, 2, 3, 4], [5, 6, 7, 8]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> aplatir([[1], [2], [3], [4], [5], [6]])
    [1, 2, 3, 4, 5, 6]
    ```

{{ IDE('exo') }}