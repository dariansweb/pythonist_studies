# for loop - Create a set of unique test scores
test_scores = [99, 53, 74, 66, 45, 74]
unique_scores = set()
for score in test_scores:
    unique_scores.add(score)

# set comprehension syntax template
# unique_scores = {expression for temporary_variable in original_iterable}

########

# for loop - Create a set of unique test scores over 70
test_scores = [99, 53, 74, 66, 45, 74]
unique_scores_over_70 = set()
for score in test_scores:
    if score > 70:
        unique_scores_over_70.add(score)

# set comprehension syntax template
# unique_scores_over_70 = {expression for temporary_variable in original_iterable}

########

# print statements
print(unique_scores)
print(unique_scores_over_70)
