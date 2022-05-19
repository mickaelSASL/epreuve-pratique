---
author: Sébastien HOARAU
title: Couleurs
tags:
    - string
    - dictionnaire
description: Manipuler une chaine de caractères et un petit calcul arithmétique pour construire un tuple.
difficulty: facile
---

# Des couleurs en HTML

## Deux représentations des couleurs

Une couleur en HTML est représentée par une chaine de caractères de sept caractères dont le premier est `'#'` ; les six autres, groupés 2 par 2 forment 3 entiers en hexadécimal (base 16). Le premier entier est la quantité de rouge ; le deuxième la quantité de vert et le troisième est la quantité de bleu. Ces trois valeurs hexadécimales sont comprises entre `"00"` et `"FF"`.

!!! example "Exemples"

    Voici quelques couleurs en HTML : 
    
    - `"#C0392B"` (une sorte de <span style="color:#C0392B;">brun rouge</span>), 
    - `"#00FF00"` du <span style="color:#00FF00">vert</span> uniquement, 
    - `"#000000"` du noir.

Une autre façon de représenter une couleur est par un triplet $(r, v, b)$ de valeurs décimales comprises entre $0$ et $255$ : $r$ est la quantité de rouge, $v$ la quantité de vert et $b$ la quantité de bleu.

On souhaite écrire une fonction `html_vers_rvb` qui prend une chaine de caractères représentant une couleur HTML en paramètre et qui renvoie le triplet de décimaux $(r, v, b)$ représentant la même couleur.

On rappelle les valeurs décimales des 16 _chiffres_ hexadécimaux sont : `'0'` vaut $0$, jusqu'à `'9'` qui vaut $9$, puis `'A'` vaut $10$, `'B'` vaut $11$ ainsi de suite jusqu'à `'F'` qui vaut $15$.

Pour calculer la valeur décimale d'un nombre hexadécimal de deux chiffres $(ab)_{16}$, on fera le produit de la valeur décimale du chiffre des seizaines $a$ par $16$ plus la valeur décimale du chiffre des unités $b$.

!!! example "Exemples"

    - le nombre hexadécimal `"B5"` vaut $11\times 16 + 5$ soit $181$ en décimal,
    - `"00"` vaut $0\times 16 + 0$ soit $0$,

!!! note "Indication"

    ```pycon
    >>> couleur = "#F307D6"
    >>> couleur[1]
    'F'
    >>> couleur[2]
    '3'
    ```

## Questions

1. Compléter le dictionnaire `HEX_DEC` qui donne les valeurs décimales des _chiffres_ hexadécimaux
2. Écrire la définition de la fonction `hex_int` qui prend deux chaines d'un caractère en paramètres `a` et `b` ; de sorte que $(ab)_{16}$ est un entier en hexadécimal et renvoie la valeur décimale associée : 
      ```pycon
      >>> hex_int('B', '5')
      181
      >>> hex_int('0', '0')
      0
      ```

3. Écrire la définition de la fonction `html_vers_rvb` en vous servant de la fonction précédente.
      ```pycon
      >>> html_vers_rvb("#C0392B")
      (192, 57, 43)
      >>> html_vers_rvb("#00FF00")
      (0, 255, 0)
      >>> html_vers_rvb("#000000")
      (0, 0, 0)
      ```

{{ IDE('exo') }}
