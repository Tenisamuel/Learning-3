#Copy the program shown in example 1 above, save and run it. improve it so that the last display before walk
#says "1 second" and not "1 seconds"

import time

print("Wait")
for seconds in range(10,0,-1):
    print(seconds, "second")
    time.sleep(1)
print("Walk")