
import json

from typing import Any, Dict
from dataclasses import field
from pydantic.json import pydantic_encoder

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser


class SchemaBase:

    def toXML(self) -> str:
        """Serializes an abstract data model to XML.

        Returns:
            str: XML data model as string.
        """
        config = SerializerConfig(pretty_print=True)
        serializer = XmlSerializer(config=config)
        return serializer.render(self)

    def toJSON(self, indent: int = 2) -> str:
        """Serializes an abstract data model to JSON.

        Args:
            indent (int): Degree of indentation.

        Returns:
            str: JSON data model as string.
        """
        return json.dumps(
            self,
            indent=indent,
            default=pydantic_encoder
        )

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
        return cls.__pydantic_model__.parse_raw(json_string)


def _generateField(
    name: str,
    type: str,
    default: Any = None,
    choices: Dict[str, Any] = None,
    namespace: str = ""
):
    """Metafunction to generate a valid field for later XML serialization."""

    # Declare dict type
    metadata_dict: Dict[str, Any] = dict(
        name=name, type=type, namespace=namespace
    )

    if choices:
        metadata_dict['choices'] = choices

    if default:
        return field(
            default_factory=default,
            metadata=metadata_dict,
        )
    else:
        return field(
            metadata=metadata_dict,
        )


def attribute(name: str, default: Any = None):
    """Defines an attribute as an XML attribute.

        <parent name=XYZ />

    Args:
        name (str): The name of the attribute
        default (Any, optional): Default value. Defaults to None.

    Returns:
        field: Dataclass Field element, which adds all teh metadata needed to generate an XML
    """
    return _generateField(name, 'Attribute', default)


def element(name: str, default: Any = None):
    """Defines an attribute as an XML element.

        <name>XYZ</name>

    Args:
        name (str): The name of the attribute
        default (Any, optional): Default value. Defaults to None.

    Returns:
        field: Dataclass Field element, which adds all teh metadata needed to generate an XML
    """
    return _generateField(name, 'Element', default)
