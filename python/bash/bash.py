#!/usr/bin/python3
import os
import subprocess

# Method 1: subprocess.call(<bash_cmd | bash_script>)
#subprocess.call("./test.sh", shell=True)

# Method 2: os.system(<bash_cmd | bash_script>)
#os.system("./test.sh")

#print os.popen("cat /var/log/dmesg").read()
#subprocess.call("cat /var/log/dmesg", shell=True)

# Method 3: Popen
#cmd = "ls"
#proc=Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
#output=proc.stdout.read()
#proc.stdin.close()
#proc.kill()



# Method 4: write the output of the command in the out_file
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
out_file=open("out.txt","w+")
retcode=subprocess.call( ["ls", "-l"] , stdout=out_file, stderr=subprocess.STDOUT, shell=False)
out_file.close()
print(retcode)

# Method 5: write the output of the command in the buffer
cmd="cat /var/log/dmesg"
out_buf = subprocess.getoutput(cmd)
#print(out_buf)
