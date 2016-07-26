from makeKey import makeKey as m
from debruijn import de_bruijn as d
from rflib import *
from yardstick import init as init

r = RfCat()
init(r)

db = d(2,9)
key = m(db)

r.RFxmit(key)


