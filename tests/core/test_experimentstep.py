from cmath import exp
from pyaniml.core.experimentstep import ExperimentStep, ExperimentStepSet
from pyaniml.core.infrastructure import Infrastructure
from pyaniml.core.method import Method
from pyaniml.core.result import Result
from pyaniml.core.sample import Sample
from pyaniml.core.method import Method, Software, Author, Device, Category
from pyaniml.core.enums import Purposes, UserTypes


class TestExperimentStep:
    def test_content(self):
        """Tests whether the content that is inserted is constant"""

        # Set up minimum element
        exp_step = ExperimentStep(name="Name", experiment_step_id="ID")

        assert exp_step.name == "Name"
        assert exp_step.experiment_step_id == "ID"
        assert isinstance(exp_step.infrastructure, Infrastructure)
        assert isinstance(exp_step.method, Method)
        assert isinstance(exp_step.result, Result)

    def test_add_sample_reference(self):
        """Tests whether the add method for sample reference is working properly"""

        # Create objects necessary
        exp_step = ExperimentStep(name="Name", experiment_step_id="ID")
        sample = Sample(name="Sample", id="ID")

        # Sample reference
        exp_step.add_sample_reference(
            sample=sample, role="Role", sample_purpose=Purposes.CONSUMED
        )

        # Extract the resulting object for readability
        added_sample = exp_step.infrastructure.sample_references.sample_references[0]

        assert added_sample.sample_id == "ID"
        assert added_sample.role == "Role"
        assert added_sample.sample_purpose == Purposes.CONSUMED

    def test_add_method(self):
        """Tests whether the add method for method is working properly"""

        # Create objects necessary
        exp_step = ExperimentStep(name="Name", experiment_step_id="ID")

        # Set up an author to add
        author = Author(
            user_type=UserTypes.HUMAN,
            name="Name",
            affiliation="Affil",
            role="Operator",
            email="email",
            phone="0000",
            location="Location",
        )

        exp_step.add_method(author)

        # Test author addition
        added_author: Author = exp_step.method.methods[0]

        assert added_author.user_type == UserTypes.HUMAN
        assert added_author.name == "Name"
        assert added_author.affiliation == "Affil"
        assert added_author.role == "Operator"
        assert added_author.email == "email"
        assert added_author.phone == "0000"
        assert added_author.location == "Location"

        # Set up a device to add
        device = Device(
            device_id="0000",
            manufacturer="Manufacturer",
            name="Name",
            firmware_version="Version",
            serial_number="0000",
        )

        exp_step.add_method(device)

        # Test device addition
        added_device: Device = exp_step.method.methods[1]

        assert added_device.device_id == "0000"
        assert added_device.manufacturer == "Manufacturer"
        assert added_device.name == "Name"
        assert added_device.firmware_version == "Version"
        assert added_device.serial_number == "0000"

        # Set up a software to add
        software = Software(
            manufacturer="Manufacturer",
            name="Name",
            version="Version",
            operating_system="OS",
        )

        exp_step.add_method(software)

        # Test software addition
        added_software: Software = exp_step.method.methods[2]

        assert added_software.manufacturer == "Manufacturer"
        assert added_software.name == "Name"
        assert added_software.version == "Version"
        assert added_software.operating_system == "OS"

        # Set up a categroy to add
        category = Category(name="Category")

        exp_step.add_method(category)

        # Test category addition
        added_category: Category = exp_step.method.methods[3]

        assert added_category.name == "Category"
        assert len(added_category.content) == 0

    def test_add_result(self):
        """Tests whether the add method for results is working properly"""

        # Create objects necessary
        exp_step = ExperimentStep(name="Name", experiment_step_id="ID")

        # Set up a category to add
        category = Category(name="Category")

        exp_step.add_result(category)

        # Test content
        added_category: Category = exp_step.result.results[0]

        assert added_category.name == "Category"
        assert len(added_category.content) == 0

class TestExperimentStepSet:

    def test_add_method(self):
        """Tests whether the addition of an ExperimentStep works properly"""

        # Set up an experiment set and step
        exp_set = ExperimentStepSet()
        exp_step = ExperimentStep(name="Name", experiment_step_id="ID")

        exp_set.add_experiment_step(exp_step)

        # Test the added step
        added_step: ExperimentStep = exp_set.experiment_steps[0]

        assert added_step.name == "Name"
        assert added_step.experiment_step_id == "ID"