# Write your solution here

def build_variables() -> dict:
	variables = {}
	letter = ord('A')
	for i in range(26):
		char = chr(letter)
		variables[char] = 0
		letter += 1
	return variables


def check_condition(a:str, operator:str, b:str, variables:dict) -> bool:
	if operator == '>':
		return a > b
	elif operator == '<':
		return a < b
	elif operator == '==':
		return a == b
	elif operator == '<=':
		return a <= b
	elif operator == '>=':
		return a >= b
	elif operator == '!=':
		return a != b
	return False


# PRINT [value]: prints the value
# MOV [variable] [value]: assigns the value to the variable
# ADD [variable] [value]: adds the value to the variable
# SUB [variable] [value]: subtracts the value from the variable
# MUL [variable] [value]: multiplies the variable by the value
# [location]:: names a line of code, so it can be jumped to from elsewhere
# JUMP [location]: jumps to the location specified
# IF [condition] JUMP [location]: if the condition is true, jump to the location specified
# END: finish execution

