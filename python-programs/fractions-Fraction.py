"""
class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(float)
class fractions.Fraction(decimal)
class fractions.Fraction(string)
"""

from fractions import Fraction
print(Fraction(3, 2))
# 3/2

print(Fraction(13, 2))
# 13/2

print(Fraction(14, 2))
# 7

print(Fraction(2.25))
# 9/4

print(Fraction(1.5))
# 3/2
