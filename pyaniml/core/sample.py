from dataclasses import dataclass
from typing import List, Union
from pyaniml.utility.utils import attribute, elements, SchemaBase
from pyaniml.core.parameter import Parameter, Category


@dataclass
class Sample(SchemaBase):
    """Describes an experiment sample"""

    id: str = attribute(name="sampleID")
    name: str = attribute(name="name")
    properties: List[object] = elements(
        choices=(
            {"name": "Parameter", "type": Parameter},
            {"name": "Category", "type": Category}
        ),
        default=list
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
    sample_purpose: str = attribute(name="samplePurpose")

    @classmethod
    def from_sample(cls, sample: Sample, role: str, sample_purpose: str):
        return cls(
            sample_id=sample.id,
            role=role,
            sample_purpose=sample_purpose
        )
