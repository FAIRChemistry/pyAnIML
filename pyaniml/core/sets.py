from typing import List
from dataclasses import dataclass
from pyaniml.utility.utils import SchemaBase, element


@dataclass
class AuditTrailEntrySet(SchemaBase):
    """Container for audit trail entries"""

    audit_trail_entries: List[str] = element(name="AuditTrailEntry", default=list)

    def add_audit_trail_entry(self, audit_trail_entry):
        self.audit_trail_entries.append(audit_trail_entry)


@dataclass
class SignatureSet(SchemaBase):
    """Container for digital signatures"""

    signatures: List[str] = element(name="Signature", default=list)

    def add_signature(self, signature):
        self.signatures.append(signature)
