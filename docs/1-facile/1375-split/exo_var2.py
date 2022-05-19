def decoupe_mots(discours):
    return [mot for mot in discours.split() if len(mot) >= 4]

discours = "je peux vous dire aujourd hui mes amis qu en depit des difficultes et des frustrations actuelles j ai quand meme fait un reve c est un reve profondement enracine dans le reve americain "

print(decoupe_mots(discours))
