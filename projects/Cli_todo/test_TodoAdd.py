import pytest
import click
from click.testing import CliRunner
from todo import add
from unittest.mock import patch, mock_open


class Test_TodoAdd:

    @pytest.mark.regression
    def test_add_task_to_context(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        task = 'Test Task'
        runner.invoke(add, ['Test Task'], obj=ctx)
        assert ctx.obj['TASKS'][ctx.obj['LATEST']] == task

    @pytest.mark.regression
    def test_echo_task_and_id(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        task = 'Test Task'
        result = runner.invoke(add, ['Test Task'], obj=ctx)
        assert 'Added task "Test Task" with ID 0' in result.output

    @pytest.mark.regression
    @patch("builtins.open", new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        task = 'Test Task'
        runner.invoke(add, ['Test Task'], obj=ctx)
        mock_file.assert_called_once_with('./todo.txt', 'w')
        mock_file.return_value.writelines.assert_called_once()

    @pytest.mark.negative
    def test_add_null_task(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        runner.invoke(add, [None], obj=ctx)
        assert ctx.obj['TASKS'] == {}
