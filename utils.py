
class CalculatorUtil:
    status_on = 'on'
    status_off = 'off'

    common_calc = 'common'
    accountant_calc = 'acc'
    scientific_calc = 'sci'

    add = "add"
    minus = "minus"
    multiple = "multiple"
    division = "division"
    sinus = "sinus"
    cosinus = "cosinus"
    sqr = "sqr"
    sqrt = "sqrt"

    @classmethod
    def statuses(cls):
        return cls.status_on, cls.status_off

    @classmethod
    def models(cls):
        return cls.common_calc, cls.accountant_calc, cls.scientific_calc

    @classmethod
    def choices_for_common(cls):
        return cls.add, cls.minus, cls.multiple, cls.division, cls.sqr, cls.sqrt

    @classmethod
    def choices_for_scientific(cls):
        return cls.add, cls.minus, cls.multiple, cls.division, cls.sqr, cls.sqrt, cls.sinus, cls.cosinus

    @classmethod
    def choices_for_accountant(cls):
        return cls.add, cls.minus, cls.multiple, cls.division
