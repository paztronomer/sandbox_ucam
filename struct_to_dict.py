""" Simple function to transform from structured array to dictionary
Francisco Paz-Chinchon
Institute of Astronomy, University of Cambridge
"""
import numpy as np

def dict_from_sarr(sarr, sel_field, change_byte=True):
    """Dictionary from structured array

    Parameters
    ----------
    sarr : ndarray
        structured array
    sel_field : list
        list of names for the fields to be used
    change_byte : boolean
        flag to change to little endian, in case the
        input FITS is big-endian
    Returns
    -------
    out_d : dict
        dictionary containing the pairs column name
        and column array
    """
    # Transform big-endian to little-endian
    if change_byte:
        sarr = sarr.byteswap().newbyteorder()
    out_d = dict()
    for col in sel_field:
        out_d.update({col: sarr[col]})
    return out_d
