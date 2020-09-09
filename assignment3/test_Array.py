from Array import Array

shape = (4,)

my_array = Array(shape, 2, 3, 1, 0)

#__str__
assert my_array.__str__() == "2, 3, 1, 0"

#__add__
3 + my_array
assert my_array.__str__() == "5, 6, 4, 3"
tmp_array = Array(shape, 1, 0, 4, 3)
my_array + tmp_array

assert my_array.__str__() == "6, 6, 8, 6"

#__sub__
my_array - 3
assert my_array.__str__() == "3, 3, 5, 3"
tmp_array = Array(shape, 2, 1, 4, 1)
my_array - tmp_array
assert my_array.__str__() == "1, 2, 1, 2"

#__mul__
my_array * 2
assert my_array.__str__() == "2, 4, 2, 4"
3 * my_array
assert my_array.__str__() == "6, 12, 6, 12"

#__eq__
shape = (4,)
tmp_array = Array(shape, 6, 12, 6, 12)
assert (my_array == tmp_array) == True
shape = (2,)
tmp_array = Array(shape, 12, 18)
assert (tmp_array == my_array) == False


# is_equal()
shape = (4,)
tmp_bool = Array(shape, True, True, True, True)
tmp_array = Array(shape, 6, 12, 6, 12)
assert my_array.is_equal(tmp_array).values == tmp_bool.values
tmp_array = Array(shape, 6, 13, 6, 12)
tmp_bool = Array(shape, True, False, True, True)
assert my_array.is_equal(tmp_array).values == tmp_bool.values
tmp_bool = Array(shape, False, True, False, True)
assert my_array.is_equal(12).values == tmp_bool.values


# mean()

assert my_array.mean() == (6 + 12 + 6 + 12) / 4
shape = (3,)
my_array = Array(shape, 1, 4, 7)
assert my_array.mean() == (1 + 4 + 7) / 3


# variance()
assert my_array.variance() == 18.0
my_array = Array((6,), 3, 5, 2, 7, 1, 3)
assert my_array.variance() == 23.5

# min_element()
assert my_array.min_element() == 1
my_array + -1
assert my_array.min_element() == 0


## 2d-arrays
#__add__
shape = (3, 2)
my_array = Array(shape, 1, 2, 3, 2, 2, 4)
my_array + 3

assert my_array.__str__() == "4, 5, 6, 5, 5, 7"
4 + my_array

assert my_array.__str__() == "8, 9, 10, 9, 9, 11"

#__sub__
my_array - 3

assert my_array.__str__() == "5, 6, 7, 6, 6, 8"
tmp_array = Array(shape, 2, 1, 4, 1, 3, 2)
my_array - tmp_array
assert my_array.__str__() == "3, 5, 3, 5, 3, 6"


#__eq__
tmp_array = Array(shape, 3, 2, 4, 1, 2, 5)
assert (my_array == tmp_array) == True
shape = (2, 2)
tmp_array = Array(shape, 3, 5, 1, 3)
assert (my_array == tmp_array) == False

# is_equal()
shape = (3, 2)
tmp_array = Array(shape, 3, 1, 3, 1, 3, 2)
var = my_array.is_equal(tmp_array)
tmp_bool = Array(shape, True, False, True, False, True, False)
assert var.values == tmp_bool.values
tmp_bool = Array(shape, False, False, True, False, False, False)
tmp_array = Array(shape, 2, 1, 3, 2, 5, 2)
assert my_array.is_equal(tmp_array).values == tmp_bool.values

# mean()

assert my_array.mean() == (3 + 5 + 3 + 5 + 3 + 6) / 6

# min_element()
assert my_array.min_element() == 3

