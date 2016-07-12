#!/usr/bin/env python
"""Zero out the imageHDUs in the calexps, and then gzip the files."""
from __future__ import absolute_import, division, print_function

from astropy.io import fits
import glob
import subprocess

files = glob.glob('cfht/calexp/06AL01/D3/2006-0*/r/calexp*.fits')
for f in files:
    data = fits.open(f)
    print('processing:', f)
    for i in range(len(data)):
        if isinstance(data[i], fits.ImageHDU):
            data[i].data[:] = 0
    data.writeto(f, clobber=True)
    # gzip the file
    subprocess.call(['gzip', f])
    # move it back to the original .fits filename to keep the butler happy.
    subprocess.call(['mv', f+'.gz', f])
