"""Collection of tests around loading extensions."""

import pytest

from mlpstamps.environment import StrictEnvironment
from mlpstamps.exceptions import UnknownExtension


def test_env_should_raise_for_unknown_extension() -> None:
    """Test should raise if extension not installed in system."""
    context = {'mlpstamps': {'_extensions': ['foobar']}}

    with pytest.raises(UnknownExtension) as err:
        StrictEnvironment(context=context, keep_trailing_newline=True)

    assert 'Unable to load extension: ' in str(err.value)


def test_env_should_come_with_default_extensions() -> None:
    """Verify default extensions loaded with StrictEnvironment."""
    env = StrictEnvironment(keep_trailing_newline=True)
    assert 'mlpstamps.extensions.JsonifyExtension' in env.extensions
    assert 'mlpstamps.extensions.RandomStringExtension' in env.extensions
    assert 'mlpstamps.extensions.SlugifyExtension' in env.extensions
    assert 'mlpstamps.extensions.TimeExtension' in env.extensions
    assert 'mlpstamps.extensions.UUIDExtension' in env.extensions
