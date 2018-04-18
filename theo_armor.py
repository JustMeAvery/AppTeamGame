class armor:
	def __init__(self, dur):
		self.dur = dur

class breastplate(armor):
	def __init__(self):
		super(breastplate,self).__init__(400)

class helm(armor):
	def __init__(self):
		super(helm,self).__init__(300)

class platelegs(armor):
	def __init__(self):
		super(platelegs,self).__init__(350)

class shield(armor):
	def __init__(self):
		super(shield,self).__init__(500)