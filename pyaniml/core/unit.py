from dataclasses import dataclass
from typing import List

from pyaniml.core.enums import SIUnits
from pyaniml.utility.utils import SchemaBase, element, attribute


@dataclass
class SIUnit(SchemaBase):
    """Container for a SI base unit."""

    si_name: SIUnits
    factor: float = attribute(name="factor", default_value=1)
    exponent: float = attribute(name="exponent", default_value=1)
    offset: float = attribute(name="offset", default_value=0)


@dataclass
class Unit(SchemaBase):
    """Container for unit information for a series."""

    label: str = attribute(name="label")
    quantity: str = attribute(name="quantity")
    si_unit: List[SIUnit] = element(name="SIUnit", default=list)

    def add_si_unit(self, si_unit: SIUnit) -> None:
        """
        Adds a SI base unit to the container. Must be of SIUnit type.

        Args:
            si_unit (SIUnit): The SI base unit.
        """
        self.si_unit.append(si_unit)
