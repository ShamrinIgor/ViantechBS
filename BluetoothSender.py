import subprocess
#kek
command = ["ls", "-l"]
p = subprocess.Popen(command, stdout=subprocess.PIPE)
text = p.communicate()
for line in text:
    print(text)
