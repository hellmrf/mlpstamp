"""Test main mlpstamps invocation with user input enabled (mocked)."""

import os

import pytest

from mlpstamps import main, utils


@pytest.fixture(scope='function')
def remove_additional_dirs():
    """Remove special directories which are created during the tests."""
    yield
    if os.path.isdir('fake-project'):
        utils.rmtree('fake-project')
    if os.path.isdir('fake-project-input-extra'):
        utils.rmtree('fake-project-input-extra')


@pytest.mark.usefixtures('clean_system', 'remove_additional_dirs')
def test_mlpstamps_local_with_input(monkeypatch) -> None:
    """Verify simple mlpstamps run results, without extra_context provided."""
    monkeypatch.setattr(
        'mlpstamps.prompt.read_user_variable',
        lambda _var, default, _prompts, _prefix: default,
    )
    main.mlpstamps('tests/fake-repo-pre/', no_input=False)
    assert os.path.isdir('tests/fake-repo-pre/{{mlpstamps.repo_name}}')
    assert not os.path.isdir('tests/fake-repo-pre/fake-project')
    assert os.path.isdir('fake-project')
    assert os.path.isfile('fake-project/README.rst')
    assert not os.path.exists('fake-project/json/')


@pytest.mark.usefixtures('clean_system', 'remove_additional_dirs')
def test_mlpstamps_input_extra_context(monkeypatch) -> None:
    """Verify simple mlpstamps run results, with extra_context provided."""
    monkeypatch.setattr(
        'mlpstamps.prompt.read_user_variable',
        lambda _var, default, _prompts, _prefix: default,
    )
    main.mlpstamps(
        'tests/fake-repo-pre',
        no_input=False,
        extra_context={'repo_name': 'fake-project-input-extra'},
    )
    assert os.path.isdir('fake-project-input-extra')
