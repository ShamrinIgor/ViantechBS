# import subprocess
# #kek
# command = ["ls", "-l"]
# p = subprocess.Popen(command, stdout=subprocess.PIPE)
# text = p.communicate()
# for line in text:
#     print(text)
import  subprocess
output = subprocess.check_output("ls -a", shell = True )
output = str(output)
output = output.split('\\n')
for i in range(len(output)):
    print (output[i])
