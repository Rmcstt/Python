import subprocess

ping = subprocess.run(['ping','-c','4','google.com'],capture_output=True, text=True) 



# print(ping.stderr)
print(ping.stdout)
# print(ping.returncode)
# print(ping.args)