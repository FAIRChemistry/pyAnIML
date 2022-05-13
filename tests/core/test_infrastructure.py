from pyaniml.core.infrastructure import Infrastructure
from pyaniml.core.sample import Sample, SampleReferenceSet
from pyaniml.core.enums import Purposes


class TestInfrastructure:
    """Tests the content and methods of the Infracsture class"""

    def test_content(self):
        """Tests the content of the Infracsture class"""

        infrastructure = Infrastructure()

        assert isinstance(infrastructure.sample_references, SampleReferenceSet)

    def test_add_method(self):
        """Tests the add_method of the Infracsture class"""

        # Set up a sample reference and add it
        sample = Sample(name="Name", id="ID")

        infrastructure = Infrastructure()
        infrastructure.add_sample_reference(
            sample=sample, role="Role", sample_purpose=Purposes.CONSUMED
        )

        added = infrastructure.sample_references.sample_references[0]

        assert added.sample_id == "ID"
        assert added.role == "Role"
        assert added.sample_purpose == Purposes.CONSUMED
