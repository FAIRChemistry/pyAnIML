from typing import List, Optional, Union
from dataclasses import dataclass

from pyaniml.core.series import SeriesSet
from pyaniml.core.enums import DataTypes
from pyaniml.utility.utils import SchemaBase, attribute, elements


@dataclass
class Parameter(SchemaBase):
    """Container holding a parameter description"""

    value: Union[str, float, int, bool]
    name: str = attribute()
    dtype: DataTypes = attribute(name="parameterType")


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

    def __post_init__(self):
        # Validate content types
        if not all(
            isinstance(entry, (Parameter, SeriesSet, self.__class__))
            for entry in self.content
        ):
            # Guard clause to check type conistency
            raise TypeError(
                "Property must be either a 'Parameter', 'Category' or a 'SeriesSet'"
            )

    def add_content(self, content: Union[Parameter, SeriesSet]) -> None:
        """Adds a category to the the container. Must be of any low-level AnIML type.

        Args:
            content (Union[Parameter, SeriesSet]): Content to add to the container.
        """

        self.content.append(content)
