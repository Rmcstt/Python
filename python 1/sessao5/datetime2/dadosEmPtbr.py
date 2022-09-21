from datetime import datetime
from locale import setlocale, LC_ALL

dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
setlocale(LC_ALL, 'pt_BR.utf-8')
