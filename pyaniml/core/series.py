import pydantic

from typing import List
from dataclasses import dataclass
from pyaniml.utility.utils import SchemaBase, element, attribute, elements
from pyaniml.core.enums import data_types, dependencies, type_inference


@dataclass
class IndividualValueSet(SchemaBase):
    """Container holding individual values of a measurement"""

    data: List[object] = elements(
        default=list,
        choices=type_inference
    )


@dataclass
class Series(SchemaBase):
    """Container holding a single Series of datapoints"""

    name: str = attribute()
    id: str = attribute(name="seriesID")
    data: IndividualValueSet = element(name="IndividualValueSet")
    data_type: str = attribute(name="SeriesType")
    dependency: str = attribute()
    plot_scale: str = attribute(name="plotScale")

    # Validators
    @staticmethod
    def verify_data_type(data_type):
        if data_type not in data_types.values:
            raise TypeError(
                f"Invalid data type. Please choose from {data_types.values()}"
            )

    @staticmethod
    def verify_dependency(dependency):
        if dependency not in dependencies:
            raise TypeError(
                f"Unknown dependency argument '{dependency}'. Please choose from {dependencies}"
            )


@ dataclass
class SeriesSet(SchemaBase):
    """Container for multi-dimensional datasets"""

    name: str = attribute()
    series: List[Series] = element(
        name="Series", default=list
    )
