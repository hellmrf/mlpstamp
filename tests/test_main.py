"""Collection of tests around mlpstamps's replay feature."""

from mlpstamps.main import mlpstamps


def test_original_mlpstamps_options_preserved_in__mlpstamps(
    monkeypatch,
    mocker,
    user_config_file,
) -> None:
    """Preserve original context options.

    Tests you can access the original context options via
    `context['_mlpstamps']`.
    """
    monkeypatch.chdir('tests/fake-repo-tmpl-_mlpstamps')
    mock_generate_files = mocker.patch('mlpstamps.main.generate_files')
    mlpstamps(
        '.',
        no_input=True,
        replay=False,
        config_file=user_config_file,
    )
    assert mock_generate_files.call_args[1]['context']['_mlpstamps'][
        'test_list'
    ] == [1, 2, 3, 4]
    assert mock_generate_files.call_args[1]['context']['_mlpstamps'][
        'test_dict'
    ] == {"foo": "bar"}


def test_replay_dump_template_name(
    monkeypatch, mocker, user_config_data, user_config_file
) -> None:
    """Check that replay_dump is called with a valid template_name.

    Template name must not be a relative path.

    Otherwise files such as ``..json`` are created, which are not just cryptic
    but also later mistaken for replay files of other templates if invoked with
    '.' and '--replay'.

    Change the current working directory temporarily to 'tests/fake-repo-tmpl'
    for this test and call mlpstamps with '.' for the target template.
    """
    monkeypatch.chdir('tests/fake-repo-tmpl')

    mock_replay_dump = mocker.patch('mlpstamps.main.dump')
    mocker.patch('mlpstamps.main.generate_files')

    mlpstamps(
        '.',
        no_input=True,
        replay=False,
        config_file=user_config_file,
    )

    mock_replay_dump.assert_called_once_with(
        user_config_data['replay_dir'],
        'fake-repo-tmpl',
        mocker.ANY,
    )


def test_replay_load_template_name(
    monkeypatch, mocker, user_config_data, user_config_file
) -> None:
    """Check that replay_load is called correctly.

    Calls require valid template_name that is not a relative path.

    Change the current working directory temporarily to 'tests/fake-repo-tmpl'
    for this test and call mlpstamps with '.' for the target template.
    """
    monkeypatch.chdir('tests/fake-repo-tmpl')

    mock_replay_load = mocker.patch('mlpstamps.main.load')
    mocker.patch('mlpstamps.main.generate_context').return_value = {
        'mlpstamps': {}
    }
    mocker.patch('mlpstamps.main.generate_files')
    mocker.patch('mlpstamps.main.dump')

    mlpstamps(
        '.',
        replay=True,
        config_file=user_config_file,
    )

    mock_replay_load.assert_called_once_with(
        user_config_data['replay_dir'],
        'fake-repo-tmpl',
    )


def test_custom_replay_file(monkeypatch, mocker, user_config_file) -> None:
    """Check that reply.load is called with the custom replay_file."""
    monkeypatch.chdir('tests/fake-repo-tmpl')

    mock_replay_load = mocker.patch('mlpstamps.main.load')
    mocker.patch('mlpstamps.main.generate_context').return_value = {
        'mlpstamps': {}
    }
    mocker.patch('mlpstamps.main.generate_files')
    mocker.patch('mlpstamps.main.dump')

    mlpstamps(
        '.',
        replay='./custom-replay-file',
        config_file=user_config_file,
    )

    mock_replay_load.assert_called_once_with(
        '.',
        'custom-replay-file',
    )
