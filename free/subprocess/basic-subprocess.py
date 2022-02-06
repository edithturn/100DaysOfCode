import subprocess

for i in range(0,10):
    nombreDir = "dir"+str(i)
    subprocess.call(['rm', '-r', nombreDir])
#subprocess.call(['ls', '-l'])
