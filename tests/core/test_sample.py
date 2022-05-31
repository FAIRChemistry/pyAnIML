from pyaniml.core.sample import Sample, SampleReference, SampleSet, SampleReferenceSet
from pyaniml.core.parameter import Parameter
from pyaniml.core.enums import DataTypes, Purposes


class TestSample:
    """Tests the Sample class"""

    def test_content(self):
        """Tests content consistency"""

        sample = Sample(name="Name", id="ID")

        assert sample.name == "Name"
        assert sample.id == "ID"
        assert isinstance(sample.properties, list)
        assert len(sample.properties) == 0

    def test_add_method(self):
        """Tests the add_method working properly"""

        # Set up a property
        parameter = Parameter(value=10.0, name="Name", dtype=DataTypes.FLOAT32)

        sample = Sample(name="Name", id="ID")
        sample.add_property(parameter)

        added: Parameter = sample.properties[0]

        assert added.name == "Name"
        assert added.value == 10.0
        assert added.dtype == DataTypes.FLOAT32


class TestSampleReference:
    """Tests the SampleReference class"""

    def test_content(self):
        """Tests content consistency"""

        sample_ref = SampleReference(
            sample_id="ID", role="Role", sample_purpose=Purposes.CONSUMED
        )

        assert sample_ref.sample_id == "ID"
        assert sample_ref.role == "Role"
        assert sample_ref.sample_purpose == Purposes.CONSUMED

    def test_from_sample(self):
        """Tests the classmethod from_sample to work properly"""

        sample = Sample(name="Name", id="ID")

        sample_ref = SampleReference.from_sample(
            sample=sample, role="Role", sample_purpose=Purposes.CONSUMED
        )

        assert sample_ref.sample_id == "ID"
        assert sample_ref.role == "Role"
        assert sample_ref.sample_purpose == Purposes.CONSUMED


class TestSampleSet:
    """Tests the SampleSet class"""

    def test_content(self):
        """Tests content consistency"""

        sample_set = SampleSet()

        assert isinstance(sample_set.samples, list)
        assert len(sample_set.samples) == 0

    def test_add_method(self):
        """Tests the add_method to work properly"""

        # Set up a sample
        sample = Sample(name="Name", id="ID")

        sample_set = SampleSet()
        sample_set.add_sample(sample)

        added = sample_set.samples[0]

        assert added.id == "ID"
        assert added.name == "Name"


class TestSampleReferenceSet:
    """Tests the SampleReferenceSet class"""

    def test_content(self):
        """Tests content consistency"""

        sample_ref_set = SampleReferenceSet()

        assert isinstance(sample_ref_set.sample_references, list)
        assert len(sample_ref_set.sample_references) == 0

    def test_add_method(self):
        """Tests the add_method to work properly"""

        sample = Sample(name="Name", id="ID")
        sample_ref_set = SampleReferenceSet()
        sample_ref_set.add_reference(
            sample, role="Role", sample_purpose=Purposes.CONSUMED
        )

        added = sample_ref_set.sample_references[0]

        assert added.sample_id == "ID"
        assert added.role == "Role"
        assert added.sample_purpose == Purposes.CONSUMED
