# A bag contains 5 red balls and 5 blue balls.

# Two balls are selected without replacement.

# Calculate:

# Probability that the first ball is red.
# Probability that the second ball is red given that the first ball was red.
# Probability that both balls are red.
# Are the two events independent or dependent?
# Repeat the problem assuming the first ball is replaced before selecting the second ball.
# Compare the two cases.



# without replacement:

red = 5
blue = 5
total = red + blue

# 1. First ball is red
p_first_red = red / total

# 2. Second is red given first was red
p_second_red_given_first_red = (red - 1) / (total - 1)

# 3. Both are red
p_both_red = p_first_red * p_second_red_given_first_red

# 4. Independent or dependent?
# Because probability changes after first selection:
dependent = p_second_red_given_first_red != p_first_red

print("P(First Red):", p_first_red)
print("P(Second Red | First Red):", p_second_red_given_first_red)
print("P(Both Red):", p_both_red)
print("Dependent:", dependent)




# With replacement

p_first_red_replace = 5 / 10

p_second_red_given_first_red_replace = 5 / 10

p_both_red_replace = (
    p_first_red_replace *
    p_second_red_given_first_red_replace
)

print("P(First Red):", p_first_red_replace)
print(
    "P(Second Red | First Red):",
    p_second_red_given_first_red_replace
)
print("P(Both Red):", p_both_red_replace)