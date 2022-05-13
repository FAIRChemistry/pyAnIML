from dataclasses import dataclass
from typing import List, Union

from pyaniml.utility.utils import SchemaBase, elements
from pyaniml.core.series import SeriesSet
from pyaniml.core.parameter import Category


@dataclass
class Result(SchemaBase):
    """Container for experiment results"""

    results: List[object] = elements(
        choices=(
            {"name": "SeriesSet", "type": SeriesSet},
            {"name": "Category", "type": Category},
        ),
        default=list,
    )

    def add_result(self, result: Union[SeriesSet, Category]) -> None:
        """Adds a measurement result to the the container. Must be of any low-level AnIML type.

        Args:
            result (Union[SeriesSet, Category]): The quantitive measurement results.
        """
        self.results.append(result)
