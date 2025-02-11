from mapattrs import trace, dflr, inheritance, mapattrs

from testmixin0 import Sub

I = Sub()                                                       # Sub inherits from Super and ListInstance roots

trace(dflr(I.__class__))                                        # 2.X search order: implied object before lister!

trace(inheritance(I))                                           # 3.X (+ 2.X new-style) search order: lister first

trace(mapattrs(I))

trace(mapattrs(I, bysource = True))

trace(mapattrs(I, withobject = True))

amap = mapattrs(I, withobject = True, bysource = True)

trace(amap)
