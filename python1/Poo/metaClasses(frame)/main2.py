#  nesse caso aqui podemos ate mesmo setar se um atributo de uma classe pode ou nao sobrepor o atributo da classe pai...

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'valor A'


class B(A):

    attr_classe = 'valor B'


class C(B):

    attr_classe = 'valor C'


b = C()
print(b.attr_classe)
