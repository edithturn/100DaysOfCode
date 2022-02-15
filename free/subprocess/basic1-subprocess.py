import subprocess

# Shell on Linux, Mac, Windows, as a list
subprocess.run('ls -al', shell=True)
# Save the output in a variable
# Print the command
p1 = subprocess.run(['ls', '-al'])
# Print the return code
print(p1.returncode)
# Print arguments of the comand
print(p1.args) 

# Return None, because we are printing 
print(p1.stdout)
# Capture the output
p2 = subprocess.run(['ls'], capture_output=True, text=True)
print(p2.stdout)

# 
with open('output.txt', 'w') as f:
    p3 = subprocess.run(['ls'], stdout=f, text=True)

p4 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)

if p4.returncode != 0:
    print("Error Case")
print(p4.stderr)

# Running cat
p5 = subprocess.run(['cat', 's.txt'], capture_output=True, text=True)
#print(p5.stdout)

# Grep
p6 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p5.stdout)
print(p6.stdout)