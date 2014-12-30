def find_max_deviation(v, d):
	l = len(v)
	max_deviation = 0
	for i in xrange(l):
	   	if len(v[i:i+d]) == d:
	   	    print v[i:i+d]
	   	    deviation = max(v[i:i+d]) - min(v[i:i+d])
	   	    if deviation > max_deviation:
	   	        max_deviation = deviation

	print max_deviation