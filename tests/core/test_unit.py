from pyaniml.core.unit import SIUnit, Unit
from pyaniml.core.enums import SIUnits


class TestSIUnit:
    """Tests the SIUnit class"""

    def test_content(self):
        """Tests content consistency"""

        si_unit = SIUnit(si_name=SIUnits.GRAM, factor=1.0, exponent=1.0, offset=0)

        assert si_unit.si_name == SIUnits.GRAM
        assert si_unit.factor == 1.0
        assert si_unit.exponent == 1.0
        assert si_unit.offset == 0


class TestUnit:
    """Tests the Unit class"""

    def test_content(self):
        """Tests content consistency"""

        unit = Unit(
            label="label",
            quantity="quantity",
            si_unit=[SIUnit(si_name=SIUnits.GRAM, factor=1, exponent=1, offset=0)],
        )

        assert unit.label == "label"
        assert unit.quantity == "quantity"
        assert unit.si_unit[0].si_name == SIUnits.GRAM
        assert unit.si_unit[0].factor == 1
        assert unit.si_unit[0].exponent == 1
        assert unit.si_unit[0].offset == 0

    def test_add_method(self):
        """Tests the add_method to work properly"""

        unit = Unit(
            label="label",
            quantity="quantity",
        )

        assert unit.label == "label"
        assert unit.quantity == "quantity"
        assert isinstance(unit.si_unit, list)
        assert len(unit.si_unit) == 0

        unit.add_si_unit(SIUnit(si_name=SIUnits.GRAM, factor=1, exponent=1, offset=0))

        assert unit.si_unit[0].si_name == SIUnits.GRAM
        assert unit.si_unit[0].factor == 1
        assert unit.si_unit[0].exponent == 1
        assert unit.si_unit[0].offset == 0
