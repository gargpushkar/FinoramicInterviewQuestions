def checkBraces(A):
	stack = []
	for a in A:
		if a == ')':
			b = stack.pop()
			if b == '(':
				return 1
			while b != '(':
				b = stack.pop()
		elif a == '(' or a == '/' or a == '*' or a == '-' or a == '+':
			stack.append(a)	
	return 0

A = input()
print(checkBraces(A))
