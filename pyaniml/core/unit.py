from dataclasses import dataclass
from typing import List

from pyaniml.core.enums import si_unit_name_list
from pyaniml.utility.utils import SchemaBase, element, attribute


@dataclass
class SIUnit(SchemaBase):
    """Container for a SI base unit."""

    si_name: str
    factor: float = attribute(name="factor", default_value=1.0)
    exponent: float = attribute(name="exponent", default_value=1.0)
    offset: float = attribute(name="offset", default_value=0.0)

    # Validators
    @staticmethod
    def verify_si_name(si_name):
        if si_name not in si_unit_name_list:
            raise TypeError(
                f"Invalid SI base unit. Please choose from {si_unit_name_list}."
            )


@dataclass
class Unit(SchemaBase):
    """Container for unit information for a series."""

    si_unit: List[SIUnit] = element(name="SIUnit")
    label: str = attribute(name="label")
    quantity: str = attribute(name="quantity")

    def add_si_unit(self, si_unit: SIUnit) -> None:
        """
        Adds a SI base unit to the container. Must be of SIUnit type.

        Args:
            si_unit (SIUnit): The SI base unit.
        """
        self.si_unit.append(si_unit)
