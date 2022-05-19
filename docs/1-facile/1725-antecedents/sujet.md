---
author: Jean Diraison
title: Dictionnaire des antécédents
tags:
  - dictionnaire
  - boucle
---
# Dictionnaire des antécédents

Un dictionnaire associe des valeurs à des clés, comme par exemple `{"Paris": "P", "Lyon": "L", "Nantes": "N", "Lille": "L"}` qui associe `"P"` à la clé `"Paris"`. 

Suivant les cas, une même valeur peut être associée à une ou plusieurs clés. Dans l'exemple précédent, la valeur `"L"` est associée aux clés `"Lyon"` et `"Lille"`, on les appelle les **antécédents** de `"L"`, tandis que `"P"` a la clé `"Paris"` pour seul et unique antécédent.

On peut ainsi construire le dictionnaire des antécédents `{"P": ["Paris"], "L": ["Lyon", "Lille"], "N": ["Nantes"]}`.

Vous devez écrire une fonction `antecedents` de paramètre `dico` qui renvoie le dictionnaire associant les valeurs de `dico` à la liste de leurs antécédents dans `dico`.


Note : Puisqu'aucun ordre ne vous est imposé dans la construction des listes, une étape supplémentaire de tri est réalisée lors des tests de validation.

!!! Exemples

    ```pycon
    >>> antecedents({'a': 5, 'b': 7})
    {5: ['a'], 7: ['b']}
    >>> antecedents({'a': 5, 'b': 7, 'c': 5})
    {5: ['a', 'c'], 7: ['b']}
    >>> antecedents({"Paris": "P", "Lyon": "L", "Nantes": "N", "Lille": "L"})
    {"P": ["Paris"], "L": ["Lyon", "Lille"], "N": ["Nantes"]}
    ```

{{ IDE('exo') }}
