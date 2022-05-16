def denivele_positif(altitudes):
    denivele = 0
    for i in range(len(altitudes) - 1):
        if altitudes[i + 1] > altitudes[i]:
            denivele += altitudes[i + 1] - altitudes[i]
    return denivele

# tests

assert denivele_positif([330, 490, 380, 610, 780, 550]) == 560
assert denivele_positif([200, 300, 100]) == 100
