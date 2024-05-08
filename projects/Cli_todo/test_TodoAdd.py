import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:

    @pytest.mark.positive
    def test_add_task_to_context(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        task = 'Test task'
        result = runner.invoke(add, [task], obj=ctx)
        assert ctx.obj['TASKS'][ctx.obj['LATEST']] == task

    @pytest.mark.positive
    def test_echo_task_and_id(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        task = 'Test task'
        result = runner.invoke(add, [task], obj=ctx)
        assert 'Added task "' + task + '" with ID ' + str(ctx.obj['LATEST']) in result.output

    @pytest.mark.positive
    def test_write_to_file(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        task = 'Test task'
        runner.invoke(add, [task], obj=ctx)
        with open('./todo.txt', 'r') as f:
            lines = f.readlines()
        assert lines[0].strip() == '1'
        assert lines[1].strip() == '0