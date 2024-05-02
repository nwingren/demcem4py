"""
Test script for DEMCEM bindings to be run in its current directory.

Copyright (C) 2024 Niklas Wingren

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
import demcem4py

def test_ss_ea_nxrwg():

    r1 = np.array([0.0, 0.0, 0.0])
    r2 = np.array([0.0, 0.1, 0.0])
    r3 = np.array([0.0, 0.0, 0.1])
    r4 = np.array([0.1, 0.0, 0.0])
    k0 = 2 * np.pi
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ss_ea_nxrwg(r1, r2, r3, r4, k0, 5, 5, result)

    # refvals = np.loadtxt('demcem_ref_ss_ea_nxrwg.txt')

    refvals = np.array([
        [-0.00147157, 1.49234e-07],
        [0.00431984, -4.473e-05],
        [-0.000639886, 3.1679e-05],
        [0.00365444, -4.47881e-05],
        [-0.00147157, 1.49234e-07],
        [-0.00365244, 4.48754e-05],
        [-0.00224266, 2.2462e-05],
        [0.00135456, -1.20167e-08],
        [0.0062409, -2.26163e-05]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)


def test_ss_ea_rwg():

    r1 = np.array([0.0, 0.0, 0.0])
    r2 = np.array([0.0, 0.1, 0.0])
    r3 = np.array([0.0, 0.0, 0.1])
    r4 = np.array([0.1, 0.0, 0.0])
    k0 = 2 * np.pi
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ss_ea_rwg(r1, r2, r3, r4, k0, 5, 5, result)

    # refvals = np.loadtxt('demcem_ref_ss_ea_rwg.txt')

    refvals = np.array([
        [-0.00170003, 3.16168e-05],
        [0, 0],
        [0.00452612, -3.17845e-05],
        [0, 0],
        [0.00170003, -3.16168e-05],
        [-0.00349291, 2.25417e-05],
        [0.00349289, -2.25371e-05],
        [-0.00452616, 3.17781e-05],
        [4.75819e-07, -5.67386e-12]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)


def test_ss_va_nxrwg():

    r1 = np.array([0.1, 0.1, 0.1])
    r2 = np.array([0.2, 0.1, 0.1])
    r3 = np.array([0.1, 0.2, 0.1])
    r4 = np.array([0.0, 0.1, 0.2])
    r5 = np.array([0.0, 0.2, 0.2])
    k0 = 2 * np.pi
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ss_va_nxrwg(r1, r2, r3, r4, r5, k0, 5, 5, 5, result)

    # refvals = np.loadtxt('demcem_ref_ss_va_nxrwg.txt')

    refvals = np.array([
        [0.000510175, -5.96019e-05],
        [-0.00043004, 8.68874e-07],
        [-0.00127912, 8.62414e-05],
        [3.80592e-05, -3.3162e-07],
        [0.000451142, -3.6913e-05],
        [-0.000287834, 3.03408e-05],
        [-0.000103248, 6.21047e-07],
        [-0.000452986, 7.2761e-05],
        [0.000928168, -6.02386e-05]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)


def test_ss_va_rwg():

    r1 = np.array([0.1, 0.1, 0.1])
    r2 = np.array([0.2, 0.1, 0.1])
    r3 = np.array([0.1, 0.2, 0.1])
    r4 = np.array([0.0, 0.1, 0.2])
    r5 = np.array([0.0, 0.2, 0.2])
    k0 = 2 * np.pi
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ss_va_rwg(r1, r2, r3, r4, r5, k0, 5, 5, 5, result)

    # refvals = np.loadtxt('demcem_ref_ss_va_rwg.txt')

    refvals = np.array([
        [0, 0],
        [-0.000396981, 5.11351e-05],
        [0.000321244, -4.18749e-05],
        [0.000463996, -4.2766e-05],
        [-0.000131806, -3.59886e-05],
        [-0.00160549, 9.16104e-05],
        [-0.000322689, 4.18133e-05],
        [0.000474518, -1.36943e-06],
        [0.000843793, -6.02511e-05]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)


def test_ws_ea_rwg():

    r1 = np.array([0.0, 0.0, 0.0])
    r2 = np.array([0.5, 0.0, 0.0])
    r3 = np.array([0.0, 0.0, 0.5])
    r4 = np.array([0.0, 0.5, 0.0])
    k0 = 1.0
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ws_ea_rwg(r1, r2, r3, r4, k0, 5, 5, result)

    # refvals = np.loadtxt('demcem_ref_ws_ea_rwg.txt')

    refvals = np.array([
        [-0.351861, -1.35868],
        [-0.487363, -1.87833],
        [-0.344618, -1.32818],
        [-0.238589, -0.923054],
        [-0.351862, -1.35868],
        [-0.248804, -0.960731],
        [-0.248804, -0.960731],
        [-0.344618, -1.32818],
        [-0.243682, -0.939166]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)


def test_ws_st_rwg():
    
    r1 = np.array([0.0, 0.0, 0.5])
    r2 = np.array([0.0, 0.0, 0.0])
    r3 = np.array([0.5, 0.0, 0.0])
    k0 = 2 * np.pi
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ws_st_rwg(r1, r2, r3, k0, 5, result)

    # refvals = np.loadtxt('demcem_ref_ws_st_rwg.txt')

    refvals = np.array([
        [0.0774216, 0.117725],
        [-0.303475, -0.291591],
        [-0.357179, -0.362711],
        [-0.303475, -0.291591],
        [-0.143998, -0.0993206],
        [-0.303475, -0.291591],
        [-0.357179, -0.362711],
        [-0.303475, -0.291591],
        [0.0774216, 0.117725]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)


def test_ws_va_rwg():

    r1 = np.array([1.0, 1.0, 1.0])
    r2 = np.array([2.0, 1.0, 1.0])
    r3 = np.array([1.0, 2.0, 1.0])
    r4 = np.array([0.0, 1.0, 1.0])
    r5 = np.array([0.0, 2.0, 1.0])
    k0 = 2 * np.pi
    result = np.zeros(9, dtype=np.complex128)

    demcem4py.ws_va_rwg(r1, r2, r3, r4, r5, k0, 5, 5, 5, result)

    # refvals = np.loadtxt('demcem_ref_ws_va_rwg.txt')

    refvals = np.array([
        [-0.0478167, 0.0359795],
        [-0.0520999, 0.102836],
        [0.0840446, -0.0850105],
        [-0.0207496, 0.204112],
        [0.152997, 0.0943941],
        [0.193664, -0.0447827],
        [-0.0261748, -0.0535851],
        [-0.0260403, -0.0390443],
        [-0.0541084, 0.024204]
    ])

    refvals = refvals[:,0] + 1j * refvals[:,1]

    assert np.allclose(result, refvals)
