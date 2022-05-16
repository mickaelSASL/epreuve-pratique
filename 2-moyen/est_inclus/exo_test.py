# tests
assert     est_inclus("AATC", "GTACAAATCTTGCC")
assert not est_inclus("AGTC", "GTACAAATCTTGCC")
assert not est_inclus("AGTC", "GTACAAATCTTGCA")
assert     est_inclus("AGTC", "GTACAAATCTAGTC")



# autres tests
assert     est_inclus("AAAA", "AAAAGTATCTTGCC")
assert     est_inclus("GTAC", "GTACAAATCTTGCC")
assert     est_inclus("AAAA", "GTACAAATCTAAAA")
assert     est_inclus("AGTA", "GTACAAATCTAGTA")
assert not est_inclus("AGTA", "GTACAAATCTAGTC")
