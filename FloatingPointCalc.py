# the other way to import a method without importing a
# full module, "D" is now an alias - allows to avoid conflict
# in naming
from decimal import Decimal as D

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum = ", sum)

print(".1 + .1 + .1 - .3 = ", 0.1 + 0.1 + 0.1 - 0.3)
