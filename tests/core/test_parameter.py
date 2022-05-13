from unicodedata import category

from pyaniml.core.parameter import Parameter, Category
from pyaniml.core.series import SeriesSet, Series, IndividualValueSet
from pyaniml.core.enums import DataTypes, SIUnits
from pyaniml.core.unit import Unit


class TestParameter:
    """Tests the Parameter class"""

    def test_content(self):
        """Tests content conistency"""

        parameter = Parameter(value=10.0, name="Name", dtype=DataTypes.FLOAT32)

        assert parameter.value == 10.0
        assert parameter.name == "Name"
        assert parameter.dtype == DataTypes.FLOAT32


class TestCategory:
    """Tests the Catgeory class"""

    def test_content(self):
        """Tests content consistency"""

        category = Category(name="Name")

        assert category.name == "Name"
        assert isinstance(category.content, list)
        assert len(category.content) == 0

    def test_add_method(self):
        """Tests if the add_method is working properly"""

        # Set up an example object
        parameter = Parameter(value=10.0, name="Name", dtype=DataTypes.FLOAT32)

        # Add it to a Catgeory
        category = Category(name="Name")
        category.add_content(parameter)

        added: Parameter = category.content[0]

        assert added.name == "Name"
        assert added.value == 10.0
        assert added.dtype == DataTypes.FLOAT32
