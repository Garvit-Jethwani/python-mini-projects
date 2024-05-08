import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:

    @pytest.mark.positive
    def test_add_task_to_context_list(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = click.Context(add)
            ctx.obj = {'TASKS': {}, 'LATEST': 1}
            add(ctx, "Test task")

            assert ctx.obj['TASKS'][1] == "Test task"

    @pytest.mark.positive
    def test_task_addition_message(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = click.Context(add)
            ctx.obj = {'TASKS': {}, 'LATEST': 1}
            result = runner.invoke(add, ["Test task"], obj=ctx)

            assert 'Added task "Test task" with ID 1' in result.output

    @pytest.mark.positive
    def test_writing_to_todo_txt(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = click.Context(add)
            ctx.obj = {'TASKS': {}, 'LATEST': 1}
            runner.invoke(add, ["Test task"], obj=ctx)

            with open('todo.txt', 'r') as file:
                lines = file.readlines()

            assert lines[0] == '2\n'
            assert lines[1] == '1