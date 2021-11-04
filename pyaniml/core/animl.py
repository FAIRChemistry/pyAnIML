from dataclasses import dataclass
from pyaniml.utility import element, SchemaBase
from pyaniml.core.experimentstep import ExperimentStepSet
from pyaniml.core.sample import SampleSet
from pyaniml.core.sets import AuditTrailEntrySet


@dataclass
class AnIMLDocument(SchemaBase):
    """Container for an AnIML document"""

    class Meta:
        name = "AnIML"
        # namespace = "urn:org:astm:animl:schema:core:draft:0.90"

    samples: SampleSet = element(
        name="SampleSet", default=SampleSet
    )

    experiment_steps: ExperimentStepSet = element(
        name="ExperimentStepSet", default=ExperimentStepSet
    )

    audit_tray_entries: AuditTrailEntrySet = element(
        name="AuditTrailEntrySet", default=AuditTrailEntrySet
    )

    def add_sample(self, sample):
        """Adds a sample to the sample set

        Args:
            sample (Sample): Container describing a sample
        """
        self.samples.add_sample(sample)

    def add_experiment_step(self, experiment_step):
        """Adds an experiment step to the experiment step set

        Args:
            experiment_step (ExperimentStep): Container describing an experiment step
        """
        self.experiment_steps.add_experiment_step(experiment_step)
