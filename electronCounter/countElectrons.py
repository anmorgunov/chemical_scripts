import constants
import parser

def count_electrons(formula):
    parsed = parser.parse(formula)
    electrons = 0
    for element, quantity in parsed.items():
        electrons += constants.PTABLE[element][0] * quantity
    return electrons


formulas = ['H2', 'He2', 'H2O', 'C2H6O', 'C2H5OH', 'C2H4O2', 'CH3COOH', 'CH3CH2COOH', 'CH3CH2COONa']
#             2     4      10     26       26         32       32          40               50s

# for formula in formulas:
#     print(count_electrons(formula))