---
author: Franck Chambon
title: Collage
tags:
  - boucle
  - string
  - a_trou
---
# Collage de mots

Un logiciel de reconnaissance vocale donne la liste des mots d'un candidat hésitant, il y a de nombreux « heu » que l'on souhaite supprimer de son discours.

Écrire une fonction `supprimeuh`

- qui prend en paramètre `mots` : une liste de mots qui sont des chaines de caractères (non vides) uniquement composées de lettres minuscules,
- et qui renvoie le discours sous forme d'une seule chaine de caractères qui ne contient plus les mots `"heu"` de la liste. Les mots seront séparés par une seule espace. Il n'y aura pas d'espace ni au début, ni à la fin du discours.


> On n'utilisera pas `join`, ni `print` dans cet exercice.

!!! example "Exemples"

    ```pycon
    >>> supprimheu(["je", "heu", "vais", "coder", "heu", "la", "fonction", "supprimheu"])
    'je vais coder la fonction supprimheu'
    ```

    ```pycon
    >>> supprimheu(["c", "est", "facile"])
    'c est facile'
    ```

{{ IDE('exo') }}
