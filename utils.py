
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

    @classmethod
    def statuses(cls):
        return cls.status_on, cls.status_off

    @classmethod
    def models(cls):
        return cls.common_calc, cls.accountant_calc, cls.scientific_calc

    @classmethod
    def choices_for_common_and_scientific(cls):
        return cls.add, cls.minus, cls.multiple, cls.division

    @classmethod
    def choices_for_accountant(cls):
        return cls.add, cls.minus, cls.multiple, cls.division, cls.sinus, cls.cosinus
