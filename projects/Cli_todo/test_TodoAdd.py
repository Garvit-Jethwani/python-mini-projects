import pytest
import click
from click.testing import CliRunner
from todo import add

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def mock_context():
    return {
        'TASKS': {1: 'Task 1', 2: 'Task 2'},
        'LATEST': 2
    }

@pytest.fixture
def mock_context_empty():
    return {
        'TASKS': {},
        'LATEST': 0
    }

@pytest.fixture
def mock_context_without_latest():
    return {
        'TASKS': {1: 'Task 1', 2: 'Task 2'}
    }

@pytest.fixture
def mock_context_file():
    return {
        'TASKS': {1: 'Task 1', 2: 'Task 2'},
        'LATEST': 2,
        'FILE': './todo.txt'
    }

class Test_TodoAdd:

    def test_add_task_to_context_list(self, runner, mock_context):
        result = runner.invoke(add, ['New Task'], obj=mock_context)
        assert mock_context['TASKS'][3] == 'New Task'

    def test_console_output(self, runner, mock_context):
        result = runner.invoke(add, ['New Task'], obj=mock_context)
        assert 'Added task "New Task" with ID 3' in result.output

    def test_write_to_file(self, runner, mock_context_file):
        runner.invoke(add, ['New Task'], obj=mock_context_file)
        with open(mock_context_file['FILE'], 'r') as f:
            lines = f.readlines()
        assert lines[0].strip() == '3'
        assert '3