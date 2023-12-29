from currency_converter import CurrencyConverter
c = CurrencyConverter()
b = c.convert(100, 'GBP', 'USD')
from log import logger

def convert_dollars_to_pounds(dollars):
    return c.convert(dollars, 'USD', 'GBP')

def convert_pounds_to_dollars(pounds):
    return c.convert(pounds, 'GBP', 'USD')

def convert_symbol_to_symbol(amount, symbol_from, symbol_to):
    try: 
        return c.convert(amount, symbol_from, symbol_to)
    except ValueError as e:
        logger.debug(e, stack_info=True)
        return 'Invalid symbol'

print(convert_symbol_to_symbol(100, 'GBP', 'USDD'))