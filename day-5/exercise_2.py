scores = input("Enter the scores of the students:\n")
scores = list(map(int, scores.split(' ')))
print(f"The highest score in the class is: {max(scores)}")
