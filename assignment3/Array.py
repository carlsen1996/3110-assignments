from copy import deepcopy

class Array:
    # Assignment 3.3  

    def __init__(self, shape, *values):
        self.shape = shape
        self.values = values
        """This checks if all values in the array is the same type"""
        fileType = type(self.values[0])
        for value in self.values:
            if type(value) != fileType:
                raise ValueError("The data types in the array are not the same")
        """Here it checks if the values added corresponds with the shape"""
        sum = 1
        for i in self.shape:
            sum = sum * i
        if len(self.values) != sum:
            raise ValueError("The number of values does not match the shape")
        
        """
        This builds up a 2-dimentional tuple to be able to print it out and use the __getitem__ function properly
        It builds up tuples and adding the thuples in other tuples so it looks properly
        """
        if len(self.shape) > 1:
            count = 0
            self.twoDTup = ()
            for i in range(0, self.shape[0]):
                tmpTup1 = ()
                for j in range(0, self.shape[1]):
                    tmpTup1 = tmpTup1 + (self.values[count],)
                    count = count + 1
                self.twoDTup = self.twoDTup + (tmpTup1,)
            

        
        
        
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
        """This prints out the array so it looks nice and proper. This will not work with dimentions over 2"""
        if len(self.shape) == 1:
            return str(self.values).strip("()")
        else:
            #return str(self.twoDTup)
            return str(self.values).strip("()")
            

        
        
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
    def __getitem__(self, key):
        """
        This function gets the key value from the array. If the array is 2-dimentional it can be used with two brackets to get
        specific values from the tuples. This only work with 1-dimetional and 2-dimentional
        """
        if len(self.shape) > 1:
            return self.twoDTup[key]
        else:
            return self.values[key]


    def __add__(self, other):
        """
        this function adds up all the numbers in the array with either a numeric value, or it adds up the values from
        another array from the same places, or if its a multidimentional array it can take in tuples to add up respectivly
        This work with all kinds of dimentions
        """
        if isinstance(other, (int, float)):
            """Here it goes through all the values and adds up with the numeric value"""
            tmpTup = ()
            for value in self.values:
                value = value + other
                tmpTup = tmpTup + (value,)
            self.values = tmpTup
            return self
        elif isinstance(other, Array):
            """This takes in an array and adds the number from the same places in the arrays"""
            if self.shape == other.shape:
                i = 0
                tmpTup = ()
                for value in self.values:
                    value = value + other.values[i]
                    i = i + 1
                    tmpTup = tmpTup + (value,)
                self.values = tmpTup
                return self
            else:
                raise ValueError("the shapes does not match")
            
        
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
        """This one does the same as __add__, but it can be taken in reversed"""
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
        """this one works the same as __add__, except it subtracts instead of add"""
        if isinstance(other, (int, float)):
            tmpTup = ()
            for value in self.values:
                value = value - other
                tmpTup = tmpTup + (value,)
            self.values = tmpTup
            return self
        elif isinstance(other, Array):
            if self.shape == other.shape:
                i = 0
                tmpTup = ()
                for value in self.values:
                    value = value - other.values[i]
                    i = i + 1
                    tmpTup = tmpTup + (value,)
                self.values = tmpTup
                return self
            else:
                raise ValueError("The shapes does not match")
            
        elif isinstance(other, tuple):
            i = 0
            if isinstance(other[0], (int, float)):
                tmpTup = ()
                while i < len(self.values):
                    for value in other:
                        val = self.values[i] - value
                        tmpTup = tmpTup + (val,)
                        i = i + 1
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
        """This works the same as __radd__ except it subtracts instead of adds"""
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
        """This will multiply all values in the array with a numeric value or an array"""
        if isinstance(other, (float, int)):
            tmpTup = ()
            for value in self.values:
                value = value * other
                tmpTup = tmpTup + (value,)
            tmpArr = self
            tmpArr.shape = (len(tmpTup),)
            tmpArr.values = tmpTup
            return tmpArr
        elif isinstance(other, Array):
            i = 0
            if self == other:
                for value in self.values:
                    value = value * other.values[i]
                    i = i + 1
                return self
            else:
                raise ValueError("the shapes does not match")
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        

    def __rmul__(self, other):
        """This works as __mul__ but reverse"""
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
        """This checks if the arrays have the same shapes"""
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
        """
        This checks if the values in the array is equal to another array or a numeric value and returns a new array with
        truths of falses for each value
        """
        booltup = ()
        if self == other:
            for i in range(0, len(self.values)):
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
        """This finds the mean value of all the values in the array"""
        total = 0
        for value in self.values:
            if isinstance(value, (int, float)):
                total = total + value
            else:
                raise ValueError("not numeric types in the array")
        return total / len(self.values)
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        

    def variance(self):
        """This finds out the variance of the array using the respective formula"""
        

        mean = self.mean()
        var = 0
        for value in self.values:
            var = var + ((value - mean)**2)
        
        return var
        

        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        pass

    def min_element(self):
        """This finds the smallest value in the array"""
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

"""
I got almost all of the functions to work with n-dimentional arrays except __str__ and __getitem__ 
wich only work for 1 and 2-dimentinal arrays
"""