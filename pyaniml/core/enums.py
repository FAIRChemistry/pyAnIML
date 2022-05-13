from enum import Enum


class DataTypeChoices(Enum):

    """
    This Enum stores the mapping from native Python types to the corresponding
    types in AnIMLs Series element.
    """

    I = "I"
    F = "F"
    S = "S"
    Boolean = "Boolean"

    @classmethod
    def get(cls):
        return (
            {"name": "I", "type": int},
            {"name": "F", "type": float},
            {"name": "S", "type": str},
            {"name": "Boolean", "type": bool},
        )


class DataTypes(Enum):

    """
    This Enum stores all data types that are supported as an attribute in AnIML
    """

    INT32 = "Int32"
    INT64 = "Int64"
    FLOAT32 = "Float32"
    FLOAT64 = "Float64"
    STRING = "String"


class Dependencies(Enum):

    """
    This Enum stores all types of dependencies found in AnIML.
    """

    DEPENDENT = "dependent"
    INDEPENDENT = "independent"


class Purposes(Enum):

    """
    This Enum stores all supported sample purposes in AnIML.
    """

    PRODUCED = "produced"
    CONSUMED = "consumed"


class UserTypes(Enum):

    """
    This Enum stores all supported user types in AnIML.
    """

    HUMAN = "human"
    DEVICE = "device"
    SOFTWARE = "software"


class SIUnits(Enum):

    """
    This Enum stores all supported SI units in AnIML.
    """

    DIMENSIONLESS = "1"
    METER = "m"
    GRAM = "g"
    SECOND = "s"
    AMPERE = "A"
    KELVIN = "K"
    MOL = "mol"
    CANDELA = "cd"
