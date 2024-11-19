"""Test mlpstamps invocation with nested configuration structure."""

from pathlib import Path

import pytest

from mlpstamps import main


@pytest.mark.parametrize(
    "template_dir,output_dir",
    [
        ["fake-nested-templates", "fake-project"],
        ["fake-nested-templates-old-style", "fake-package"],
    ],
)
def test_mlpstamps_nested_templates(
    mocker, template_dir: str, output_dir: str
) -> None:
    """Verify mlpstamps nested configuration files mechanism."""
    mock_generate_files = mocker.patch("mlpstamps.main.generate_files")
    main_dir = (Path("tests") / template_dir).resolve()
    main.mlpstamps(f"{main_dir}", no_input=True)
    expected = (Path(main_dir) / output_dir).resolve()
    assert mock_generate_files.call_args[1]["repo_dir"] == f"{expected}"
