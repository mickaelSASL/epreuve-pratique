# tests

tableau1 = [0, 1, 0, 1, 0, 1, 0]
separe(tableau1)
assert tableau1 == [0, 0, 0, 0, 1, 1, 1]

tableau2 = [1, 1, 1, 0, 0, 0]
separe(tableau2)
assert tableau2 == [0, 0, 0, 1, 1, 1]

# autres tests

tableau_vide = []
separe(tableau_vide)
assert tableau_vide == []

que_0 = [0]*100
separe(que_0)
assert que_0 == [0]*100

que_1 = [1]*100
separe(que_1)
assert que_1 == [1]*100

mono_0 = [0]
separe(mono_0)
assert mono_0 == [0]

mono_1 = [1]
separe(mono_1)
assert mono_1 == [1]

duo = [1, 0]
separe(duo)
assert duo == [0, 1]

un_seul_1_a = [1, 0, 0, 0, 0, 0]
separe(un_seul_1_a)
assert un_seul_1_a == [0, 0, 0, 0, 0, 1]

un_seul_1_b = [0, 0, 1, 0, 0, 0]
separe(un_seul_1_b)
assert un_seul_1_b == [0, 0, 0, 0, 0, 1]

un_seul_1_c = [0, 0, 0, 0, 0, 1]
separe(un_seul_1_c)
assert un_seul_1_c == [0, 0, 0, 0, 0, 1]

un_seul_0_a = [0, 1, 1, 1, 1, 1]
separe(un_seul_0_a)
assert un_seul_0_a == [0, 1, 1, 1, 1, 1]

un_seul_0_c = [1, 1, 1, 1, 1, 0]
separe(un_seul_0_c)
assert un_seul_0_c == [0, 1, 1, 1, 1, 1]
