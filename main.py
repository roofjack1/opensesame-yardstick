from makeKey import makeKey as m
from debruijn import de_bruijn as d
from rflib import *
from yardstick import init as init

r = RfCat()
init(r)

db = d(2,10)
key = m(db)

r.setMdmDRate(4000)
r.RFxmit(key)

