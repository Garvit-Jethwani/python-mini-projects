import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:

    @pytest.mark.positive
    def test_add_task_to_context(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = click.Context(add)
            ctx.obj = {'TASKS': {}, 'LATEST': 0}
            task = 'Test Task'
            add(ctx, task)
            assert ctx.obj['TASKS'][0] == task
            assert ctx.obj['LATEST'] == 0

    @pytest.mark.positive
    def test_echo_message_after_adding_task(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = click.Context(add)
            ctx.obj = {'TASKS': {}, 'LATEST': 0}
            task = 'Test Task'
            result = runner.invoke(add, [task], obj=ctx)
            assert result.output.strip() == f'Added task "{task}" with ID 0'

    @pytest.mark.positive
    def test_write_tasks_to_file(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = click.Context(add)
            ctx.obj = {'TASKS': {}, 'LATEST': 0}
            task = 'Test Task'
            add(ctx, task)
            with open('./todo.txt', 'r') as f:
                lines = f.readlines()
                assert lines[0].strip() == '1'
                assert lines[1].strip() == f'0