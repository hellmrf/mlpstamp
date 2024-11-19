"""Tests for `repository_has_mlpstamps_json` function."""

import pytest

from mlpstamps.repository import repository_has_mlpstamps_json


def test_valid_repository() -> None:
    """Validate correct response if `mlpstamps.json` file exist."""
    assert repository_has_mlpstamps_json('tests/fake-repo')


@pytest.mark.parametrize(
    'invalid_repository', (['tests/fake-repo-bad', 'tests/unknown-repo'])
)
def test_invalid_repository(invalid_repository) -> None:
    """Validate correct response if `mlpstamps.json` file not exist."""
    assert not repository_has_mlpstamps_json(invalid_repository)
