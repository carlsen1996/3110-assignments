from Array import Array

shape = (4,)

my_array = Array(shape, 2, 3, 1, 0)

#__str__
assert my_array.__str__() == "2, 3, 1, 0"

#__add__
3 + my_array
assert my_array.__str__() == "2, 3, 1, 0, 3"
shape = (2,)
tmp_array = Array(shape, 1, 0)
my_array + tmp_array
assert my_array.__str__() == "2, 3, 1, 0, 3, 1, 0"

#__sub__
my_array - 0
assert my_array.__str__() == "2, 3, 1, 3, 1"
tmp_array = Array(shape, 0, 1)
my_array - tmp_array
assert my_array.__str__() == "2, 3, 3"

#__mul__
my_array * 2
assert my_array.__str__() == "4, 6, 6"
3 * my_array
assert my_array.__str__() == "12, 18, 18"

#__eq__
shape = (3,)
tmp_array = Array(shape, 12, 18, 18)
assert (my_array == tmp_array) == True
shape = (2,)
tmp_array = Array(shape, 12, 18)
assert (tmp_array == my_array) == False


# is_equal()
shape = (3,)
tmp_array = Array(shape, 12, 18, 18)
assert my_array.is_equal(tmp_array) == Array((3,), True, True, True)
tmp_array = Array(shape, 12, 18, 17)
assert my_array.is_equal(tmp_array) == Array((3,), True, True, False)
assert my_array.is_equal(18) == Array((3,), False, True, True)


# mean()

assert my_array.mean() == (12 + 18 + 18) / 3
my_array = Array(shape, 1, 4, 7)
assert my_array.mean() == (1 + 4 + 7) / 3


# variance()
#assert my_array.variance() == 

# min_element()
assert my_array.min_element() == 1
my_array + -1
assert my_array.min_element() == -1


## 2d-arrays
#__add__
shape = (3, 2)
my_array = Array(shape, 1, 2, 3, 2, 2, 4)
assert my_array + (3, 1) == (1, 2, 3, 2, 2, 4, 3, 1)
assert (4, 1) + my_array == (1, 2, 3, 2, 2, 4, 3, 1, 4, 1)

#__sub__
assert my_array - (4, 1) == (1, 2, 3, 2, 2, 4, 3, 1)

#__eq__
shape = (3, 2)
tmp_array = Array(shape, 3, 2, 4, 1, 2, 5)
assert (my_array == tmp_array) == False
tmp_array + (2, 3)
assert (my_array == tmp_array) == True

# is_equal()
shape = (4, 2)
tmp_array = Array(shape, 1, 2, 3, 2, 2, 4, 3, 1)
assert my_array.is_equal(tmp_array) == Array(shape, True, True, True, True, True, True, True, True)
tmp_array = Array(shape, 1, 4, 2, 2, 1, 4, 5, 2)
assert my_array.is_equal(tmp_array) == Array(shape, True, False, False, True, False, True, False, False)

# mean()
assert my_array.mean() == (1 + 4 + 2 + 2 + 1 + 4 + 5 + 2) / 8

# min_element()
assert my_array.min_element() == 1