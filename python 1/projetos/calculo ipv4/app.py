

from classes.calcipv4 import CalcIpv4
import os

if os.name == 'posix':
    cls = "clear"
else:
    cls = "cls"

""" calculo ipv4, com bbase em um ip  e uma mascara ou prefixo"""

os.system(cls)

ip = input('digite o ip: ')

os.system(cls)



maskOrPrefix = input(' digite a mascara ou o prefixo: ')

os.system(cls)

if len(maskOrPrefix) == 2:
  calc_ipv4 = CalcIpv4(ip, prefixo=int(maskOrPrefix))
else:
  calc_ipv4 = CalcIpv4(ip, mascara=maskOrPrefix)

