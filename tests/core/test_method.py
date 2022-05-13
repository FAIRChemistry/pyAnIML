from pyaniml.core.method import Method, Author, Device, Software, Category
from pyaniml.core.enums import UserTypes


class TestAuthor:
    """Tests the Author class"""

    def test_content(self):
        """Tests content conistency"""

        author = Author(
            user_type=UserTypes.HUMAN,
            name="Name",
            affiliation="Affil",
            role="Role",
            email="Mail@Mail.com",
            phone="0000",
            location="Location",
        )

        assert author.user_type == UserTypes.HUMAN
        assert author.name == "Name"
        assert author.affiliation == "Affil"
        assert author.role == "Role"
        assert author.email == "Mail@Mail.com"
        assert author.phone == "0000"
        assert author.location == "Location"


class TestDevice:
    """Tests the Device class"""

    def test_content(self):
        """Tests content conistency"""

        device = Device(
            device_id="ID",
            manufacturer="Manufacturer",
            name="Name",
            firmware_version="1.2.2",
            serial_number="0000",
        )

        assert device.device_id == "ID"
        assert device.manufacturer == "Manufacturer"
        assert device.name == "Name"
        assert device.firmware_version == "1.2.2"
        assert device.serial_number == "0000"


class TestSoftware:
    """Tests the Software class"""

    def test_content(self):
        """Tests content conistency"""

        software = Software(
            manufacturer="Manufacturer",
            name="Name",
            version="1.2.2",
            operating_system="OS",
        )


class TestMethod:
    """Tests the Method class"""

    def test_content(self):
        """Tests content conistency"""

        method = Method()

        assert isinstance(method.methods, list)
        assert len(method.methods) == 0

    def test_add_method(self):
        """Tests the add_method"""

        # Set up everything that can be added
        author = Author(
            user_type=UserTypes.HUMAN,
            name="Name",
            affiliation="Affil",
            role="Role",
            email="Mail@Mail.com",
            phone="0000",
            location="Location",
        )

        device = Device(
            device_id="ID",
            manufacturer="Manufacturer",
            name="Name",
            firmware_version="1.2.2",
            serial_number="0000",
        )

        software = Software(
            manufacturer="Manufacturer",
            name="Name",
            version="1.2.2",
            operating_system="OS",
        )

        # Set up method and add all parts
        method = Method()
        method.add_method(author)
        method.add_method(device)
        method.add_method(software)

        assert len(method.methods) > 0
        assert isinstance(method.methods[0], Author)
        assert isinstance(method.methods[1], Device)
        assert isinstance(method.methods[2], Software)
