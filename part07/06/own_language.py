# Write your solution here

from string import ascii_uppercase

def main():
	program1 = ['MOV A 1', 'MOV B 2', 'PRINT A', 'PRINT B', 'ADD A B', 'PRINT A', 'END']
	result = run(program1)
	print(result)
		# [1, 2, 3]
	program2 = ['MOV A 1', 'MOV B 10', 'begin:', 'IF A >= B JUMP quit', 'PRINT A', 'PRINT B', 'ADD A 1', 'SUB B 1', 'JUMP begin', 'quit:', 'END']
	result = run(program2)
	print(result)
		# [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
	program3 = ['MOV A 1', 'MOV B 1', 'begin:', 'PRINT A', 'ADD B 1', 'MUL A B', 'IF B <= 10 JUMP begin', 'END']
	result = run(program3)
	print(result)
		# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
	program4 = ['MOV N 50', 'PRINT 2', 'MOV A 3', 'begin:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP error', 'IF C > A JUMP over', 'ADD C B', 'JUMP new', 'error:', 'MOV Z 1', 'JUMP over2', 'over:', 'ADD B 1', 'IF B < A JUMP test', 'over2:', 'IF Z == 1 JUMP over3', 'PRINT A', 'over3:', 'ADD A 1', 'IF A <= N JUMP begin']
	result = run(program4)
	print(result)
		# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
	prog = ['MOV A 1', 'MOV B 1', 'start:', 'MUL A 2', 'ADD B 1', 'IF B != 101 JUMP start', 'PRINT A']
	result = run(prog)
	print(result)
		# [1267650600228229401496703205376]
	exit()


def build_variables() -> dict:
	variables = {}
	letter = ord('A')
	for i in range(26):
		char = chr(letter)
		variables[char] = 0
		letter += 1
	return variables


def get_ab_values(orig_a:str, orig_b:str, variables:dict) -> tuple:
	a = orig_a
	if orig_b in ascii_uppercase:
		b = variables[orig_b]
	else:
		b = int(orig_b)
	return (a, b)


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

main()
