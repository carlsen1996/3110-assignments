import Array

shape = (4,)
print(shape)
my_array = Array(shape, 2, 3, 1, 0)

assert print(my_array) == "2, 3, 1, 0"

my_array.add(3)
assert print(my_array) == "2, 3, 1, 0, 3"
shape = (2,)
tmp_array = Array(shape, 1, 0)
my_array.add(tmp_array)
assert print(my_array) == "2, 3, 1, 0, 3, 1, 0"

my_array.sub(0)
assert print(my_array) == "2, 3, 1, 0, 3, 1"
tmp_array.rsub(my_array)
assert print(my_array) == "2, 3, 3"

my_array.mul(2)
assert print(my_array) == "4, 6, 6"
my_array.mul(3)
assert print(my_array) == "12, 18, 18"

shape = (3,)
tmp_array = Array(shape, 12, 18, 17)
assert (my_array == tmp_array) == True
shape = (2,)
tmp_array = Array(shape, 12, 18)
assert (tmp_array == my_array) == False

shape = (3,)
tmp_array = Array(shape, 12, 18, 18)
assert my_array.is_equal(tmp_array) == True
tmp_array = Array(shape, 12, 18, 17)
assert my_array.is_equal(tmp_array) == False

assert my_array.mean() == (12 + 18 + 18) / 3
my_array = Array(shape, 1.2, 4, 7)
assert my_array.mean() == (1.2, 4, 7) / 3

#assert my_array.variance() == 

assert my_array.min_element() == 1.2
my_array.add(1)
assert my_array.min_element() == 1