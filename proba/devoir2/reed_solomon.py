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

