from dataclasses import dataclass
from typing import List, Union
from pyaniml.utility.utils import SchemaBase, attribute, element, elements
from pyaniml.core.parameter import Category, Parameter
from pyaniml.core.enums import user_types


@dataclass
class Software(SchemaBase):
    """Container of software used in this ExerimentStep"""

    manufacturer: str = element("Manufacturer")
    name: str = element("Name")
    version: str = element("Version")
    operating_system: str = element("OperatingSystem")


@dataclass
class Device(SchemaBase):
    """Container describing a physical device"""

    device_id: str = element("DeviceIdentifier")
    manufacturer: str = element("Manufacturer")
    name: str = element("Name")
    firmware_version: str = element("FirmwareVersion")
    serial_number: str = element("SerialNumber")


@dataclass
class Author(SchemaBase):
    """Container describing an author"""

    user_type: str = attribute("userType")
    name: str = element("Name")
    affiliation: str = element("Affiliation")
    role: str = element("Role")
    email: str = element("Email")
    phone: str = element("Phone")
    location: str = element("Location")

    @staticmethod
    def verify_user_type(user_type):
        if user_type not in user_types:
            raise TypeError(
                f"Unknown dependency argument '{user_type}'. Please choose from {user_types}"
            )


@dataclass
class Method(SchemaBase):
    """Container for method-related informations"""

    methods: List[object] = elements(
        choices=(
            {"name": "Device", "type": Software},
            {"name": "Device", "type": Device},
            {"name": "Author", "type": Author},
            {"name": "Parameter", "type": Parameter},
            {"name": "Category", "type": Category},
        ),
        default=list,
    )

    def add_method(
        self, method: Union[Software, Device, Author, Parameter, Category]
    ):
        """Adds a method-related property to the Method section of an experiment step

        Args:
            method (Union[Device, Author, Parameter, Category]): Characteristics of a method.
        """
        self.methods.append(method)
