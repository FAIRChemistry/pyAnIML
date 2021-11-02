from typing import List
from pydantic.dataclasses import dataclass

from pyaniml.utility import element, SchemaBase

from pyaniml.core.sample import Sample
from pyaniml.core.sets import ExperimentStepSet
from pyaniml.core.sets import SampleSet
from pyaniml.core.sets import AuditTrailEntrySet


@dataclass
class AnIMLDocument(SchemaBase):
    """Container for an AnIML document"""

    class Meta:
        name = "AnIML"
        namespace = "urn:org:astm:animl:schema:core:draft:0.90"

    samples: SampleSet = element(
        name="SampleSet", default=SampleSet
    )

    experiment_steps: ExperimentStepSet = element(
        name="ExperimentStepSet", default=ExperimentStepSet
    )

    audit_tray_entries: AuditTrailEntrySet = element(
        name="AuditTrailEntrySet", default=AuditTrailEntrySet
    )


if __name__ == "__main__":
    animldoc = AnIMLDocument()
    animldoc.samples.add_sample(
        Sample(sample_id="Lol", name="Lol")
    )

    print(animldoc.toXML())
