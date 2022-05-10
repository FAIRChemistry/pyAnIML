# Basic data types and mapping
# TODO extend to all parameter types

# Data types that are used within parameters and
# individual value sets
data_types = {int: "I", float: "F", str: "S", bool: "Boolean"}

# Tuple that is used to derive xsd:choice elements
# according to their type
type_inference = tuple(
    {"name": element_name, "type": data_type}
    for data_type, element_name in data_types.items()
)


# Datatypes which are supported via the
# parameter as well as series type
parameter_types = ["Int32", "Int64", "Float32", "Float64", "String"]

# Dependency enum describing the supported options for the
# dependencies attribute
dependencies = ["dependent", "independent"]

# Purpose enum describing supported sample purposes
purposes = ["produced", "consumed"]

# User types allowed for Author in Method of ExperimentStep
user_types = ["human", "device", "software"]

# Names of all SI Units
si_unit_name_list = ["1", "m", "kg", "s", "A", "K", "mol", "cd"]
