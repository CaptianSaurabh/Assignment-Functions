## Question In Question Paper 

orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

result = list(map(lambda order: (order[0], order[3] * order[2] + (10 if order[3] * order[2] < 100 else 0)), orders))

print(result)