a = [4, 5, 6, 10, 1, 3]
# print(a[-1])


import unittest

def merge_sort(a):
	if len(a) < 2:
		return a[:]
	else:
		median = int(len(a) / 2)
		left = merge_sort(a[:median])
		right = merge_sort(a[median:])
		return merge(left, right)

def merge(left, right):
	res = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	while i < len(left):
		res.append(left[i])
		i += 1
	while j < len(right):
		res.append(right[j])
		j += 1
	return res


class Test_merge(unittest.TestCase):
	
	def test_merge(self):
		a = [4, 5, 6, 10, 1, 3]
		h = [4, 5, 6, 10, 1, 3]
		h.sort()
		self.assertEqual(merge_sort(a),h)


unittest.main()
