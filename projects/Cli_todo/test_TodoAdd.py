import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:
    
    @pytest.mark.regression
    def test_add_task_to_context(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS': {}, 'LATEST': 0}
            add_task = 'task1'
            add(ctx, add_task)
            assert ctx['TASKS'][0] == add_task

    @pytest.mark.regression
    def test_add_task_echo_message(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS': {}, 'LATEST': 0}
            add_task = 'task1'
            result = runner.invoke(add, [ctx, add_task])
            assert result.output == 'Added task "task1" with ID 0\n'

    @pytest.mark.regression
    def test_add_task_write_to_file(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS': {}, 'LATEST': 0}
            add_task = 'task1'
            add(ctx, add_task)
            with open('todo.txt', 'r') as f:
                lines = f.readlines()
            assert lines[0].strip() == '1'
            assert lines[1].strip() == '0