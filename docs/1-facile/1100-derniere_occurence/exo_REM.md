En commençant par la fin, on s'arrête dès qu'on trouve la cible :

```python
def derniere_occurrence(tableau, cible):
    for i in range(len(tableau)-1, -1, -1):
        if tableau[i] == cible:
            return i
    return len(tableau)
```
