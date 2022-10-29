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
		return []
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
		return False,[]
		#END TODO

if __name__ == "__main__":
	test13 = [6, 2, ["00111100", "01000001"], ["01101110", "11000000", "01000011", "00001101", "01010111", "10011010"], ["11100110", "01110101"]]
	test14 = [8, 20, ["00010101", "00110010", "11100001", "01011000", "11010101", "10000011", "01101010", "10101101", "11001000", "11010011", "11100000", "01100111", "10101111", "10111010", "11000101", "11000110", "10000111", "11010010", "11110100", "10000000"], ["00010101", "10010000", "01101010", "11101110", "00101111", "01110001", "11010001", "00101000"], ["10011000", "10010010", "11101111", "01010001", "11000101", "00000001", "00001110", "01110110", "00111011", "11111111", "00101111", "11100011", "11111111", "11001001", "10111101", "00100011", "10001110", "11000001", "10110101", "11100011"]]
	test15 = [10, 20, ["11111000", "01101000", "10101100", "00001111", "10111101", "10100011", "00000011", "00110001", "11001101", "11001111", "00001100", "01100101", "11111010", "01001101", "00010111", "10000110", "01000100", "11100110", "01010000", "10110011"], ["10111110", "01111110", "00111101", "11000110", "00110100", "00000101", "01010100", "11101010", "00010110", "00100001"], ["00111101", "10001011", "00000000", "10010100", "01000110", "11010111", "01010101", "00110101", "10000101", "00001110", "11100111", "11000110", "01101001", "11111110", "11111100", "00001100", "10101001", "10000001", "11000001", "01001100"]]
	test16 = [10, 40, ["01111110", "00001001", "11010000", "00111001", "10000111", "01111011", "00001100", "01011000", "01111001", "01111111", "10110001", "10110101", "01000010", "11110000", "01010110", "11111001", "10000100", "11101110", "01110001", "01100111", "01000111", "10100011", "11000111", "11110101", "01111100", "00101011", "00000110", "00110111", "01101100", "10010100", "11001010", "10011000", "10010000", "10101101", "01100010", "11101100", "11011111", "00010111", "11111000", "01101011"], ["01010111", "01110011", "11001001", "01000101", "11000100", "10010101", "11010000", "01100110", "10101101", "10100010"], ["01000101", "10000111", "00000111", "11100001", "01000110", "10011111", "11000110", "00011111", "10010100", "10111000", "11001001", "01101101", "11000000", "11001010", "00011110", "01011000", "00100111", "01000010", "10111111", "10100011", "11000111", "11101110", "11001101", "01011000", "00011110", "00000100", "11010110", "00011011", "11110001", "11101101", "11100000", "00100000", "01110010", "11011010", "11111101", "01000011", "10000101", "10111111", "10110110", "10111100"]]
    
	#4) Encoding tests	
	rs13 = ReedSolomon(test13[0],test13[1],test13[2])
	assert(rs13.encoding(test13[3])== test13[4])
	rs14 = ReedSolomon(test14[0],test14[1],test14[2])
	assert(rs14.encoding(test14[3])== test14[4])
	rs15 = ReedSolomon(test15[0],test15[1],test15[2])
	assert(rs15.encoding(test15[3])== test15[4])
	rs16 = ReedSolomon(test16[0],test16[1],test16[2])
	assert(rs16.encoding(test16[3])== test16[4])