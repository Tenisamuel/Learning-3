#The depth of the water at various points in a harbour is measured by a device, accurate to two decimal
#places.A mapmaker wants to print each recorded depth rounded down to the nearest integer. For example, a
#recorded depth rounded down to the nearest integer.For example, a recorded depth of 40.63m will be printed 
#as 40m.

#write statements to calculate and print depths recorded by the device as 38.0m and 53.9 m, to the nearest integers
#below the recorded values.

import math
recorded_value1 = 38.0
recorded_value2 = 53.9
print(math.floor(recorded_value1))
print(math.floor(recorded_value2))
