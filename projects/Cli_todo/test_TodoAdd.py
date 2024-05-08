import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:

    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.mark.regression
    def test_add_task_to_context(self, runner):
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 1})
        task = "Test Task"
        add(ctx, task)
        assert ctx.obj['TASKS'][ctx.obj['LATEST']] == task

    @pytest.mark.regression
    def test_echo_added_task(self, runner):
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 1})
        task = "Test Task"
        result = runner.invoke(add, [task], obj=ctx.obj)
        assert result.output.strip() == f'Added task "{task}" with ID {ctx.obj["LATEST"]}'

    @pytest.mark.regression
    def test_write_to_file(self, runner):
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 1})
        task = "Test Task"
        runner.invoke(add, [task], obj=ctx.obj)
        with open('./todo.txt', 'r') as f:
            lines = f.readlines()
        assert lines[1].strip() == f'{ctx.obj["LATEST"]}