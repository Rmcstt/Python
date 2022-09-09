"""
descricao rapida
lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

variavel1 = 'valor 1'
def soma(x,y):
    """
    soma x e y
    :param x: numero 1
    :type x: int or float
    :param y: numero 2
    :type y: int or float

    :return: soma de x e y
    :rtype: int or float
    """
    return x + y

def multiplica(x,y, z=None):
    """
    multiplica x e y
    :param x: numero 1
    :type x: int or float
    :param y: numero 2
    :type y: int or float
    :param z: numero 3
    :type z: int or float or None

    :return: multiplicacao de x e y
    :rtype: int or float
    """
    if z:
        return x*y*z
    return x*y

