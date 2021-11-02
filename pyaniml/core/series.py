from typing import List, Any

from pydantic import validator
from pydantic.dataclasses import dataclass
from pyaniml.utility.utils import SchemaBase, element, attribute
from pyaniml.core.enums import parameter_types, dependencies


@dataclass
class Series(SchemaBase):
    """Container holding a single Series of datapoints"""

    name: str = attribute()
    id: str = attribute(name="seriesID")
    data_type: str = attribute(name="SeriesType")
    dependency: str = attribute()
    plot_scale: str = attribute(name="plotScale", default="none")

    # Validators
    @validator("data_type")
    def verify_data_type(cls, data_type):
        if data_type not in parameter_types.values:
            raise TypeError(
                f"Invalid data type. Please choose from {parameter_types.values()}"
            )

    @validator("dependency")
    def verify_dependency(cls, dependency):
        if dependency not in dependencies:
            raise TypeError(
                f"Unknown dependency argument '{dependency}'. Please choose from {dependencies}"
            )


@dataclass
def IndividualValueSet(SchemaBase):
    """Container holding individual values of a measurement"""

    def add_data(self, data: List[Any]) -> None:
        self.data: Any = element(
            name=parameter_types.get()
        )


@dataclass
class SeriesSet(SchemaBase):
    """Container for multi-dimensional datasets"""

    name: str = attribute()
    series: List[Series] = element(
        name="Series", default=list
    )
