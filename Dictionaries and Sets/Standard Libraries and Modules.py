#Standard Libraries and Modules

#Put import at top of the file

import math
print(math.sqrt(81))

import math as m
print(m.sqrt(64))

from math import radians, cos, sin
angle_degrees = 40
angle_radians = radians(angle_degrees)
sine_value = sin(angle_radians)
cos_value = cos(angle_radians)
print(sine_value)
print(cos_value)

from math import *
print(sqrt(25))
print(pow(5, 2))
print(exp(1))
print(math.pi)

import datetime
birthday = datetime.date(2008, 10, 6)
print(birthday.day)
print(birthday.month)
print(birthday.year)
