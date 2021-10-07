import math

# deghat baraye mosavi bodan adad
epsilon = 1e-12

# bode matrice vorodi dade shode
n = int(input())

# tabe baraye namayesh matrice
def print_matrix(A):
	for i in range(len(A)):
		for j in range(len(A[i])):
			print ("%.6f" % A[i][j], end = " ")
		print()
	print()

# tabe baraye zarbe do matrice n dar n
def multiply(A, B):
	result = []
	for i in range(n):
		result.append([0 for j in range(n)])

	for i in range(n):
		for j in range(n):
			for k in range(n):
				result[i][j] += A[i][k] * B[k][j]
	return result

# matrice givens baraye davarane khane (row, col) ba zavie ke cosinos aan barabare c va sinos aan barabare s ast
def givens(row, col, c, s):
	G = []
	for i in range(n):
		G.append([0 for j in range(n)])
	for i in range(n):
		G[i][i] = 1

	G[row][row] = c
	G[col][col] = c
	G[row][col] = s
	G[col][row] = -s
	return G

# bedast avordan tajzie QR
def QR(A):

	# ebteda Q ra matrice hamani gharar midahim
	Q = []
	for i in range(n):
		Q.append([0 for j in range(n)])
	for i in range(n):
		Q[i][i] = 1

	# baraye sotoone i mikhahim satr haie i + 1 ta n - 1 ra 0 konim
	for i in range(n):
		# deraie (i, i) matrix ra ba meghdari nasfer az aan sotoon jaigozin mikonim
		if abs(A[i][i]) < epsilon :
			for j in range(i + 1, n):
				if abs(A[j][i]) >= epsilon:
					A[j], A[i] = A[i], A[j]
					break

		# agar (i, i) nasefri mojood nabashad matrice voroodi dade shode varoon pazir nist
		if abs(A[i][i]) < epsilon:
			print("Matrix is not inversable!")
			exit()

		# baraye tam satr ha i + 1 ta n - 1 mannade j mikhahim ba komake A[i][i] meghdare A[j][i] ra sefr konim
		for j in range(i + 1, n):
			r = math.sqrt(A[j][i] * A[j][i] + A[i][i] * A[i][i])
			c, s = A[i][i] / r, -A[j][i] / r
			A = multiply(givens(j, i, c, s), A) # A ra dar matrice givens(j, i, c, s) zarb konim A[j][i] sefr mishavad
			Q = multiply(Q, givens(j, i, c, -s)) # givens(j, i, c, -s) haman varoon givens(j, i, c, s) ast

	return [Q, A]

#voroodi gereftan az karbar
A = []
for i in range(n):
	A.append([int(num) for num in input().split(' ')])


# print kardan javab
Q, R = QR(A)
print ("Q:")
print_matrix(Q)
print("R: ")
print_matrix(R)