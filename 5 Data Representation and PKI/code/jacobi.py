def jacobi (a, m):
	j = 1
	a %= m
	while a
		t = 0
		while not a & 1:
			a = a >> 1
			t += 1
		if t & 1 and m % 8 in (3, 5):
			j = -j
		if (a % 4 == m % 4 == 3):
			j = -j
		a, m = m % a, a
	return j if m == 1 else 0
