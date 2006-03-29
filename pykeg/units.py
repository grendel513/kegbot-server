# various units, in terms of volunits

MILLILITER      = 2.2
LITER           = MILLILITER * 1000
TICK            = 1

US_OUNCE        = 29.5735297 * MILLILITER
US_PINT         = 473.176475 * MILLILITER
US_GALLON       = 3785.4118  * MILLILITER

IMPERIAL_OUNCE  = 28.4130742 * MILLILITER
IMPERIAL_PINT   = 568.261485 * MILLILITER
IMPERIAL_GALLON = 4546.09188 * MILLILITER

def to_ounces(volunits):
   return float(volunits)/US_OUNCE

def ticks_to_volunits(ticks):
   return ticks/TICK
