class A:  # classe
  vc = 123  # atributo de classe

  def __init__(self):  
    self.vc = 321  # atributo de instancia


a1 = A()  # instancia 1
a2 = A()  # instancia 2

a1.vc = 321  

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print(a1.vc) # pela instancia
print(a2.vc) # pela instamcia
print(A.vc)  # chamar direto pela classe

