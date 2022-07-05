heights = input("Enter the heights:\n")

heights = list(map(int, heights.split(' ')))

average_height = sum(heights)/len(heights)

print(average_height)
