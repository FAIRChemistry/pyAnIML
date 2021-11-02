from typing import List

from pydantic.dataclasses import dataclass
from pydantic import validate_arguments
from pyaniml.utility.utils import SchemaBase, element, attribute
from pyaniml.core.sample import Sample, SampleReference


@dataclass
class ExperimentStepSet(SchemaBase):
    """Container for experiment steps"""

    experiment_steps: List[str] = element(
        name="ExperimentStep", default=list
    )

    @validate_arguments
    def add_experiment_step(self, experiment_step) -> None:
        self.experiment_steps.append(experiment_step)


@dataclass
class SampleSet(SchemaBase):
    """Container for samples"""

    samples: List[Sample] = element(
        name="Sample", default=list
    )

    @validate_arguments
    def add_sample(self, sample: Sample) -> None:
        """Adds a sample to a sample set.

        Args:
            sample (Sample): Object describing a sample.
        """
        self.samples.append(sample)


@dataclass
class AuditTrailEntrySet(SchemaBase):
    """Container for audit trail entries"""

    audit_trail_entries: List[str] = element(
        name="AuditTrailEntry", default=list
    )

    @validate_arguments
    def add_audit_trail_entry(self, audit_trail_entry):
        self.audit_trail_entries.append(audit_trail_entry)


@dataclass
class SampleReferenceSet(SchemaBase):
    """Container for references to samples that have been defined in the AnIMLDocument"""

    sample_reference: SampleReference = element(
        name="SampleReference", default=list
    )
