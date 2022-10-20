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
		return []
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
		return []
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
		return []
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
		return []
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
