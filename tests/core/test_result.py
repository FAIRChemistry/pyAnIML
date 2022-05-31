from pyaniml.core.result import Result
from pyaniml.core.parameter import Category


class TestResult:
    """Tests the Result class"""

    def test_content(self):
        """Tests content consistency"""

        result = Result()

        assert isinstance(result.results, list)
        assert len(result.results) == 0

    def test_add_method(self):
        """Tests the add_method wokring properly"""

        # Set up a catgeory to add
        category = Category(name="Name")

        # Set up result and add category
        result = Result()
        result.add_result(category)

        added: Category = result.results[0]

        assert added.name == "Name"
        assert isinstance(added.content, list)
        assert len(added.content) == 0
