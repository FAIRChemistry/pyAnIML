from pydantic.dataclasses import dataclass
from pyaniml.utility import attribute, SchemaBase


@dataclass
class Sample(SchemaBase):
    """Describes an experiment sample"""

    sample_id: str = attribute(name="sampleID")
    name: str = attribute(name="name")
