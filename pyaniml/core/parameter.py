from typing import List, Union
from dataclasses import dataclass
from pyaniml.core.series import Series, SeriesSet
from pyaniml.utility.utils import SchemaBase, attribute, elements
from pyaniml.core.enums import type_inference


@dataclass
class Parameter(SchemaBase):
    """Container holding a parameter description"""

    name: str = attribute()
    parameter_type: str = attribute(name="parameterType")
    value: List[object] = elements(choices=type_inference)


@dataclass
class Category(SchemaBase):
    """Container holding a category description wit multiple parameters"""

    name: str = attribute()
    categories: List[object] = elements(
        choices=(
            {"name": "Series", "type": Series},
            {"name": "SeriesSet", "type": SeriesSet},
            {"name": "Parameter", "type": Parameter},
            {"name": "Category", "type": "Category"},
        ),
        default=list,
    )

    def add_category(
        self, category: Union[Series, SeriesSet, Parameter, "Category"]
    ) -> None:
        """Adds a category to the the container. Must be of any low-level AnIML type.

        Args:
            category (Union[Series, SeriesSet, Parameter, Category]): A category of results.
        """
        self.categories.append(category)
