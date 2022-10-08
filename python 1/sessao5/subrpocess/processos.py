import subprocess

# subprocess serve para executar comandos do sistema operacinoal de dentro da aplicação!!!


# exemplo a seguir seria o ping do google...

ping = subprocess.run(['ping','-c','4','google.com'],capture_output=True, text=True)   # o capture_output=True serve para capturar a saida do comando e o text=True serve para transformar a saida em texto



# print(ping.stderr)
print(ping.stdout)
# print(ping.returncode)
# print(ping.args)