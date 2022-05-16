# Tests
assert supprime_premier('ukulélé', 'u') == (True, 'kulélé')
assert supprime_premier('ukulélé', 'é') == (True, 'ukullé')
assert supprime_premier('ukulélé', 'a') == (False, 'ukulélé')
assert anagrammes('chien', 'niche')
assert anagrammes('énergie noire', 'reine ignorée')
assert not anagrammes('louve', 'poule')

# Tests supplémentaires
assert supprime_premier('mississippi', 'm') == (True, 'ississippi')
assert supprime_premier('mississippi', 'a') == (False, 'mississippi')
assert anagrammes('nsi', 'isn')
assert not anagrammes('nsi', 'snt')
assert anagrammes('clint  eastwood', 'old west action')
assert anagrammes('astronomers ', 'moon starers')
assert not anagrammes('astronome', 'metronome')
