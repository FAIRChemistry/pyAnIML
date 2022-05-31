from typing import Union, List
from dataclasses import dataclass

from pyaniml.utility import attribute, element, SchemaBase
from pyaniml.core.sample import Sample
from pyaniml.core.infrastructure import Infrastructure
from pyaniml.core.result import Result
from pyaniml.core.method import Method, Software
from pyaniml.core.method import Device
from pyaniml.core.method import Author
from pyaniml.core.parameter import Category
from pyaniml.core.series import SeriesSet
from pyaniml.core.enums import Purposes


@dataclass
class ExperimentStep(SchemaBase):
    """Container for metadata as well as measured data from an experiment"""

    name: str = attribute()
    experiment_step_id: str = attribute(name="experimentStepID")
    infrastructure: Infrastructure = element(
        name="Infrastructure", default=Infrastructure
    )
    method: Method = element(name="Method", default=Method)
    result: Result = element(name="Result", default=Result)

    def add_sample_reference(self, sample: Sample, role: str, sample_purpose: Purposes):
        """Adds a sample to the infrastructure and creates a Reference.

        Args:
            sample (Sample): Sample object that has been defined beforehand
            role (str): The role of the sample in this experiment step.
            sample_purpose (str): The purpose the sample is intended for.
        """
        self.infrastructure.add_sample_reference(
            sample=sample, role=role, sample_purpose=sample_purpose
        )

    def add_method(self, method: Union[Author, Device, Software, Category]) -> None:
        """Adds a method-related property to the Method section of an experiment step

        Args:
            method (Union[Author, Device, Software, Category]): Characteristics of a method.
        """
        self.method.add_method(method)

    def add_result(self, result: Union[SeriesSet, Category]) -> None:
        """Adds a result to the Result section of an experiment step

        Args:
            result (Union[SeriesSet, Category]): Characteristics of a result.
        """
        self.result.add_result(result)


@dataclass
class ExperimentStepSet(SchemaBase):
    """Container for experiment steps"""

    experiment_steps: List[ExperimentStep] = element(
        name="ExperimentStep", default=list
    )

    def add_experiment_step(self, experiment_step: ExperimentStep) -> None:
        """Adds an experiment step to the experiment set.

        Args:
            experiment_step (ExperimentStep): Object describing an experiment step.
        """
        self.experiment_steps.append(experiment_step)
