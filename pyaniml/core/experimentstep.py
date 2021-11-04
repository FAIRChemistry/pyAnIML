from typing import Union
from dataclasses import dataclass
from pyaniml.utility import attribute, element, SchemaBase
from pyaniml.core.sample import Sample
from pyaniml.core.infrastructure import Infrastructure
from pyaniml.core.result import Result
from pyaniml.core.method import Method
from pyaniml.core.method import Device
from pyaniml.core.method import Author
from pyaniml.core.parameter import Parameter
from pyaniml.core.parameter import Category
from pyaniml.core.series import Series
from pyaniml.core.series import SeriesSet


@dataclass
class ExperimentStep(SchemaBase):
    """Container for metadata as well as measured data from an experiment"""

    name: str = attribute()
    experiment_step_id: str = attribute(name="experimentStepID")
    infrastructure: Infrastructure = element(
        name="Infrastructure", default=Infrastructure
    )
    method: Method = element(
        name="Method", default=Method
    )
    result: Result = element(
        name="Result", default=Result
    )

    def add_sample_reference(self, sample: Sample, role: str, sample_purpose: str):
        """Adds a sample to the infrastructure and creates a Reference.

        Args:
            sample (Sample): Sample object that has been defined beforehand
            role (str): The role of the sample in this experiment step.
            sample_purpose (str): The purpose the sample is intended for.
        """
        self.infrastructure.add_sample_reference(
            sample=sample, role=role, sample_purpose=sample_purpose
        )

    def add_method(self, method: Union[Device, Author, Parameter, Category]) -> None:
        """Adds a method-related property to the Method section of an experiment step

        Args:
            method (Union[Device, Author, Parameter, Category]): Characteristics of a method.
        """
        self.method.add_method(method)

    def add_result(self, result: Union[Series, SeriesSet, Parameter, Category]) -> None:
        """Adds a result to the Result section of an experiment step

        Args:
            result (Union[Series, SeriesSet, Parameter, Category]): Characteristics of a result.
        """
        self.result.add_result(result)