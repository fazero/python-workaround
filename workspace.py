#!/usr/bin/python
# -*- coding: utf-8 -*-
for x in range(1, 11):
#    print '%2d %3d %4d'.format(x, x*x, x*x*x)
    print ('Some {:2} {:3} {:4}'.format(x, x * x, x * x * x))

import math
print 'Значение PI приблизительно равно %5.3f' % math.pi
m = '{:10.2f}'.format(math.pi)
print m

print vars()
