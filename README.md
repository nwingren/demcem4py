# demcem4py

demcem4py is a Python wrapper of the C++ software [DEMCEM](https://github.com/thanospol/DEMCEM) developed by Athanasios Polimeridis for computing singular integrals in EM surface integrals. This package provides a Python interface to the C++ functions of DEMCEM with native Python data types and NumPy arrays as input variables. The functions have the same inputs as the original DEMCEM functions, including the use of in-place operations to store the results.

The Python bindings of C++ code is done using [pybind11](https://pybind11.readthedocs.io) and was originally developed as a part of the [FE2MS](https://github.com/nwingren/fe2ms) finite element-boundary integral code. As the singular integral computations offered by DEMCEM might be interesting to others working with computational electromagnetics in Python, this component was separated as a stand-alone package.



## Installation

### Manual installation

The demcem4py package can be installed by cloning this git repository and installing using pip as

```bash
git clone https://github.com/nwingren/demcem4py.git
pip install demcem4py
```

## Included Functions

The functions are described in the [DEMCEM manual](https://github.com/thanospol/DEMCEM/blob/4b8e2c915eb33fda229b714bf04a49666795835c/Manual/ReadMe_DEMCEM.pdf), but they are listed here together with the Python input types for this package for completeness.

### Weakly Singular Integrals

#### Self term
```python
demcem4py.ws_st_rwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], ko: complex, Np_1D: int, result: numpy.ndarray[numpy.complex128])
```

#### Edge adjacent
```python
demcem4py.ws_ea_rwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], r4: numpy.ndarray[numpy.float64], ko: complex, N_theta: int, N_psi: int, result: numpy.ndarray[numpy.complex128])
```

#### Vertex adjacent
```python
ws_va_rwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], r4: numpy.ndarray[numpy.float64], r5: numpy.ndarray[numpy.float64], ko: complex, N_theta_p: int, N_theta_q: int, N_psi: int, result: numpy.ndarray[numpy.complex128])
```

### Strongly Singular Integrals

#### Edge adjacent
```python
demcem4py.ss_ea_rwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], r4: numpy.ndarray[numpy.float64], ko: complex, N_theta: int, N_psi: int, result: numpy.ndarray[numpy.complex128])

demcem4py.ss_ea_nxrwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], r4: numpy.ndarray[numpy.float64], ko: complex, N_theta: int, N_psi: int, result: numpy.ndarray[numpy.complex128])
```

#### Vertex adjacent
```python
demcem4py.ss_va_rwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], r4: numpy.ndarray[numpy.float64], r5: numpy.ndarray[numpy.float64], ko: complex, N_theta_p: int, N_theta_q: int, N_psi: int, result: numpy.ndarray[numpy.complex128])

demcem4py.ss_va_nxrwg(r1: numpy.ndarray[numpy.float64], r2: numpy.ndarray[numpy.float64], r3: numpy.ndarray[numpy.float64], r4: numpy.ndarray[numpy.float64], r5: numpy.ndarray[numpy.float64], ko: complex, N_theta_p: int, N_theta_q: int, N_psi: int, result: numpy.ndarray[numpy.complex128])
```

## License

The license described below is specifically for the Python bindings. DEMCEM itself is licensed under the GNU Lesser General Public License (LGPL).

Copyright (C) 2024 Niklas Wingren

demcem4py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Acknowledgements
This work was supported in part by the Swedish Armed Forces, in part by the Swedish Defence Materiel Administration, in part by the National Aeronautics Research Program and in part by the Swedish Governmental Agency for Innovation Systems.