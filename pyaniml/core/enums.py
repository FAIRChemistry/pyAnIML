# Basic data types and mapping
# TODO extend to all parameter types

# Data types that are used within parameters and
# individual value sets
data_types = {
    int: "I",
    float: "F",
    str: "S",
    bool: "Boolean"
}

# Tuple that is used to derive xsd:choice elements
# according to their type
type_inference = tuple(
    {"name": element_name, "type": data_type}
    for data_type, element_name in data_types.items()
)


# Datatypes which are supported via the
# parameter as well as series type
parameter_types = [
    "Int32", "Int64", "Float32", "Float64", "String"
]

# Dependency enum describing the supported options for the
# dependencies attribute
dependencies = [
    "dependent",
    "independent"
]
