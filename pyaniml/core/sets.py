from typing import List
from dataclasses import dataclass
from pydantic import validate_arguments
from pyaniml.utility.utils import SchemaBase, element
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

    def add_reference(self, sample: Sample, role: str, sample_purpose: str):
        """Adds a sample reference to a sample set.

        Args:
            sample (Sample): Sample object to ensure correct ID assigment
            role (str): The role of the sample.
            sample_purpose (str): The purpose of the sample.
        """
        self.sample_references.append(
            SampleReference.from_sample(
                sample=sample, role=role, sample_purpose=sample_purpose)
        )


@dataclass
class AuditTrailEntrySet(SchemaBase):
    """Container for audit trail entries"""

    audit_trail_entries: List[str] = element(
        name="AuditTrailEntry", default=list
    )

    @validate_arguments
    def add_audit_trail_entry(self, audit_trail_entry):
        self.audit_trail_entries.append(audit_trail_entry)
