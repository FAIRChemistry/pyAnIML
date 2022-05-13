from typing import Any, Dict, Tuple, Optional
from dataclasses import field
from pydantic.json import pydantic_encoder

from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser


class SchemaBase:
    def toXML(self) -> str:
        """Serializes an abstract data model to XML.

        Returns:
            str: XML data model as string.
        """
        config = SerializerConfig(pretty_print=True)
        serializer = XmlSerializer(config=config)
        return serializer.render(self)

    def toJSON(self) -> str:
        """Serializes an abstract data model to JSON.

        Args:
            indent (int): Degree of indentation.

        Returns:
            str: JSON data model as string.
        """
        config = SerializerConfig(pretty_print=True)
        serializer = JsonSerializer(context=XmlContext(), config=config)
        return serializer.render(self)

    def toDict(self) -> str:
        """Serializes an abstract data model to a dictionary.

        Returns:
            Dict[Str, Any]: JSON data model as string.
        """
        return pydantic_encoder(self)

    def JSONSchema(self) -> Dict[str, Any]:
        return self.__pydantic_model__.schema()

    @classmethod
    def fromXMLString(cls, xml_string: str):
        """Initializes an object model from an XML string.

        Args:
            xml_string (str): XML data model as string.

        Returns:
            Any: Object model that has been parsed from the XML string.
        """
        parser = XmlParser(context=XmlContext())
        return parser.from_string(xml_string, cls)

    @classmethod
    def fromJSONString(cls, json_string: str):
        """Initializes an object model from a JSON string.

        Args:
            json_string (str): JSON data model as string.

        Returns:
            Any: Object model that has been parsed from the JSON string.
        """

        parser = JsonParser(context=XmlContext())
        return parser.from_string(json_string, cls)


def _generateField(
    type: str,
    name: Optional[str] = None,
    default: Any = None,
    default_value: Any = None,
    choices: Optional[Tuple[Dict[str, Any], ...]] = None,
):
    """Metafunction to generate a valid field for later XML serialization."""

    # Declare dict type
    metadata_dict: Dict[str, Any] = dict(type=type)

    param_dict: Dict[str, Any] = {}

    if choices:
        metadata_dict["choices"] = choices
    if name:
        metadata_dict["name"] = name

    if default:
        param_dict["default_factory"] = default
    if default_value is not None:
        param_dict["default"] = default_value

    return field(**param_dict, metadata=metadata_dict)


def attribute(
    name: Optional[str] = None, default: Any = None, default_value: Any = None
):
    """Defines an attribute as an XML attribute.

        <parent name=XYZ />

    Args:
        name (str): The name of the attribute
        default (Any, optional): Default callable for mutable data types. Defaults to None.

    Returns:
        field: Dataclass Field element, which adds all teh metadata needed to generate an XML model
    """
    return _generateField(
        type="Attribute", name=name, default=default, default_value=default_value
    )


def element(name: Optional[str] = None, default: Any = None, default_value: Any = None):
    """Defines an attribute as an XML element.

        <name>XYZ</name>

    Args:
        name (str): The name of the attribute
        default (Any, optional): Default callable for mutable data types. Defaults to None.

    Returns:
        field: Dataclass Field element, which adds all teh metadata needed to generate an XML model
    """
    return _generateField(
        type="Element", name=name, default=default, default_value=default_value
    )


def elements(choices: Tuple[Dict[str, Any], ...], default: Any = None):
    """Defines an xsd:choices reference as an XML element.

        <choices1>XYZ</choices1>
        <choices2>XYZ</choices2>

    Args:
        choices (str): The types of elements that can be defined in the model.
        default (Any, optional): Default callable for mutable data types. Defaults to None.

    Returns:
        field: Dataclass Field element, which adds all teh metadata needed to generate an XML model
    """
    return _generateField(type="Elements", choices=choices, default=default)
