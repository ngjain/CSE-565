import unittest

def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
# making quicksort easy to call
def quicksort2(array):
    quickSort(array, 0, len(array)-1)
    return array


class TestStringMethods(unittest.TestCase):

# assert for sorted
    def test_1(self):
        array = [1,2,3,4,5]
        self.assertEqual(
                sorted(array),
                quicksort2(array))
# assert for random
    def test_2(self):
        array = [3,1,4,9,3]
        self.assertEqual(
                sorted(array),
                quicksort2(array))
# assert for empty
    def test_3(self):
        array = []
        self.assertEqual(
                sorted(array),
                quicksort2(array))
# assert for duplicates
    def test_4(self):
        array = [1,1,1,1]
        self.assertEqual(
                sorted(array),
                quicksort2(array))
# assert for single element
    def test_5(self):
        array = [1]
        self.assertEqual(
                sorted(array),
                quicksort2(array))
# assert for sorted
    def test_6(self):
        array = [1,2,3,4,5]
        self.assertEqual(
                sorted(array),
                quicksort2(array))
# assert for a random set of values
    def test_7(self):
        import random
        for i in range(100):
            length = random.randint(0,1000)
            array = []
            for j in range(length):
                array.append(random.randint(0,1000))
            self.assertEqual(
                    sorted(array),
                    quicksort2(array))


if __name__ == '__main__':
    unittest.main()
