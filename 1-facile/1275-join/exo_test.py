assert supprimheu([]) == ''
assert supprimheu(["heu"]) == ''
assert supprimheu(["heu", "bonjour"]) == 'bonjour'
assert supprimheu(["bien", "le", "bonjour"]) == 'bien le bonjour'
assert supprimheu(["bien", "le", "bonjour", "heu"]) == 'bien le bonjour'
