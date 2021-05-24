import os
import time
import subprocess





def main():
    print('main function')
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
   
    print(result.stdout)
  
# Using for loop


while True :
    main()
    time.sleep(10)
