import numpy as np
from fractions import Fraction
import math

print("1)", Fraction(2, 5) + Fraction(1, 3), "=",
      float(Fraction(2, 5) + Fraction(1, 3)))
print("2)", Fraction(0.375).limit_denominator(), "= {:.1%}".format(0.375))
print("3)", 30000 * (1 - 0.25), "원")
print("4)", 33000 / 1.1, "원")
print("5) {:+.0%}".format((100 - 80) / 80))
print("6)", math.log2(32))

total, ratios = 500, np.array([6, 3, 1])
print("7)", total * ratios / np.sum(ratios))
