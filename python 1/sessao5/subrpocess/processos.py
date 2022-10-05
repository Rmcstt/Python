import subprocess

# subprocess serve para executar comandos do sistema operacinoal de dentro da aplicação!!!


# exemplo a seguir seria o ping do google...

ping = subprocess.run(['ping','-c','4','google.com'],capture_output=True, text=True) 



# print(ping.stderr)
print(ping.stdout)
# print(ping.returncode)
# print(ping.args)