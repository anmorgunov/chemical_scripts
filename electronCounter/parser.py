def parse(formula):
    parsed = {}
    eltBuilder, quant = '', 0
    for i, char in enumerate(formula):
        try: 
            quant = int(char)
        except ValueError:
            eltBuilder += char
        # print(f"iteration {i}, char {char}, quant {quant}, builder {eltBuilder}")
        if not formula[i+1:i+2].islower() and not formula[i+1:i+2].isdecimal():
            if eltBuilder not in parsed:
                parsed[eltBuilder] = 0
            increment = 1
            if quant != 0:
                increment = quant
            parsed[eltBuilder] += increment
            quant = 0
            eltBuilder = ''
    if eltBuilder:
        if eltBuilder not in parsed:
            parsed[eltBuilder] = 0
        parsed[eltBuilder] += 1
    return parsed

# # TESTS
formulas = ['H2', 'He2', 'H2O', 'C2H6O', 'C2H5OH', 'C2H4O2', 'CH3COOH', 'CH3CH2COOH', 'CH3CH2COONa']
# for formula in formulas:
#     print(parse(formula))

