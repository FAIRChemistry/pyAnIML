from pyaniml.core.series import Series, SeriesSet, IndividualValueSet
from pyaniml.core.unit import Unit, SIUnit
from pyaniml.core.enums import SIUnits, Dependencies, DataTypes


class TestSeries:
    """Tests the Series class"""

    def test_content(self):
        """Tests content consistency"""

        # Set up everything
        unit = Unit(
            label="label",
            quantity="quantity",
            si_unit=[SIUnit(si_name=SIUnits.GRAM, factor=1, exponent=1, offset=0)],
        )

        series = Series(
            name="Name",
            id="ID",
            data=[1, 2, 3, 4],
            dtype=DataTypes.INT32,
            unit=unit,
            dependency=Dependencies.DEPENDENT,
            plot_scale="none",
        )

        assert series.name == "Name"
        assert series.id == "ID"
        assert series.unit == unit
        assert series.dependency == Dependencies.DEPENDENT
        assert series.plot_scale == "none"
        assert isinstance(series.data, IndividualValueSet)
        assert series.data.data == [1, 2, 3, 4]


class TestSeriesSet:
    """Tests the SeriesSet class"""

    def test_content(self):
        """Tests content consistency"""

        # Set up everything
        unit = Unit(
            label="label",
            quantity="quantity",
            si_unit=[SIUnit(si_name=SIUnits.GRAM, factor=1, exponent=1, offset=0)],
        )

        series = Series(
            name="Name",
            id="ID",
            data=[1, 2, 3, 4],
            dtype=DataTypes.INT32,
            unit=unit,
            dependency=Dependencies.DEPENDENT,
            plot_scale="none",
        )

        # Create SeriesSet
        series_set = SeriesSet(name="Name", series=[series])

        assert series_set.name == "Name"
        assert series_set.series[0] == series
