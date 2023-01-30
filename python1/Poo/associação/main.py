"""
associação - usa
agregação - tem
composição - é dono
herança - é 
"""


from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('renato')  # instanciando um escritor
caneta = Caneta('mont blanc')  # instanciando uma caneta
maquina = MaquinaDeEscrever()  # instaanciando uma maquina de escrever

escritor.ferramenta = maquina  # associando a ferramenta ao escritor
escritor.ferramenta.escrever()  # usando a função da ferramenta