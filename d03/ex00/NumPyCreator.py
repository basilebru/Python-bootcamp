import numpy as np

class NumPyCreator:
	def from_list(self, lst):
		print(np.array(lst))
	def from_tuple(self, tpl):
		print(np.array(tpl))
	def from_iterable(self, itr):
		#print(np.fromiter(itr, float))
		print(np.array(itr))
	def from_shape(self, shape, value = 0):
		print(np.full(shape, value))
	def random(self, shape):
		print(np.random.random_sample(shape))
	def identity(self, n):
		print(np.identity(n))
