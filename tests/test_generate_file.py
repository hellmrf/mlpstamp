"""Tests for `generate_file` function, part of `generate_files` function workflow."""

import json
import os
import re
from pathlib import Path

import pytest
from jinja2 import FileSystemLoader
from jinja2.exceptions import TemplateSyntaxError

from mlpstamps import generate
from mlpstamps.environment import StrictEnvironment


@pytest.fixture(scope='function', autouse=True)
def tear_down():
    """
    Fixture. Remove the test text file which is created by the tests.

    Used for all tests in this file.
    """
    yield
    if os.path.exists('tests/files/cheese.txt'):
        os.remove('tests/files/cheese.txt')
    if os.path.exists('tests/files/cheese_lf_newlines.txt'):
        os.remove('tests/files/cheese_lf_newlines.txt')
    if os.path.exists('tests/files/cheese_crlf_newlines.txt'):
        os.remove('tests/files/cheese_crlf_newlines.txt')
    if os.path.exists('tests/files/cheese_mixed_newlines.txt'):
        os.remove('tests/files/cheese_mixed_newlines.txt')
    if os.path.exists('tests/files/{{mlpstamps.generate_file}}_mixed_newlines.txt'):
        os.remove('tests/files/{{mlpstamps.generate_file}}_mixed_newlines.txt')


@pytest.fixture
def env():
    """Fixture. Set Jinja2 environment settings for other tests."""
    environment = StrictEnvironment()
    environment.loader = FileSystemLoader('.')
    return environment


def test_generate_file(env) -> None:
    """Verify simple file is generated with rendered context data."""
    infile = 'tests/files/{{mlpstamps.generate_file}}.txt'
    generate.generate_file(
        project_dir=".",
        infile=infile,
        context={'mlpstamps': {'generate_file': 'cheese'}},
        env=env,
    )
    assert os.path.isfile('tests/files/cheese.txt')
    generated_text = Path('tests/files/cheese.txt').read_text()
    assert generated_text == 'Testing cheese'


def test_generate_file_jsonify_filter(env) -> None:
    """Verify jsonify filter works during files generation process."""
    infile = 'tests/files/{{mlpstamps.jsonify_file}}.txt'
    data = {'jsonify_file': 'cheese', 'type': 'roquefort'}
    generate.generate_file(
        project_dir=".", infile=infile, context={'mlpstamps': data}, env=env
    )
    assert os.path.isfile('tests/files/cheese.txt')
    generated_text = Path('tests/files/cheese.txt').read_text()
    assert json.loads(generated_text) == data


@pytest.mark.parametrize("length", (10, 40))
@pytest.mark.parametrize("punctuation", (True, False))
def test_generate_file_random_ascii_string(env, length, punctuation) -> None:
    """Verify correct work of random_ascii_string extension on file generation."""
    infile = 'tests/files/{{mlpstamps.random_string_file}}.txt'
    data = {'random_string_file': 'cheese'}
    context = {"mlpstamps": data, "length": length, "punctuation": punctuation}
    generate.generate_file(project_dir=".", infile=infile, context=context, env=env)
    assert os.path.isfile('tests/files/cheese.txt')
    generated_text = Path('tests/files/cheese.txt').read_text()
    assert len(generated_text) == length


def test_generate_file_with_true_condition(env) -> None:
    """Verify correct work of boolean condition in file name on file generation.

    This test has positive answer, so file should be rendered.
    """
    infile = (
        'tests/files/{% if mlpstamps.generate_file == \'y\' %}cheese.txt{% endif %}'
    )
    generate.generate_file(
        project_dir=".",
        infile=infile,
        context={'mlpstamps': {'generate_file': 'y'}},
        env=env,
    )
    assert os.path.isfile('tests/files/cheese.txt')
    generated_text = Path('tests/files/cheese.txt').read_text()
    assert generated_text == 'Testing that generate_file was y'


def test_generate_file_with_false_condition(env) -> None:
    """Verify correct work of boolean condition in file name on file generation.

    This test has negative answer, so file should not be rendered.
    """
    infile = (
        'tests/files/{% if mlpstamps.generate_file == \'y\' %}cheese.txt{% endif %}'
    )
    generate.generate_file(
        project_dir=".",
        infile=infile,
        context={'mlpstamps': {'generate_file': 'n'}},
        env=env,
    )
    assert not os.path.isfile('tests/files/cheese.txt')


@pytest.fixture
def expected_msg_regex():
    """Fixture. Used to ensure that exception generated text contain full data."""
    return re.compile(
        'Missing end of comment tag\n'
        ' {2}File "(.[/\\\\])*tests[/\\\\]files[/\\\\]syntax_error.txt", line 1\n'
        ' {4}I eat {{ syntax_error }} {# this comment is not closed}'
    )


def test_generate_file_verbose_template_syntax_error(env, expected_msg_regex) -> None:
    """Verify correct exception raised on syntax error in file before generation."""
    with pytest.raises(TemplateSyntaxError) as exception:
        generate.generate_file(
            project_dir=".",
            infile='tests/files/syntax_error.txt',
            context={'syntax_error': 'syntax_error'},
            env=env,
        )
    assert expected_msg_regex.match(str(exception.value))


def test_generate_file_does_not_translate_lf_newlines_to_crlf(env) -> None:
    """Verify that file generation use same line ending, as in source file."""
    infile = 'tests/files/{{mlpstamps.generate_file}}_lf_newlines.txt'
    generate.generate_file(
        project_dir=".",
        infile=infile,
        context={'mlpstamps': {'generate_file': 'cheese'}},
        env=env,
    )

    # this generated file should have a LF line ending
    gf = 'tests/files/cheese_lf_newlines.txt'
    with Path(gf).open(encoding='utf-8', newline='') as f:
        simple_text = f.readline()
    assert simple_text == 'newline is LF\n'
    assert f.newlines == '\n'


def test_generate_file_does_not_translate_crlf_newlines_to_lf(env) -> None:
    """Verify that file generation use same line ending, as in source file."""
    infile = 'tests/files/{{mlpstamps.generate_file}}_crlf_newlines.txt'
    generate.generate_file(
        project_dir=".",
        infile=infile,
        context={'mlpstamps': {'generate_file': 'cheese'}},
        env=env,
    )

    # this generated file should have a CRLF line ending
    gf = 'tests/files/cheese_crlf_newlines.txt'
    with Path(gf).open(encoding='utf-8', newline='') as f:
        simple_text = f.readline()
    assert simple_text == 'newline is CRLF\r\n'
    assert f.newlines == '\r\n'


def test_generate_file_handles_mixed_line_endings(env) -> None:
    """Verify that file generation gracefully handles mixed line endings."""
    infile = 'tests/files/{{mlpstamps.generate_file}}_mixed_newlines.txt'
    with open(infile, mode='w', encoding='utf-8', newline='') as f:
        f.write('newline is CRLF\r\n')
        f.write('newline is LF\n')
    generate.generate_file(
        project_dir=".",
        infile=infile,
        context={'mlpstamps': {'generate_file': 'cheese'}},
        env=env,
    )

    # this generated file should have either CRLF or LF line ending
    gf = 'tests/files/cheese_mixed_newlines.txt'
    with Path(gf).open(encoding='utf-8', newline='') as f:
        simple_text = f.readline()
    assert simple_text in ('newline is CRLF\r\n', 'newline is CRLF\n')
    assert f.newlines in ('\r\n', '\n')
