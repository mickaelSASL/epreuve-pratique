# Commentaires

## Version simple

```python
def differences(source_1, source_2):
    n = len(source_1)
    resultat = [False] * n
    for i in range(n):
        if source_1[i] != source_2[i]:
            resultat[i] = True
    return resultat
```

## Version simple (2)

```python
def differences(source_1, source_2):
    n = len(source_1)
    resultat = []
    for i in range(n):
        resultat.append(source_1[i] != source_2[i])
    return resultat
```

## Avec liste en compréhension

```python
def differences(source_1, source_2):
    n = len(source_1)
    resultat = [source_1[i] != source_2[i] for i in range(n)]
    return resultat
```

## Version style fonctionnel

```python
def differences(source_1, source_2):
    return [a != b for a, b in zip(source_1, source_2)]
```
