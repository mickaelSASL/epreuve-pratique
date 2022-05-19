---
author: Nicolas Revéret
title: Anniversaires
tags:
  - dictionnaire
---

# Anniversaires

On dispose d'un dictionnaire python dans lequel :

* les clés sont les prénoms de différentes personnes. Il n'y a aucun prénom en double
* les valeurs sont les mois de naissance de ces personnes stockées sous forme de nombres entiers (`1` pour janvier, ... `12` pour décembre)

Par exemple :

```python
naissances = {'Nicolas': 10, 'Antoine': 7, 'Camille': 7}
```

Vous devez écrire une fonction `anniversaires(naissances, mois)` prenant en arguments le dictionnaire décrit ci-dessus ainsi qu'un numéro d'un mois et renvoyant une liste contenant les prénoms des personnes nées durant ce mois.

!!! example "Exemples"

    ```pycon
    >>> anniversaires({'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 1)
    []
    >>> anniversaires({'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 10)
    ['Nicolas']
    >>> anniversaires({'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 7)
    ['Antoine', Camille]
    >>> anniversaires({'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 13)
    []
    >>> anniversaires({}, 1)
    []
    ```

{{ IDE('exo') }}
