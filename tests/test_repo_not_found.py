"""Testing invalid mlpstamps template repositories."""

import pytest

from mlpstamps import exceptions, main


def test_should_raise_error_if_repo_does_not_exist() -> None:
    """Cookiecutter invocation with non-exist repository should raise error."""
    with pytest.raises(exceptions.RepositoryNotFound):
        main.mlpstamps('definitely-not-a-valid-repo-dir')
