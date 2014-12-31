from collections import defaultdict

def anagram_finder_one(potentials):
	grouped_potentials = defaultdict(list)
	anagrams = []
	for x in potentials:
		grouped_potentials[''.join(sorted(x.lower()))].append(x)
	for k,v in grouped_potentials:
		if len(v) > 1:
			anagrams.append(v)
	return anagrams

def anagram_finder_two(potentials):
	grouped_potentials = {}
	anagrams = []
	for x in potentials:
		grouped_potentials.setdefault(''.join(sorted(x.lower())), []).append(x)
	for k,v in grouped_potentials.items():
		if len(v) > 1:
			anagrams.append(v)
	return anagrams

def anagram_counter(potentials):
	sorted_potentials = [x.lower().sort for x in potentials]
	eliminated = set(sorted_potentials)
	return len(potentials) - len(eliminated)