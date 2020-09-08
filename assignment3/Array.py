from copy import deepcopy

class Array:
    # Assignment 3.3  

    def __init__(self, shape, *values):
        self.shape = shape
        self.values = values
        fileType = type(self.values[0])
        for value in self.values:
            if type(value) != fileType:
                raise ValueError("The data types in the array are not the same")
        sum = 1
        for i in self.shape:
            sum = sum * i
        
        
        if len(self.values) != sum:
            raise ValueError("The number of values does not match the shape")
        



        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        

    def __str__(self):
        if len(self.shape) == 1:
            return str(self.values).strip("()")
        else:
            return str(self.values)
        
        
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        

    def __add__(self, other):
        if isinstance(other, (int, float)):
            tmpTup = ()
            for value in self.values:
                value = value + other
                tmpTup = tmpTup + (value,)
            self.values = tmpTup
            return self
        elif isinstance(other, Array):
            i = 0
            tmpTup = ()
            for value in self.values:
                value = value + other.values[i]
                i = i + 1
                tmpTup = tmpTup + (value,)
            self.values = tmpTup
            return self
        else:
            raise NotImplementedError("The values you are adding is not implemented")


        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        

    def __radd__(self, other):
        return self + other
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            
            tmpTup = ()
            for value in self.values:
                value = value - other
                tmpTup = tmpTup + (value,)
            self.values = tmpTup
            return self

            
        elif isinstance(other, Array):
            i = 0
            tmpTup = ()
            for value in self.values:
                value = value - other.values[i]
                i = i + 1
                tmpTup = tmpTup + (value,)
            self.values = tmpTup
            return self
        else:
            raise NotImplementedError("The values you are adding is not implemented")

        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        

    def __rsub__(self, other):
        return other - self
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        

    def __mul__(self, other):
        tmpTup = ()
        for value in self.values:
            value = value * other
            tmpTup = tmpTup + (value,)
        tmpArr = self
        tmpArr.shape = (len(tmpTup),)
        tmpArr.values = tmpTup
        return tmpArr
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        

    def __rmul__(self, other):
        return self * other
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        

    def __eq__(self, other):
        if isinstance(other, Array) == False:
            return False
        if self.shape != other.shape:
            return False
        
        return True
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """
        

    def is_equal(self, other):
        booltup = ()
        if self == other:
            for i in range(0, self.shape[0]):
                if self.values[i] != other.values[i]:
                    booltup = booltup + (False,)
                else:
                    booltup = booltup + (True,)
        elif isinstance(other, (int, float)):
            for value in self.values:
                if value == other:
                    booltup = booltup + (True,)
                else:
                    booltup = booltup + (False,)
        else:
            if isinstance(other, Array):
                raise ValueError("the two array shapes does not match")
        boolArr = deepcopy(self)
        boolArr.values = booltup
        return boolArr
        
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        
    
    def mean(self):
        total = 0
        for value in self.values:
            if isinstance(value, (int, float)):
                total = total + value
            else:
                raise ValueError("not numeric types in the array")
        return total / self.shape[0]
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        

    def variance(self):

        """
        total = 0
        for value in self.values:
            total = total + value
        var = 
        """

        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        pass

    def min_element(self):
        min = self.values[0]
        for value in self.values:
            if value < min:
                min = value
        return min
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
       