from math import tan, cos, sqrt, pi, sin

class LatLng:
	def __init__(self, latitude, longitude):
		# save as radian
		self.latitude = latitude * pi / 180
		self.longitude = longitude * pi / 180

westOrigin = LatLng(38.0, 125.0)
midOrigin = LatLng(38.0, 127.0)
eastOrigin = LatLng(38.0, 129.0)
eastSeaOrigin = LatLng(38.0, 131.0)
target = LatLng(37.3738, 127.2357)

#장반경
a1 = 6378137.000 #GRS80
a2 = 6377397.155 #Bessel

#편평률
f1 = 1/298.2572221010 #GRS80
f2 = 1/299.1528128000 #Bessel

#단반경
b1 = a1 * (1 - f1) #GRS80
b2 = a2 * (1 - f2) #Bessel

#원점 가산값
dY1 = 200000 #GRS80
dX1 = 600000 #GRS80
dX2 = 200000 #Bessel
dY2 = 500000 #Bessel

#GRS80 이용
a = a1
b = b1
f = f1
dY = dY1
dX = dX1

#중부원점 사용
origin = midOrigin

#원점축척계수
k = 1.0000

#제1이심률
e1sq = (pow(a,2)-pow(b,2)) / pow(a,2)
#제2이심률
e2sq = (pow(a,2)-pow(b,2)) / pow(b,2)

# 자오 선호장 계산
def getM(target):
	return a * (
		(1-e1sq/4-3*pow(e1sq,2)/64-5*pow(e1sq,3)/256)*target.latitude -
		(3*e1sq/8 + 3*pow(e1sq,2)/32 + 45*pow(e1sq,3)/1024)*sin(2*target.latitude) +
		(15*pow(e1sq,2)/256 + 45*pow(e1sq,3)/1024)*sin(4*target.latitude) -
		35*pow(e1sq,3)/3072*sin(6*target.latitude)
	)

T = pow(tan(target.latitude), 2)
C = (e1sq/(1-e1sq)) * pow(cos(target.latitude), 2)
A = (target.longitude - origin.longitude) * cos(target.latitude)
N = a / sqrt(1 - e1sq * pow(sin(target.latitude), 2))
M = getM(target)
M0 = getM(origin)

Y = dY + k*N*(A + pow(A,3)/6*(1-T+C) + pow(A,5)/120*(5-18*T+pow(T,2)+72*C-58*e2sq))
X = dX + k*(M - M0 + N*tan(target.latitude)*(pow(A,2)/2 + pow(A,4)/24*(5-T+9*C+4*pow(C,2)) + pow(A,6)/720*(61-58*T+pow(T,2)+600*C-330*e2sq)))

print("Y " + str(Y))
print("X " + str(X))
