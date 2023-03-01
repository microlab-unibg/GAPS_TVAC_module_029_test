import os as os
import numpy as np
import pandas as pd

from erf_function import *
from read_pedestals import get_pedestal_auto
from calculate_xray_gain import get_linear_gain_realfdt


def linear_model(x, m, q):
    return m * x + q


def get_parasitic_injection(pedestal_filepath, fdt_filepath, ch, pt):
    # Read channel pedestal given peaking time
    pedestal_ch = get_pedestal_auto(pedestal_filepath, ch)

    # Calculate transfer function linear gain and estimate pedestal
    (fdt_gain, fdt_pedestal) = get_linear_gain_realfdt(fdt_filepath, ch, pt, 200)

    # Determine parasitic injection
    ch_par_inj = abs(pedestal_ch - fdt_pedestal)  # ADU
    ch_par_inj = ch_par_inj * (1 / fdt_gain)  # keV

    return ch_par_inj


def get_parasitic_injection_ADU(pedestal_filepath, fdt_filepath, ch, pt):
    # Read channel pedestal given peaking time
    pedestal_ch = get_pedestal_auto(pedestal_filepath, ch)

    # Calculate transfer function linear gain and estimate pedestal
    (fdt_gain, fdt_pedestal) = get_linear_gain_realfdt(fdt_filepath, ch, pt, 200)

    # Determine parasitic injection
    ch_par_inj = abs(pedestal_ch - fdt_pedestal)  # ADU

    return ch_par_inj


def get_pedestals(pedestal_filepath, fdt_filepath, ch, pt):
    # Read channel pedestal given peaking time
    pedestal_ch = get_pedestal_auto(pedestal_filepath, ch)

    # Calculate transfer function linear gain and estimate pedestal
    (fdt_gain, fdt_pedestal) = get_linear_gain_realfdt(fdt_filepath, ch, pt, 200)

    return fdt_pedestal, pedestal_ch
