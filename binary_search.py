def binarySearch(upper_bound, num):
	tries = 0
	lower_bound = 1
	upper_bound = upper_bound
	while True:
		tries += 1
		guess = (lower_bound + upper_bound) / 2
		if guess == num:
			print 'You guessed my number in', tries, 'tries!'
			break
		elif guess > num:
			print guess, 'is too high.'
			upper_bound = guess - 1
		else:
			print guess, 'is too low.'
			lower_bound = guess + 1

if __name__ == '__main__':
	binarySearch(300, 22)