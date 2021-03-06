#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
Qgridinfo should contain python codes to give varaibles b1, b2, b3 and n1, n2, n3

b1, b2, b3 defines the reciprocal unit cell in which the grid is defined
n1, n2, n3 are number of points along directions of b1, b2, b3 respectively
'''

def read( path ):
    lines = open(path).readlines()
    for line in lines:
        exec line in locals()
        continue
    return (b1,b2,b3), (n1,n2,n3)


def tolines(bs, ns):
    '''convert Qgridinfo in form of a 2-tuple: (b vectors, number of grid points)
    to a list of strings to be saved as a Qgridinfo file.
    '''
    s = []
    s += ['b%s=%s' % (i+1, list(bs[i])) for i in range(3)]
    s += ['n%s=%s' % (i+1, ns[i]) for i in range(3)]
    s += ['']
    return s


# version
__id__ = "$Id$"

# End of file 
