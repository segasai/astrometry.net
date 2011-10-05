class multiproc(object):
	def __init__(self, nthreads=1):
		if nthreads == 1:
			self.pool = None
			self.map = map
			self.apply = apply
		else:
			self.pool = multiprocessing.Pool(nthreads)
			self.map = self.pool.map
			self.apply = self.pool.apply_async
		self.async_results = []

	def apply(self, f, args, kwargs):
		if self.pool is None:
			return apply(f, args, kwargs)
		res = self.apply(f, args, kwargs)
		self.async_results.append(res)
		return res

	def waitforall(self):
		print 'Waiting for async results to finish...'
		for r in self.async_results:
			print '  waiting for', r
			r.wait()
		print 'all done'
		self.async_results = []