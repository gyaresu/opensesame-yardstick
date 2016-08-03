from makeKey import makeKey as m
from debruijn import de_bruijn as d
from rflib import *
from yardstick import init as init

r = RfCat()
init(r)

db = d(3,8)
key = m(db, 3)

#r.RFxmit(key)


