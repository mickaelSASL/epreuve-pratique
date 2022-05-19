# Commentaires

## Version recommandée

{{ py('exo_corr') }}


## Version sans compréhension de liste

```python
def recherche_positions(element, tableau):
    positions = []
    for i in range(len(tableau)):
        if tableau[i] == element:
            positions.append(i)
    return positions
```
