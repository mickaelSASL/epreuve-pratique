assert delta_encoding([
    1_000_000, 1_000_042, 1_000_040, 1_000_055, 1_000_010
]) ==  (1000000, [42, -2, 15, -45])

assert delta_encoding([42]) == (42, [])


assert delta_encoding([0, 1, 2, 3, 4]) == (0, [1, 1, 1, 1])

