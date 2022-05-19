# Commentaires

Sorti de son contexte, l'exercice revient à déterminer la longueur de la plus longue sous-séquence d'éléments vérifiant 
une certaine condition dans une liste. En l'occurrence, la longueur de la plus longue sous-séquence de nombres négatifs.

## Une solution possible

{{ IDE('exo_corr') }}

Comme on cherche la plus longue longueur, on commence par l'initialiser à `0` (ligne 2).

On crée ensuite la variable `periode` qui stockera la longueur de la sous-séquence de nombres négatifs actuellement lue. Avant la lecture, elle est naturellement à `0` (ligne 3).
On parcourt ensuite les valeurs de la liste `temperatures` et pour chacune d'elle :

* si elle est négative :
  
  *  on incrémente la valeur de la sous-séquence actuelle
  *  on teste si cette sous-séquence est plus longue que la plus longue déjà trouvée. Si c'est le cas, on met à jour la valeur (ligne 8)
  
* sinon (la température est strictement positive), on remet la longueur de la séquence actuelle à `0` (ligne 10)

La fonction renvoie pour terminer la longueur de la plus longue période.