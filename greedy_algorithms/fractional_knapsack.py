def fractional_knapsack(values, weights, capacity):
	n = len(values)

	def score(i):
		return values[i]/weights[i]

	items = sorted(range(n), key = score, reverse=True)

	value, weight = 0, 0

	for i in items:
		if weight+weights[i] <= capacity:
			# selected += [i]
			weight += weights[i]
			value += values[i]

	return value


def constructive(values, weights, cap):
	knapsack = []
	Weight = 0

	while(Weight <= cap):# and values):
		best = max(values)
		i = values.index(best)
		if weights[i] <= cap-Weight:
			knapsack.append(i+1)
			Weight = Weight + weights[i]
		del values[i]
		del weights[i]
	# print(knapsack, Weight)
	return knapsack, Weight

# print(fractional_knapsack([60, 100, 120], [20, 50, 30], 50))

# print(fractional_knapsack([500], [30], 10))

print(constructive([60, 100, 120], [20, 50, 30], 50))

print(constructive([500], [30], 10))