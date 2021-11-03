from dataclasses import dataclass
from typing import List, Union, Optional
from pyaniml.utility.utils import SchemaBase, elements, attribute
from pyaniml.core.series import Series
from pyaniml.core.series import SeriesSet
from pyaniml.core.parameter import Parameter
from pyaniml.core.parameter import Category


@dataclass
class Result(SchemaBase):
    """Container for experiment results"""

    results: List[object] = elements(
        choices=(
            {"name": "Series", "type": Series},
            {"name": "SeriesSet", "type": SeriesSet},
            {"name": "Parameter", "type": Parameter},
            {"name": "Category", "type": Category}
        ),
        default=list
    )

    def add_result(self, result: Union[Series, SeriesSet, Parameter, Category]) -> None:
        """Adds a measurement result to the the container. Must be of any low-level AnIML type.

        Args:
            result (Union[Series, SeriesSet, Parameter, Category]): The quantitive measurement results.
        """
        self.results.append(result)
