# tests

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !', "Erreur sur ce test"
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !', "Erreur sur ce test"

# autres tests

assert cesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1) == 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
assert cesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -2) == 'YZABCDEFGHIJKLMNOPQRSTUVWX'
assert cesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert cesar("", 7) == ''
assert cesar("!?.:", 7) == '!?.:'
assert cesar("CESAR", 139) == 'LNBJA'

