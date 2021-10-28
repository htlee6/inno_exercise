def cal_kaya(pop, gdp, enInt, carbInt):
    """
    To calculate Kaya Equation.
    """

    assert pop >= 0
    assert gdp >= 0
    assert enInt >= 0
    assert carbInt >= 0
    
    return pop * gdp * enInt * carbInt
    