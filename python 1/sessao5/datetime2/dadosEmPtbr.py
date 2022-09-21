from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

# monthrange(ano, mes) retorna uma tupla com o dia da semana e o numero de dias do mes

# setlocale deffine a localidade

# LC_ALL define a localidade para todos os tipos de dados


setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao)
print(formatacao2)
print(f'mes = {mes_atual}, ultimo dia do mes = {mdays[mes_atual]}')
print(monthrange(2020,2))
dia_semana, ultimo_dia = monthrange(2020,2)
print(ultimo_dia)  # 29

ultimos_dias_de_meses_do_ano_atual =  [
  monthrange(datetime.now().year,mes)[1] for mes in range(1,13)
]
print(ultimos_dias_de_meses_do_ano_atual)