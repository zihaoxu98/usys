###### USYS: unit system in python ####

`usys` is a package to conveniently manage unit system in python.

To install, simply run `pip install -e .`

To use, for example
```
import usys
usys.use_unit_system("si") # use SI unit system

m = 2.0 * usys.kg
g = 9.8 * usys.m / usys.s**2

print((m * g).in_unit(usys.N)) # show m * g in Newton
```

Natural unit system, Planck unit system are also supported, for example
```
import usys
usys.use_unit_system("natural") # use natural unit system

m = 1.67-27 * usys.kg # mass of a proton

print(m.in_unit(usys.eV * 1e9)) # show mass of proton in GeV
```
