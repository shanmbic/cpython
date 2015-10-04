from datetime import time, tzinfo, timedelta
class GMT1(tzinfo):
	def utcoffset(self, dt):
		return timedelta(hours=1)
	def dst(self, dt):
		return timedelta(0)
	def tzname(self,dt):
		return "Europe/Prague"
t = time(12, 10, 30, tzinfo=GMT1())
gmt = GMT1()
print(t.strftime('%:y'))