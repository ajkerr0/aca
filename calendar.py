# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:24:18 2016

@author: Alex
"""

import calendar

month = 5
year = 2016

c = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(year, 1)

holidays = [(0, 18), (8, 5)]

print c[month-1]