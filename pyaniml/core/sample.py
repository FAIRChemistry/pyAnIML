from dataclasses import dataclass
from typing import List, Union

from pyaniml.utility.utils import attribute, elements, element, SchemaBase
from pyaniml.core.parameter import Parameter, Category
from pyaniml.core.enums import Purposes


@dataclass
class Sample(SchemaBase):
    """Describes an experiment sample"""

    name: str = attribute(name="name")
    id: str = attribute(name="sampleID")
    properties: List[object] = elements(
        choices=(
            {"name": "Parameter", "type": Parameter},
            {"name": "Category", "type": Category},
        ),
        default=list,
    )

    def add_property(self, property: Union[Parameter, Category]) -> None:
        """Adds a property of type [Parameter, Category] to an AnIML document.

        Args:
            property (object): Some kind of property that describes the sample.
        """

        self.properties.append(property)


@dataclass
class SampleReference(SchemaBase):
    """References an experiment sample"""

    sample_id: str = attribute(name="sampleID")
    role: str = attribute(name="role")
    sample_purpose: Purposes = attribute(name="samplePurpose")

    @classmethod
    def from_sample(cls, sample: Sample, role: str, sample_purpose: Purposes):
        return cls(sample_id=sample.id, role=role, sample_purpose=sample_purpose)


@dataclass
class SampleSet(SchemaBase):
    """Container for samples"""

    samples: List[Sample] = element(name="Sample", default=list)

    def add_sample(self, sample: Sample) -> None:
        """Adds a sample to a sample set.

        Args:
            sample (Sample): Object describing a sample.
        """
        self.samples.append(sample)


@dataclass
class SampleReferenceSet(SchemaBase):
    """Container for references to samples that have been defined in the AnIMLDocument"""

    sample_references: List[SampleReference] = element(
        name="SampleReference", default=list
    )

    def add_reference(self, sample: Sample, role: str, sample_purpose: Purposes):
        """Adds a sample reference to a sample set.

        Args:
            sample (Sample): Sample object to ensure correct ID assigment
            role (str): The role of the sample.
            sample_purpose (str): The purpose of the sample.
        """
        self.sample_references.append(
            SampleReference.from_sample(
                sample=sample, role=role, sample_purpose=sample_purpose
            )
        )
