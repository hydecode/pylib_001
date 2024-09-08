# This example is a Python script
# Python is used to open Big Class and create columns for BMI and Odd/Even
# The data table and number of rows are sent to Python

# The Python code imports a function library that contains odd_even and divide
# These functions are used to fill in the columns for BMI and Odd/Even

def bmimain():
	import jmp
	import sys

	# adding folder with python code to the system path
	sys.path.insert(1, '/Python/Function Libraries')
	# importing the odd_even and divide functions
	from library1 import odd_even, divide

	# open Big Class and calculate bmi
	dt = jmp.open(jmp.SAMPLE_DATA + "Big Class.jmp")
	dt.new_column('BMI', jmp.DataType.Numeric)
	dt.new_column('Odd/Even', jmp.DataType.Character)

	for j in range( dt.nrows ):
		dt['BMI'][j] = divide(dt['weight'][j], dt['height'][j])
		dt['Odd/Even'][j] = odd_even(dt['age'][j])
