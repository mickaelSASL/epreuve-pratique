# Commentaires

## Liste en compréhension

```python
def delta_encoding(valeurs):
    differences = [valeurs[i] - valeurs[i - 1] for i in range(1, len(valeurs))]
    return (valeurs[0], differences)
```

## Liste dynamique

```python
def delta_encoding(valeurs):
    differences = []
    for i in range(1, len(valeurs)):
        differences.append(valeurs[i] - valeurs[i - 1])
    return (valeurs[0], differences)
```

On pouvait aussi itérer de `0` à `#!python len(valeurs) - 1`

```python
def delta_encoding(valeurs):
    differences = []
    for i in range(len(valeurs) - 1):
        differences.append(valeurs[i + 1] - valeurs[i])
    return (valeurs[0], differences)
```
