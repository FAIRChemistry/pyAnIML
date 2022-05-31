import pytest

from typing import List
from dataclasses import dataclass

from pyaniml.utility.utils import SchemaBase, attribute, element, elements


class TestSchemaBase:
    @pytest.fixture
    def simple_model(self):
        """Sets up a simple model based on the utilities given"""

        @dataclass
        class SubElement(SchemaBase):
            """Element that contains a choices part, where based on the type an element will be created"""

            foo: str = attribute(name="Foo")
            choice: List[object] = elements(
                choices=(
                    {"name": "Float", "type": float},
                    {"name": "Integer", "type": int},
                )
            )

        @dataclass
        class Test(SchemaBase):
            """Top level element"""

            sub_element: SubElement = element(name="SubElement")

        return (Test, SubElement)

    @pytest.fixture
    def expected_xml(self):
        return open("./tests/fixtures/utils_xml.xml").read()

    @pytest.fixture
    def expected_json(self):
        return open("./tests/fixtures/utils_json.json").read()

    def test_to_xml(self, simple_model, expected_xml):
        """Tests serialization to XML"""

        Test, SubElement = simple_model

        sub = SubElement(foo="Foo", choice=[1.0, 10])
        model = Test(sub_element=sub)

        assert model.toXML() == expected_xml

    def test_to_json(self, simple_model, expected_json):
        """Tests serialization to XML"""

        Test, SubElement = simple_model

        sub = SubElement(foo="Foo", choice=[1.0, 10])
        model = Test(sub_element=sub)

        assert model.toJSON() == expected_json

    def test_json_init(self, simple_model):
        """Tests whether the model is correctly initialized via JSON"""

        Test, SubElement = simple_model

        # Build the expected model
        sub = SubElement(foo="Foo", choice=[1.0, 10])
        expected_model = Test(sub_element=sub)

        # Initialize the model
        json_string = open("./tests/fixtures/utils_json.json", "r").read()
        model = Test.fromJSONString(json_string)

        assert model == expected_model

    def test_xml_init(self, simple_model):
        """Tests whether the model is correctly initialized via JSON"""

        Test, SubElement = simple_model

        # Build the expected model
        sub = SubElement(foo="Foo", choice=[1.0, 10])
        expected_model = Test(sub_element=sub)

        # Initialize the model
        xml_string = open("./tests/fixtures/utils_xml.xml", "r").read()
        model = Test.fromXMLString(xml_string)

        assert model == expected_model
