import pytest
from main import add


@pytest.mark.only
def test_add():
    assert add(1, 2) == 3


@pytest.mark.skip(reason="Not implemented yet")
def test_subtract():
    assert add(1, -2) == -1
