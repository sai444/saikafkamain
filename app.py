import os
import time
import sys
import subprocess





def main():

    command = subprocess.run(['python', 'test.py'], capture_output=True)

  
    #y =sys.stderr.buffer.write(command.stderr)
    print(command.stdout)
    #print(y)
  
        

    cmd = "git --version"

    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)
    sys.exit(command.returncode)




while True :
    main()
    time.sleep(10)
