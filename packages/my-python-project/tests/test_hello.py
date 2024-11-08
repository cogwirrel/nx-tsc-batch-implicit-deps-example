"""Hello unit test module."""

from my_python_project.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello my-python-project"
