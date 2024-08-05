# Numpy notes

# NumPy Arrays

## Introduction

NumPy arrays are a powerful data structure used in scientific computing with
Python. They allow for efficient storage and manipulation of numerical data, and
they form the backbone of many other scientific libraries in Python.

### Creating Arrays

#### 1. Basic Array

A NumPy array can be created from a Python list using `numpy.array`.

```python
import numpy as np

# Creating a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

#### 2. Array from List

Arrays can also be created from Python lists directly.

```python
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)
```

#### 3. Array from Dictionary
To create arrays from a dictionary, you can use the dictionary values.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
arr = np.array(list(my_dict.values()))
print(arr)
```

#### 4. `arange`

The `arange` function returns evenly spaced values within a given interval.

```python
# Creating an array with values from 0 to 9
arr = np.arange(10)
print(arr)

# Creating an array with values from 0 to 9 with step size of 2
arr = np.arange(0, 10, 2)
print(arr)
```

#### 5. `reshape`
The `reshape` function gives a new shape to an array without changing its data.

```python
arr = np.arange(10)
reshaped_arr = arr.reshape(2, 5)
print(reshaped_arr)
```

#### 6. `zeros`
The `zeros` function creates an array filled with zeros.

```python
# Creating a 1-dimensional array of zeros
zeros_arr = np.zeros(5)
print(zeros_arr)

# Creating a 2x3 array of zeros
zeros_arr_2d = np.zeros((2, 3))
print(zeros_arr_2d)
```

#### 7. `ones`
The `ones` function creates an array filled with ones.

```python
# Creating a 1-dimensional array of ones
ones_arr = np.ones(5)
print(ones_arr)

# Creating a 2x3 array of ones
ones_arr_2d = np.ones((2, 3))
print(ones_arr_2d)
```

#### 8. `eye`
The `eye` function creates a 2-D array with ones on the diagonal and zeros elsewhere.

```python
# Creating a 3x3 identity matrix
eye_arr = np.eye(3)
print(eye_arr)
```

### Array Attributes

#### 1. `shape`
The `shape` attribute returns the dimensions of the array.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)
```

#### 2. `dtype`
The `dtype` attribute returns the data type of the array elements.

```python
arr = np.array([1, 2, 3])
print(arr.dtype)  # Output: int64 (or int32 depending on the system)
```

### Array Operations

#### 1. Arithmetic Operations
NumPy arrays support element-wise arithmetic operations.

```python
arr = np.array([1, 2, 3, 4])
print(arr + 2)  # Output: [3 4 5 6]
print(arr * 2)  # Output: [2 4 6 8]
```

#### 2. Aggregate Functions
NumPy provides various functions to perform aggregate operations on arrays.

```python
arr = np.array([1, 2, 3, 4, 5])
print(arr.sum())  # Output: 15
print(arr.mean()) # Output: 3.0
```

### Indexing and Slicing

#### 1. Indexing
You can access array elements using indices.

```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # Output: 1
print(arr[-1]) # Output: 5
```

#### 2. Slicing

You can access a range of elements using slicing.

```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # Output: [2 3 4]
print(arr[:3])   # Output: [1 2 3]
print(arr[::2])  # Output: [1 3 5]
```

#####  Slicing Rows

```python
# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:\n", arr_2d)

# Slice the first two rows
print("First two rows:\n", arr_2d[:2])
```

#####  Slicing Columns

```python
# Slice the last two columns
print("Last two columns:\n", arr_2d[:, 1:])
```

##### Slicing Both Rows and Columns

```python
# Slice the first two rows and last two columns
print("First two rows, last two columns:\n", arr_2d[:2, 1:])
```

#### More Complex Slicing

You can also combine advanced indexing techniques like intervals (strides) in your slices.

#####  Skipping Rows or Columns

```python
# Skip every other row
print("Every other row:\n", arr_2d[::2])

# Skip every other column
print("Every other column:\n", arr_2d[:, ::2])

#Reverse Slicing
#Reversing the order of elements is another common use case.
# Reverse the entire array
print("Reversed array:\n", arr_2d[::-1])

# Reverse the order of columns
print("Reversed columns:\n", arr_2d[:, ::-1])
```

### Changing Values Using Filtering
```
You can change specific values in a NumPy array using filtering (also known as boolean indexing). This involves creating a boolean mask that identifies the elements to be changed and then applying the change.

```python
# Creating an array
arr = np.array([1, 2, 3, 4, 5])

# Creating a boolean mask where the condition is met
mask = arr == 3

# Changing the value 3 to 99
arr[mask] = 99
print(arr)  # Output: [ 1  2 99  4  5]

# Another example: changing all even numbers to -1
arr = np.array([1, 2, 3, 4, 5])
arr[arr % 2 == 0] = -1
print(arr)  # Output: [ 1 -1  3 -1  5]
```

### Sorting

NumPy provides functions to sort arrays. You can sort an array in-place or create a sorted copy of the array.

#### 1. Sorting a 1D Array

```python
arr = np.array([5, 3, 1, 4, 2])
sorted_arr = np.sort(arr)  # Returns a sorted copy
print(sorted_arr)  # Output: [1 2 3 4 5]

arr.sort()  # Sorts the array in-place
print(arr)  # Output: [1 2 3 4 5]
```

#### 2. Sorting a 2D Array by Rows or Columns

```python
arr = np.array([[3, 2, 1], [6, 5, 4]])

# Sort each row
sorted_arr_by_row = np.sort(arr, axis=1)
print(sorted_arr_by_row)  # Output: [[1 2 3] [4 5 6]]

# Sort each column
sorted_arr_by_col = np.sort(arr, axis=0)
print(sorted_arr_by_col)  # Output: [[3 2 1] [6 5 4]]
```

### Copying Arrays

There are two ways to copy arrays in NumPy: creating a view and creating a deep copy.

#### 1. View (Shallow Copy)

A view is a new array object that looks at the same data of the original array. Modifying the view will modify the original array as well.

```python
arr = np.array([1, 2, 3, 4, 5])
view_arr = arr.view()

view_arr[0] = 99
print(arr)  # Output: [99  2  3  4  5]
print(view_arr)  # Output: [99  2  3  4  5]
```

#### 2. Copy (Deep Copy)

A deep copy creates a new array with a copy of the data. Modifying the copy will not affect the original array.

```python
arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()

copy_arr[0] = 99
print(arr)  # Output: [1 2 3 4 5]
print(copy_arr)  # Output: [99  2  3  4  5]
```

## Numpy types


### Boolean Types
- `bool_`
  - Represents boolean (True or False) as a byte.

### Integer Types
- `int_` (equivalent to `int64` or `int32` depending on the platform)
  - Default integer type (same as `int` in Python).
- `intc` (equivalent to C `int` usually `int32` or `int64`)
  - Used for compatibility with C code.
- `intp` (used for indexing, equivalent to C `ssize_t`)
  - Used for indexing (same size as a pointer).
- `int8`
  - Byte (-128 to 127).
- `int16`
  - Integer (-32768 to 32767).
- `int32`
  - Integer (-2147483648 to 2147483647).
- `int64`
  - Integer (-9223372036854775808 to 9223372036854775807).

### Unsigned Integer Types
- `uint8`
  - Unsigned integer (0 to 255).
- `uint16`
  - Unsigned integer (0 to 65535).
- `uint32`
  - Unsigned integer (0 to 4294967295).
- `uint64`
  - Unsigned integer (0 to 18446744073709551615).

### Floating Point Types
- `float_` (equivalent to `float64`)
  - Double precision float: sign bit, 11 bits exponent, 52 bits mantissa.
- `float16`
  - Half precision float: sign bit, 5 bits exponent, 10 bits mantissa.
- `float32`
  - Single precision float: sign bit, 8 bits exponent, 23 bits mantissa.
- `float64`
  - Double precision float: sign bit, 11 bits exponent, 52 bits mantissa.

### Complex Number Types
- `complex_` (equivalent to `complex128`)
  - Complex number, represented by two 64-bit floats (real and imaginary components).
- `complex64`
  - Complex number, represented by two 32-bit floats (real and imaginary components).
- `complex128`
  - Complex number, represented by two 64-bit floats (real and imaginary components).

### Other Types
- `object_`
  - Any Python object stored in the array.
- `string_`
  - Fixed-length string type (each character takes up one byte).
- `unicode_`
  - Fixed-length unicode type (the size in bytes is platform-dependent).