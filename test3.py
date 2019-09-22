from __future__ import division
import copy

class Fraction:
	def __init__(self, top, bottom):
		def gcd(m, n):
			if n == 0:
				return 1
			while m % n != 0:
				old_m = m
				old_n = n
				m = old_n
				n = old_m % old_n
			return n
		common = gcd(top,bottom)
		self.num = top/common
		self.den = bottom/common
	def toFloat(self):
		return self.num/self.den
	def __str__ (self):
		if self.den.is_integer():
			returnStr = '(' + str(int(self.num)) + '/'
		else:
			returnStr = '(' + str(self.num) + '/'
		if self.den.is_integer():
			returnStr += str(int(self.den)) + ')'
		else:
			returnStr += '(' + str(self.den) + '/'
		return returnStr
	def get_num(self):
		return self.num
	def get_den(self):
		return self.den
	def __add__(self, other_fraction):
		new_num = self.num * other_fraction.den + self.den * other_fraction.num
		new_den = self.den * other_fraction.den
		return Fraction(new_num, new_den)
	def __sub__(self, other_fraction):
		new_num = self.num * other_fraction.den - self.den * other_fraction.num
		new_den = self.den * other_fraction.den
		return Fraction(new_num, new_den)
	def __mul__ (self, other_fraction):
		new_num = self.num * other_fraction.num
		new_den = self.den * other_fraction.den
		return Fraction(new_num, new_den)
	def __truediv__(self, other_fraction):
		new_num = self.num * other_fraction.den
		new_den = self.den * other_fraction.num
		return Fraction(new_num, new_den)

	def __eq__(self, other):
		first_num = self.num * other.den    
		second_num = other.num * self.den
		return first_num == second_num

def prMatrix(matrix):
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[i])):
			print(matrix[i][j], end=' ')
			#print(round(matrix[i][j].toFloat(), 2), end=' ')
		print()
	print()

#matrix = [[ 2, 5,-1, 0, 0, 16],
#		  [ 4, 1, 0,-1, 0, 9],
#		  [ 3, 2, 0, 0,-1, 13],
#		  [-6, -1, 0, 0, 0, 0]
#		]

#Z1 = [Fraction(-6, 1), Fraction(-1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]

matrix = [[2, 4, 0, 3, 1, 0, 0, 120],
		  [7, 0, 0, 6, 0, 1, 0, 100],
		  [5, 8, 4, 3, 0, 0, 1, 480],
		  [3, 4, 3, 2, 0, 0, 0]
		]

Z1 = [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]
S = [0, 0, 0]
C = [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]

for i in range(0, len(matrix)):
	for j in range(0, len(matrix[i])):
		matrix[i][j] = Fraction(matrix[i][j], 1)

prMatrix(matrix)

#for k in range(1, len(matrix)):
#	clonMatrixclonMatrix = copy.deepcopy(matrix)
#	matrix[k-1] = [j / clonMatrixclonMatrix[k-1][k-1] for j in matrix[k-1]]
#	for i in range(k, len(matrix)):
#		matrix[i][k-1] = Fraction(0, 1)
#		for j in range(k, len(matrix[i])):
#			matrix[i][j] = clonMatrixclonMatrix[k-1][k-1] * clonMatrixclonMatrix[i][j] - \
#						   clonMatrixclonMatrix[i][k-1] * clonMatrixclonMatrix[k-1][j]

#	prMatrix(matrix)


#for k in range(1, len(matrix)):
#	clonMatrixclonMatrix = copy.deepcopy(matrix)
#	matrix[k-1] = [j / clonMatrixclonMatrix[k-1][k-1] for j in matrix[k-1]]
#	for i in range(0, len(matrix)):
#		if i == k-1: continue
#		for j in range(0, len(matrix[i])):
#			matrix[i][j] = clonMatrixclonMatrix[i][j] - (clonMatrixclonMatrix[k-1][j] * \
#						   clonMatrixclonMatrix[i][k-1] / clonMatrixclonMatrix[k-1][k-1])

#	prMatrix(matrix)

#a_min1 = Fraction(-1, 1)
#matrix[0] = [i*a_min1 for i in matrix[0]]
#matrix[1] = [i*a_min1 for i in matrix[1]]
#matrix[2] = [i*a_min1 for i in matrix[2]]
#prMatrix(matrix)

for j in range(0, len(Z1)):
	Z1[j] = C[0]*matrix[0][j] - matrix[len(matrix)-1][j]
	print(Z1[j])

a = copy.deepcopy(matrix)

Z = [i.toFloat() for i in matrix[len(matrix)-1]]
col_indexMin = l = Z.index(min(Z))	# l element
print(col_indexMin)
for i in range(0, len(S)):
	if matrix[i][col_indexMin].toFloat() != 0:
		S[i] = matrix[i][len(matrix[i])-1] / matrix[i][col_indexMin]
	else:
		S[i] = matrix[i][len(matrix[i])-1]
Z = [i.toFloat() for i in S]
row_indexMin = k = Z.index(min(Z))	# k element
print(row_indexMin)
C[0] = a[k][l]

for i in range(0, len(matrix)-1):
	if i != k:
		matrix[i][len(matrix[i])-1] = a[i][len(a[i])-1] - ((a[k][len(a[i])-1]*a[i][l])/a[k][l])
	else:
		matrix[i][len(matrix[i])-1] = a[k][len(matrix[i])-1]/a[k][l]

for i in range(0, len(matrix)):
	for j in range(0, len(matrix[i])-1):
		if i != k:
			matrix[i][j] = a[i][j] - ((a[k][j] * a[i][l])/a[k][l])
		else:
			matrix[i][j] = a[k][j]/a[k][l]

prMatrix(matrix)
#for j in range(0, len(matrix[len(matrix)-1])-1):
	#if l != j:
	#print(C[0]*matrix[0][j]+C[1]*matrix[1][j]+C[2]*matrix[2][j], Z1[j])
#	matrix[len(matrix)-1][j] = C[0]*matrix[0][j] + C[1]*matrix[1][j] + C[2]*matrix[2][j] + Z1[j]
	#else:
	#	matrix[len(matrix)-1][j] = Fraction(0, 1)

#prMatrix(matrix)


exit()
a = copy.deepcopy(matrix)

Z = [i.toFloat() for i in matrix[len(matrix)-1]]
col_indexMin = l = Z.index(min(Z))	# l element
print(col_indexMin)
for i in range(0, len(S)):
	if matrix[i][col_indexMin].toFloat() != 0:
		S[i] = matrix[i][len(matrix[i])-1] / matrix[i][col_indexMin]
	else:
		S[i] = matrix[i][len(matrix[i])-1]
Z = [i.toFloat() for i in S]
row_indexMin = k = Z.index(min(Z))	# k element
print(row_indexMin)
C[1] = a[k][l]

for i in range(0, len(matrix)-1):
	if i != k:
		matrix[i][len(matrix[i])-1] = a[i][len(a[i])-1] - ((a[k][len(a[i])-1]*a[i][l])/a[k][l])
	else:
		matrix[i][len(matrix[i])-1] = a[k][len(matrix[i])-1]/a[k][l]

for i in range(0, len(matrix)):
	for j in range(0, len(matrix[i])-1):
		if i != k:
			matrix[i][j] = a[i][j] - ((a[k][j] * a[i][l])/a[k][l])
		else:
			matrix[i][j] = a[k][j]/a[k][l]


#for j in range(0, len(matrix[len(matrix)-1])-1):
#	matrix[len(matrix)-1][j] = C[0]*matrix[0][j] + C[1]*matrix[1][j] + C[2]*matrix[2][j] + Z1[j]

prMatrix(matrix)
print(C[0], ' ', C[1])