def cal_kaya(pop, gdp, enInt, carbInt, output='CO2'):
    """
    To calculate Kaya Equation.
    """

    assert pop >= 0
    assert gdp >= 0
    assert enInt >= 0
    assert carbInt >= 0

    if output == 'CO2':
        return pop * gdp * enInt * carbInt
    if output == 'C':
        return pop * gdp * enInt * carbInt * 12 / 44
    