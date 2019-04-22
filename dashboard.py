#!/usr/local/bin/python3.7
import pendulum

from gen_table import *

dt = pendulum.now()

mon = dt.start_of('week')
tue = mon.add(days=1)
wed = mon.add(days=2)
thu = mon.add(days=3)
fri = mon.add(days=4)
sat = mon.add(days=5)
sun = mon.add(days=-1)

days = [sun, mon, tue, wed, thu, fri, sat]


gen_table = gen_table('content.json', days)

