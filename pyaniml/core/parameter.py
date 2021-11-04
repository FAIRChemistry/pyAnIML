from typing import List
from dataclasses import dataclass
from pyaniml.utility.utils import SchemaBase, element, attribute, elements
from pyaniml.core.enums import type_inference


@dataclass
class Parameter(SchemaBase):
    """Container holding a parameter description"""

    name: str = attribute()
    parameter_type: str = attribute(name="parameterType")
    value: List[object] = elements(choices=type_inference)


@ dataclass
class Category(SchemaBase):
    """Container holding a category description wit multiple parameters"""

    name: str = attribute()
    parameters: List[Parameter] = element(default=list, name="Parameter")
