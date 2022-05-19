---
author: Franck Chambon
title: Découpe
tags:
  - boucle
  - string
---
# Découpage de mots

Pour analyser automatiquement les débats entre des orateurs, on vous demande de créer une fonction `decoupe_mots` qui renvoie la liste des mots de 4 lettres ou plus dans une chaine de caractères `discours` passée en paramètre.


On suppose que la chaine `discours` a été renvoyée par une fonction de reconnaissance vocale qui ignore la ponctuation et ne renvoie que des lettres minuscules sans accent ainsi que des espaces. Le `discours` se termine aussi par une espace.

> On n'utilisera pas la fonction `split` dans cet exercice.

!!! example "Exemples"

    ```pycon
    >>> discours = "je peux vous dire aujourd hui mes amis qu en depit des difficultes et des frustrations actuelles j ai quand meme fait un reve c est un reve profondement enracine dans le reve americain "
    >>> decoupe_mots(discours)
    ['peux', 'vous', 'dire', 'aujourd', 'amis', 'depit', 'difficultes', 'frustrations', 'actuelles', 'quand', 'meme', 'fait', 'reve', 'reve', 'profondement', 'enracine', 'dans', 'reve', 'americain']

    ```

    ```pycon
    >>> test_2 = "abcd azerty   xyz    azerty     "
    >>> decoupe_mots(test_2)
    ['abcd', 'azerty', 'azerty']
    ```

{{ IDE('exo') }}
