# tests

assert cree_palindrome("ka", "y") == 'kayak'
assert cree_palindrome("ser", "") == 'serres'
assert cree_palindrome("r", "ada") == 'radar'
assert cree_palindrome("ar", "fettttef") == 'arfettttefra'

# autres tests

assert cree_palindrome("", "") == ''
assert cree_palindrome("", "a") == 'a'
assert cree_palindrome("a", "") == 'aa'
assert cree_palindrome("abcd", "tyuuyt") == 'abcdtyuuytdcba'
assert cree_palindrome("abcde", "tyuzuyt") == 'abcdetyuzuytedcba'
