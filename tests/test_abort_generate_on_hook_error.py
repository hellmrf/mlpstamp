"""
test_abort_generate_on_hook_error.

Tests to ensure mlpstamps properly exits with a non-zero exit code whenever
errors occur in (optional) pre- or pos-gen hooks.
"""

import pytest

from mlpstamps import exceptions, generate


@pytest.mark.parametrize(
    ("abort_pre_gen", "abort_post_gen"),
    (("yes", "no"), ("no", "yes")),
    ids=("pre_gen_hook_raises_error", "post_gen_hook_raises_error"),
)
@pytest.mark.usefixtures("clean_system")
def test_hooks_raises_errors(tmp_path, abort_pre_gen, abort_post_gen) -> None:
    """Verify pre- and pos-gen errors raises correct error code from script.

    This allows developers to make different error codes in their code,
    for different errors.
    """
    context = {
        "mlpstamps": {
            "repo_dir": "foobar",
            "abort_pre_gen": abort_pre_gen,
            "abort_post_gen": abort_post_gen,
        }
    }

    with pytest.raises(exceptions.FailedHookException):
        generate.generate_files(
            repo_dir="tests/hooks-abort-render",
            context=context,
            output_dir=str(tmp_path),
        )
    assert not tmp_path.joinpath("foobar").is_dir()
