from dataclasses import dataclass
from typing import List, Union
from pyaniml.utility.utils import SchemaBase, element, elements
from pyaniml.core.parameter import Parameter
from pyaniml.core.parameter import Category


@dataclass
class Device(SchemaBase):
    """Container describing a physical device"""

    name: str = element("Name")
    firmware_version: str = element("FirmwareVersion")
    serial_number: str = element("SerialNumber")


@dataclass
class Author(SchemaBase):
    """Container describing an author"""

    name: str = element("Name")


@dataclass
class Method(SchemaBase):
    """Container for method-related informations"""

    methods: List[object] = elements(
        choices=(
            {"name": "Device", "type": Device},
            {"name": "Author", "type": Author},
            {"name": "Parameter", "type": Parameter},
            {"name": "Category", "type": Category}
        ),
        default=list
    )

    def add_method(self, method: Union[Device, Author, Parameter, Category]):
        """Adds a method-related property to the Method section of an experiment step

        Args:
            method (Union[Device, Author, Parameter, Category]): Characteristics of a method.
        """
        self.methods.append(method)
