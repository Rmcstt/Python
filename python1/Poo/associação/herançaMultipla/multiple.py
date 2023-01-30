class A:
  def falar(self):
    print('falando... estou em A')

class B(A):
  def falar(self):
    print('falando... estou em B')

class C(A):
  def falar(self):
    print('falando... estou em C')

class D(B, C):
  pass

d = D()
d.falar()