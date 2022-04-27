from typing import List, Union
from dataclasses import dataclass
from pyaniml.core.series import SeriesSet

# from pyaniml.core.unit import Unit
from pyaniml.utility.utils import SchemaBase, attribute, element, elements
from pyaniml.core.enums import type_inference


@dataclass
class Parameter(SchemaBase):
    """Container holding a parameter description"""

    name: str = attribute()
    parameter_type: str = attribute(name="parameterType")
    # unit: Unit = element(name="Unit")
    value: List[object] = elements(choices=type_inference)


@dataclass
class Category(SchemaBase):
    """Container holding a category description with multiple parameters"""

    name: str = attribute()
    content: List[object] = elements(
        choices=(
            {"name": "Parameter", "type": Parameter},
            {"name": "SeriesSet", "type": SeriesSet},
        ),
        default=list,
    )

    def add_content(self, content: Union[Parameter, SeriesSet]) -> None:
        """Adds a category to the the container. Must be of any low-level AnIML type.

        Args:
            category (Union[Parameter, SeriesSet]): A category of results.
        """
        self.content.append(content)
