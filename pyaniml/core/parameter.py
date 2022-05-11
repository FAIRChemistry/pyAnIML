from typing import List, Optional, Union
from dataclasses import dataclass

from pyaniml.core.series import SeriesSet
from pyaniml.utility.utils import SchemaBase, attribute, elements


@dataclass
class Parameter(SchemaBase):
    """Container holding a parameter description"""

    value: Union[str, float, int, bool]
    name: str = attribute()
    parameter_type: str = attribute(name="parameterType")


@dataclass
class Category(SchemaBase):
    """Container holding a category description with multiple parameters"""

    name: str = attribute()
    content: List[object] = elements(
        choices=(
            {"name": "Parameter", "type": Parameter},
            {"name": "SeriesSet", "type": SeriesSet},
            {"name": "Category", "type": Optional["Category"]},
        ),
        default=list,
    )

    def add_content(self, content: Union[Parameter, SeriesSet]) -> None:
        """Adds a category to the the container. Must be of any low-level AnIML type.

        Args:
            category (Union[Parameter, SeriesSet]): A category of results.
        """
        self.content.append(content)
