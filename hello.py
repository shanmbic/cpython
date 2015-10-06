from datetime import time, tzinfo, timedelta, datetime
class GMT1(tzinfo):
	def utcoffset(self, dt):
		return timedelta(hours=1)
	def dst(self, dt):
		return timedelta(hours=1)
	def tzname(self,dt):
		return "Europe/Prague"
tz = GMT1()
t = datetime(2014, 4, 26, 12, 1, tzinfo=tz)
u = tz.fromutc(t)
print (t)
print (u - u.utcoffset() )

#print(t.strftime("%:mk"))

#"%"+u"\u003A"+u"\u003A"+"z"