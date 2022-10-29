import numpy

class BinaryDomains():

	def toBinary(self, n):
		"""
		Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

		Args:
			n (int): L'entier à convertir en représentation binaire 8 bits.
		Returns:
			string: Forme binaire de l'entier en string.
		"""
		return ''.join(str(1 & int(n) >> i) for i in range(8)[::-1])
	
	def add(self, x, y):
		"""
		Additionne deux séquences binaires (x+y) reçues sous la forme de string.

		Example : "10111001" + "10010100" = "00101101".

		Args:
			x (string): Premier élément de l'addition.
			y (string): Deuxième élément de l'addition.

		Returns:
			string: Résultat de l'addition x+y en binaire.
		"""

		#BEGIN TODO
		return "".join(str(int(x[i])^int(y[i])) for i in range(len(x)))
		#END TODO

	def multiply(self, x, y):
		"""
		Multiplie deux séquences binaires (x*y) reçues sous la forme de string, en utilisant
        le polynôme irréductible choisi pour le corps.

		Example : "10111001" * "10010100" = "10110010".

		Args:
			x (string): Premier élément de la multiplication.
			y (string): Deuxième élément de la multiplication.

		Returns:
			string: Résultat de la multiplication x*y en binaire.
		"""
		#BEGIN TODO
		Px = "101001101"
		mult = "00000000"
		while y != "00000000":
			if y[-1] == '1':
				mult = self.add(mult, x)
				y = self.add(y, "00000001")
			if x[0] == "1":
				x = self.add("1" + self.toBinary(int(x, 2) << 1),Px)[1:] 
			else:
				x = self.toBinary(int(x, 2) << 1)
			y = self.toBinary(int(y, 2) >> 1)
		return mult
		#END TODO

	def inverse(self, x):
		"""
		Inverse un élément (x^(-1)) du corps donné sous la forme d'une séquence binaire.

		Example : ("10111001")^(-1) = "10001110".

		Args:
			x (string): Elément à inverser.

		Returns:
			string: Résultat de l'inversion en binaire.
		"""
		#BEGIN TODO
		inv = "00000001"
		for i in range(len(x)-1):
			x = self.multiply(x, x)
			inv = self.multiply(inv, x)
		return inv
		#END TODO

class ReedSolomon():
	def __init__(self, k, n, x):
		"""
		Args:
			k (int): dimension des messages à transmettre.
			n (int): taille du bloc que l'on souhaite transmettre.
			x (liste de string de taille n): les points Xi.
		"""
		self.f = BinaryDomains()
		self.k = k
		self.n = n
		self.x = x

	def encoding(self, message_original):
		"""
		Encode le message à stocker sous la forme d'une liste comportant k bytes/octets.

		Exemple:
			k = 4 | n = 6 | x = ["00000000", "00000001", "00000010", "00000011", "00000100", "10000000"].
			message_original = ["11010000", "10110001", "11100110", "11111111"].
			-> retourne : ["11010000", "01111000", "10100101", "00111001", "01111111","00111001"].
		
		Args:
			message_original (liste de string de taille k): Le message original a encodé.
		
		Returns:
			(liste de string de taille n): Le message encodé.
		"""
		#BEGIN TODO
		A = []
		bd = BinaryDomains()
		for X in self.x:
			a = message_original[0]
			pow = X
			for d in range(1,self.k):
				a = bd.add(a, bd.multiply(message_original[d], pow))
				pow = bd.multiply(X, pow)
			A.append(a)
		return A
		#END TODO

	def gaussian_elimination(self, X, AX):
		"""
		Ex: k = 4: retourne les coefficients (di) de la fonction A(Xi) = d0 + d1*Xi + d2*Xi^2 + d3*Xi^3
		en partant de 4 points (Xi,A(Xi)).

		Ce problème est généralisé pour tout k.
		Pour le résoudre -> Effectuer l'élimination de Gauss-Jordan sur le système Vx = a.
		Avec V la matrice de Vandermonde.
		
		Args:
			X (liste de string de taille k): Les points Xi.
			AX (liste de string de taille k): Les points A(Xi).
		
		Returns:
			(liste de string de taille k): Les coefficients (di) de l'interpolation.
		"""
		#BEGIN TODO
		bd = BinaryDomains()
		P = [] #augmented matrix (V|a)
		d = [] #vector containing the message 
		#we have to create the normal matrix V
		for z in range(self.k):
			row = [bd.toBinary(1)]
			pow = X[z]
			for lolz in range(self.k-1):
				row.append(pow)
				pow = bd.multiply(pow,X[z])
			P.append(row)
		#we add the vector a to the matrix V
		for indx in range(self.k):
			P[indx].append(AX[indx])
		#gaussian_elimination algorithm 2 of the document
		for i in range(self.k):
			for j in range(self.k):
				if i != j:
					r = bd.multiply(P[j][i],bd.inverse(P[i][i]))
					for m in range(self.k+1):
						P[j][m] = bd.add(P[j][m],bd.multiply(r, P[i][m]))
		for i in range(self.k):
			d.append(bd.multiply(P[i][self.k], bd.inverse(P[i][i])))
		return d
		#END TODO

	def decoding(self, message_corrupted):
		"""
		Décode le message corrompu sous la forme d'une liste comportant k bytes.

		Args:
			message_corrupted (liste de string de taille n): Le message 'corrompu' reçu.
		
		Returns:
			(bool): True s'il est possible de décoder le message corrompu, False sinon.
			(liste de string de taille n): Le message décodé. (si bool = False, alors retourner []).
		"""
		#BEGIN TODO
		nonCorrupted = []
		for msgIndx in range(len(message_corrupted)):
			add = True
			try:
				int(message_corrupted[msgIndx],2)
				if len(message_corrupted[msgIndx]) != 8:
					add = False
			except ValueError:
				add = False
			if add:
				nonCorrupted.append((message_corrupted[msgIndx],msgIndx))
		if len(nonCorrupted) < self.k:  #if we have less than k messages, we can't decode it 
			return False,[]
		else: #other wise we can decode it
			X = []
			AX = []
			for K in range(self.k):
				X.append(self.x[nonCorrupted[K][1]]) #Xi points 
				AX.append(nonCorrupted[K][0]) #A(Xi) points 
			return True,self.gaussian_elimination(X,AX)
		#END TODO

if __name__ == "__main__":
	test17 = [6, 10, ["00100010", "01011001", "01111010", "11000101", "01010111", "11110111", "00100101", "00100100", "10001011", "10010010"], ["01111010", "1101a011", "1s10q001", "11110000", "11001111", "10111111", "00f10001", "00010001", "00111001", "h1110101"], ["00111010", "11000010", "01111110", "00100001", "11001111", "00001001"]]
	test18 = [8, 20, ["01110110", "11111010", "11000001", "10101010", "00101000", "00000100", "10100000", "11110101", "00100011", "00110110", "00001000", "11111100", "00111100", "11111011", "10011010", "01010000", "01100000", "10011100", "00110101", "11101110"], ["11111111", "001x1111", "0k11110v", "00010100", "01001010", "10000111", "11p10111", "01y01101", "0et11111", "011b1110", "1101k1w1", "r11i0010", "1lt10001", "0c0r0010", "10011010", "000qbf01", "z1001001", "00110110", "01111000", "11010111"], ["00001101", "00010010", "10001011", "01100000", "01001010", "01100000", "11011100", "00100110"]]
	test19 = [10, 20, ["01100010", "00010111", "11110011", "10001001", "10101100", "11011100", "00001110", "01100111", "11011000", "11000001", "00101000", "10110100", "10001100", "11011110", "11001010", "01011000", "11100110", "01001001", "01111110", "11100101"], ["10000101", "1a0e0010", "100w1r11", "11010111", "u10h101j", "100110r0", "11001000", "00001110", "r1011100", "101i0v00", "11110111", "10011001", "11001j10", "01101101", "00101101", "1b1c1110", "00110000", "000000hq", "01110110", "0100b100"], ["01011010", "01100101", "01111100", "10101100", "10001011", "01011011", "01010001", "01100101", "10100001", "00010011"]]
	test20 = [10, 40, ["11101010", "00101100", "11110011", "10010101", "00110110", "11011110", "01010011", "01000111", "00001110", "11100010", "11011011", "01111011", "10101111", "10011000", "00110000", "01100101", "10101000", "11000100", "01000001", "11101110", "00011111", "10011111", "11011100", "10111101", "10100000", "11000011", "11000111", "00000100", "10001101", "01110010", "01111010", "01011001", "10110111", "00100111", "11000010", "11111110", "00000110", "10111000", "11100001", "10110000"], ["01e0ki11", "10110011", "i01u0m0q", "1j001r00", "01001010", "10111w0h", "0011l000", "1e11111h", "01111111", "11g0101u", "00001u00", "11111111", "010001m1", "00r001h0", "10101010", "11101be0", "0100111f", "0011q100", "11sk1000", "101e0b00", "100p0110", "10000111", "j0cwv100", "10100101", "00110000", "a0p11010", "111iyg1n", "11100101", "1111111j", "1cs0np00", "1z10101g", "01t00101", "m1j00011", "0010ya00", "100rt100", "11000000", "1k001110", "10001x01", "0c0u1011", "00n011n0"], ["01111110", "10110010", "01001101", "00001100", "00100001", "00000000", "11000001", "01100111", "11100100", "00010100"]]
	test21 = [6, 10, ["10001111", "10011101", "10100101", "00110110", "00000010", "01101001", "00000101", "10100111", "11011101", "10000011"], ["01011011", "10111001", "00010101", "11110100", "00110001", "10010011", "1110011", "0111001", "0010101", "0100101"], ["01110100", "00101110", "01011110", "01101001", "00001100", "10010010"]]
	test22 = [8, 20, ["10101001", "11001010", "00110000", "10010010", "10110001", "10101000", "01111111", "01000000", "10010101", "01101011", "00101000", "10101010", "11100100", "11010010", "10111000", "01011000", "00010101", "01101001", "01000101", "11011011"], ["10101001", "000010", "00011010", "11100111", "101010", "00111001", "1011010", "00010", "1010", "111000", "1101001", "000000", "010100", "110011", "00011111", "00110011", "0101", "10110011", "00000110", "1100101"], ["00110100", "00001100", "00000111", "10101111", "11110111", "01010000", "00101111", "01100010"]]
	test23 = [10, 20, ["01110101", "10001111", "01101111", "00101110", "10100111", "01000100", "10001010", "00111100", "10011010", "00100101", "01000111", "01101100", "10011001", "11000011", "00110110", "10000010", "00101001", "11011011", "10101010", "01110000"], ["11110010", "11010", "00101111", "10111110", "0100011", "10100", "00100", "1001011", "0010111", "10010000", "0001000", "1001101", "1111100", "10100010", "01010100", "01", "00011000", "01001001", "01010001", "10011011"], ["00101000", "11001001", "00001101", "00100111", "11011110", "00000010", "11101110", "00111010", "11111001", "11011110"]]
	test24 = [10, 40, ["00101010", "11010100", "10010100", "01111101", "00011110", "11010110", "11010111", "01011110", "11000010", "00010101", "11000101", "10011001", "11100001", "00000011", "10010000", "00000101", "11111101", "10101010", "11011101", "11110010", "11111001", "00000110", "00110110", "01001110", "10000100", "11001000", "01100110", "10011000", "00010100", "10101011", "00000100", "00011111", "10001110", "01011010", "01001101", "10100001", "01101100", "10100011", "10000000", "10010001"], ["11111101", "100101", "101011", "01000101", "1010010", "0011100", "0000001", "0110111", "010000", "0000111", "0011111", "00100000", "1100110", "0001000", "01000100", "010101", "1100010", "001001", "00010110", "111111", "101010", "111100", "010001", "1011110", "111010", "001011", "000111", "011100", "01000010", "1011101", "00011110", "100101", "0010101", "10101010", "00001111", "0100011", "000101", "0100111", "011000", "01010000"], ["11110100", "10011111", "01100000", "01001101", "11001000", "00100111", "01001001", "10101111", "01101101", "00000110"]]

	#5) Decoding tests 1
	rs17 = ReedSolomon(test17[0],test17[1],test17[2])
	assert(rs17.decoding(test17[3])[1]== test17[4])
	rs18 = ReedSolomon(test18[0],test18[1],test18[2])
	assert(rs18.decoding(test18[3])[1]== test18[4])
	rs19 = ReedSolomon(test19[0],test19[1],test19[2])
	assert(rs19.decoding(test19[3])[1]== test19[4])
	rs20 = ReedSolomon(test20[0],test20[1],test20[2])
	assert(rs20.decoding(test20[3])[1]== test20[4])

	#6) Decoding tests 2
	rs21 = ReedSolomon(test21[0],test21[1],test21[2])
	assert(rs21.decoding(test21[3])[1]== test21[4])
	rs22 = ReedSolomon(test22[0],test22[1],test22[2])
	assert(rs22.decoding(test22[3])[1]== test22[4])
	rs23 = ReedSolomon(test23[0],test23[1],test23[2])
	assert(rs23.decoding(test23[3])[1]== test23[4])
	rs24 = ReedSolomon(test24[0],test24[1],test24[2])
	assert(rs24.decoding(test24[3])[1]== test24[4])