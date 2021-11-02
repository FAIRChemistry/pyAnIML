from typing import List

from pydantic.dataclasses import dataclass
from pyaniml.utility import attribute, element, SchemaBase


@dataclass
class ExperimentStep(SchemaBase):
    """Container for metadata as well as measured data from an experiment"""

    name: str = attribute()
    experiment_step_id: str = attribute(name="experimentStepID")


@dataclass
class Result(SchemaBase):
    """Container for experiment results"""

    name: str = attribute()
    series: List[Series] = element(name="Series")
    parameter: List[Parameter] = element(name="Parameter")
    series_set: List[SeriesSet] = element(name="SeriesSet")
    category: List[Category] = element(name="Category")
