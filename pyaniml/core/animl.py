from dataclasses import dataclass

from pyaniml.utility import element, SchemaBase
from pyaniml.core.experimentstep import ExperimentStepSet, ExperimentStep
from pyaniml.core.sample import SampleSet, Sample
from pyaniml.core.sets import AuditTrailEntrySet, SignatureSet


@dataclass
class AnIMLDocument(SchemaBase):
    """Container for an AnIML document"""

    class Meta:
        name = "AnIML"
        # namespace = "urn:org:astm:animl:schema:core:draft:0.90"

    sample_set: SampleSet = element(name="SampleSet", default=SampleSet)

    experiment_step_set: ExperimentStepSet = element(
        name="ExperimentStepSet", default=ExperimentStepSet
    )

    audit_trail_entry_set: AuditTrailEntrySet = element(
        name="AuditTrailEntrySet", default=AuditTrailEntrySet
    )

    signature_set: SignatureSet = element(name="SignatureSet", default=SignatureSet)

    def add_sample(self, sample: Sample):
        """Adds a sample to the sample set

        Args:
            sample (Sample): Container describing a sample
        """
        self.sample_set.add_sample(sample)

    def add_experiment_step(self, experiment_step: ExperimentStep):
        """Adds an experiment step to the experiment step set

        Args:
            experiment_step (ExperimentStep): Container describing an experiment step
        """
        self.experiment_step_set.add_experiment_step(experiment_step)
