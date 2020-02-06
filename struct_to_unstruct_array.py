"""
Simple script to go from structured to unstructured array.
Native implementation with recfunctions and alternative
way with list comprehension.

Francisco Paz-Chinchon
Institute of Astronomy, University of Cambridge
"""

import os
import numpy as np
import pandas as pd
import xarray as xr
import fitsio
import timeit
import functools

from numpy.lib.recfunctions import structured_to_unstructured

def get_sel(sarr, xcol_nm, output_array=False):
    """Splits an structured array in its columns

    Method to split a structured array into a list of arrays,
    each one being a column/field of the original. It can return
    either a list o an array.

    Parameters
    ----------
    sarr : ndarray
        structured array
    xcol_snm : list
        list of fileds to be returned
    output_array : boolena
        flag to wether return an array or a list

    Returns
    -------
    getcol : list or nadarray
        depending on the flag
    """
    getcol = [sarr[c] for c in xcol_nm]
    if output_array:
        return np.array(getcol)
    else:
        return getcol

if __name__ == "__main__":
    # Define a structured array for testing
    # Useful for FITS bintable manipulation

    # Create datatype, most flexible way
    # Available fields: name, format, offset, itemsize
    # https://docs.scipy.org/doc/numpy-1.15.0/user/basics.rec.html
    dt = np.dtype(
        {"names": ["field01", "field02", "field03", "field04"],
         "formats": ["f4", "f4", "f4", "f4"],
        }
    )

    # Create list of arrays, or list of tuple
    data = [np.random.normal(0, 0.3, 1000000),
            np.exp(np.random.normal(0, 0.3, 1000000)),
            np.random.normal(-10, .1, 1000000),
            np.sin(np.random.normal(-10, .1, 1000000)),]

    # Create structured array
    st_arr = np.array(data, dtype=dt)

    # Checking execution time for both methods
    t1 = timeit.Timer(
        functools.partial(get_sel, st_arr, st_arr.dtype.names),
        setup="from __main__ import get_sel"
    )
    print("Handcrafted method, time: {0:.2E} s".format(t1.timeit(number=1000)))

    t2 = timeit.Timer(
        functools.partial(structured_to_unstructured, st_arr),
        # setup="from __main__ import get_sel"
    )
    print("Functools method, time: {0:.2E} s".format(t2.timeit(number=100)))

    #timeit.timeit(
    #    structured_to_unstructured(st_arr), number=1000
    #)

    # %timeit -n 1000 get_sel(fits_ref[1].read(), fits_ref[1].read().dtype.names)
    # %timeit -n 10 structured_to_unstructured(fits_ref[1].read())
