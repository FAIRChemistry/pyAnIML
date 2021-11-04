from typing import List
from dataclasses import dataclass
from pydantic import validate_arguments
from pyaniml.utility.utils import SchemaBase, element
from pyaniml.core.sample import Sample, SampleReference
from pyaniml.core.experimentstep import ExperimentStep


@dataclass
class AuditTrailEntrySet(SchemaBase):
    """Container for audit trail entries"""

    audit_trail_entries: List[str] = element(
        name="AuditTrailEntry", default=list
    )

    @validate_arguments
    def add_audit_trail_entry(self, audit_trail_entry):
        self.audit_trail_entries.append(audit_trail_entry)
