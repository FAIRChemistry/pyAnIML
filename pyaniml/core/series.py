from typing import List, Union
from dataclasses import dataclass
from pyaniml.core.unit import Unit
from pyaniml.utility.utils import SchemaBase, element, attribute, elements
from pyaniml.core.enums import DataTypeChoices, Dependencies, DataTypes


@dataclass
class IndividualValueSet(SchemaBase):
    """Container holding individual values of a measurement"""

    data: List[object] = elements(default=list, choices=DataTypeChoices.get())


@dataclass
class Series(SchemaBase):
    """Container holding a single Series of datapoints"""

    name: str = attribute()
    id: str = attribute(name="seriesID")
    data: IndividualValueSet = element(name="IndividualValueSet")
    unit: Unit = element(name="Unit")
    dtype: DataTypes = attribute(name="SeriesType")
    dependency: Dependencies = attribute()
    plot_scale: str = attribute(name="plotScale")

    def __post_init__(self):
        """Used to convert a list of values to an IndividualValueSet"""

        self.data = IndividualValueSet(data=self.data)


@dataclass
class SeriesSet(SchemaBase):
    """Container for multi-dimensional datasets"""

    name: str = attribute()
    series: List[Series] = element(name="Series", default=list)
