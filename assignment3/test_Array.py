from Array import Array

shape = (4,)

my_array = Array(shape, 2, 3, 1, 0)

assert my_array.__str__() == "(2, 3, 1, 0)"

3 + my_array
assert my_array.__str__() == "(2, 3, 1, 0, 3)"
shape = (2,)
tmp_array = Array(shape, 1, 0)
my_array + tmp_array
assert my_array.__str__() == "(2, 3, 1, 0, 3, 1, 0)"

my_array - 0
assert my_array.__str__() == "(2, 3, 1, 3, 1)"
tmp_array = Array(shape, 0, 1)
my_array - tmp_array
assert my_array.__str__() == "(2, 3, 3)"


my_array * 2
assert my_array.__str__() == "(4, 6, 6)"
3 * my_array
assert my_array.__str__() == "(12, 18, 18)"


shape = (3,)
tmp_array = Array(shape, 12, 18, 18)
assert (my_array == tmp_array) == True
shape = (2,)
tmp_array = Array(shape, 12, 18)
assert (tmp_array == my_array) == False



shape = (3,)
tmp_array = Array(shape, 12, 18, 18)
assert my_array.is_equal(tmp_array) == (True, True, True)
tmp_array = Array(shape, 12, 18, 17)
assert my_array.is_equal(tmp_array) == (True, True, False)
assert my_array.is_equal(18) == (False, True, True)



assert my_array.mean() == (12 + 18 + 18) / 3
my_array = Array(shape, 1, 4, 7)
assert my_array.mean() == (1 + 4 + 7) / 3



#assert my_array.variance() == 

assert my_array.min_element() == 1
my_array + -1
assert my_array.min_element() == -1

