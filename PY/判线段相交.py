class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def __add__(self, rhs):
        return Point(self.x+rhs.x, self.y+rhs.y)
    def __sub__(self, rhs):
        return Point(self.x-rhs.x, self.y-rhs.y)
    def __mul__(self, rhs):
        return self.x*rhs.x + self.y*rhs.y
    def __mod__(self, rhs):
        return self.x*rhs.y - self.y*rhs.x
    
Vector = Point

def sgn(x):
    if abs(x) < 1e-8:
        return 0
    elif x < 0:
        return -1
    else:
        return 1
def Intersection(a1, a2, b1, b2):
    c1, c2 = (a2-a1)%(b1-a1), (a2-a1)%(b2-a1)
    c3, c4 = (b2-b1)%(a1-b1), (b2-b1)%(a2-b1)
    return sgn(c1)*sgn(c2) < 0 and sgn(c3)*sgn(c4) < 0

def OnSeg(p, a1, a2):
    return sgn((a1-p)%(a2-p)) == 0 and sgn((a1-p)*(a2-p)) <= 0

T = int(input())
for i in range(T):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
    a1, a2, b1, b2 = Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4)
    res = False
    res |= Intersection(a1, a2, b1, b2)
    res |= OnSeg(a1, b1, b2)
    res |= OnSeg(a2, b1, b2)
    res |= OnSeg(b1, a1, a2)
    res |= OnSeg(b2, a1, a2)
    if res:
        print("Yes")
    else:
        print("No")
              
