class StringConverter:
	def __init__(self, char):
		self.pos = 0
		self.char = char
		self.minus = False
		self.is_float = False
		
		if self.is_minus() == True:
			self.char = self.char[1:]
			self.minus = True

		
		# print(self.minus)
		self.origin = len(self.char) - 1
		if (b:=self.find_dot()) != 0:
			self.origin = b - 1
			self.is_float = True
		
		# reset position
		self.pos = 0

		super().__init__()
	
	# 飛び出てませんか？
	def is_eof(self):
		return len(self.char) <= self.pos

	# これはマイナスの値ですか？
	def is_minus(self):
		return self.char[0] == '-'

	def get_char(self):
		return self.char[self.pos]

	def consume_char(self):
		c = self.get_char()
		self.pos += 1
		return c
	
	def exchange(self, s_num):
		assert(s_num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

		if s_num == '0':
			return 0
		elif s_num == '1':
			return 1
		elif s_num == '2':
			return 2
		elif s_num == '3':
			return 3
		elif s_num == '4':
			return 4
		elif s_num == '5':
			return 5
		elif s_num == '6':
			return 6
		elif s_num == '7':
			return 7
		elif s_num == '8':
			return 8
		elif s_num == '9':
			return 9
	
	def find_dot(self):
		appered_dot = False
		origin = 0
		if self.get_char() == '.':
			raise SyntaxError('You cannot place a dot in the first digit.')

		while self.is_eof() == False:
			c = self.consume_char()
			if c != '.':
				if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
					# 変な文字が含まれていないか。
					raise SyntaxError('Not allowed character.')
				else:
					continue
			else:
				if appered_dot == True:
					# ドットがすでに出てきていないか。
					raise SyntaxError('Not allowed continuas dots.')
				else:
					origin = self.pos
					appered_dot = True
		return origin
	
	def calculate_range_from_origin(self):
		numbs = []
		while self.is_eof() == False:
			if self.is_float == True:
				if self.pos < self.origin:
					c = self.consume_char()
					c = self.exchange(c)
					numbs.append(c * (10 ** (self.origin - self.pos)))
				else:
					c = self.consume_char()
					if c == '.':
						continue
					c = self.exchange(c)
					numbs.append(c * (10 ** -(self.pos - self.origin - 1)))
			else:
				c = self.consume_char()
				c = self.exchange(c)
				numbs.append(c * (10 ** (self.origin - self.pos +1)))
		return numbs
	
	def convert(self):
		i = 0
		for cal in self.calculate_range_from_origin():
			i += cal
		
		if self.minus == True:
			i *= -1
		
		# print(f'{i} (float: {self.is_float})')
		return i


# st = StringConverter(
# 	'-300.1'
# )
# r = st.calculate_range_from_origin()
# print(r)

# st = StringConverter(
# 	'30.1'
# )
# r = st.calculate_range_from_origin()
# print(r)


# st = StringConverter(
# 	'5000'
# )
# r = st.calculate_range_from_origin()
# print(r)