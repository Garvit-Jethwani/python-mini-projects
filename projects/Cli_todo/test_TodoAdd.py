import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:
    @pytest.mark.valid
    def test_add_task_to_context_list(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        result = runner.invoke(add, ['Test task'], obj=ctx)
        assert ctx.obj['TASKS'][0] == 'Test task'

    @pytest.mark.valid
    def test_echo_added_task_and_id(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        result = runner.invoke(add, ['Test task'], obj=ctx)
        assert 'Added task "Test task" with ID 0' in result.output

    @pytest.mark.valid
    def test_write_current_index_and_tasks_to_file(self):
        runner = CliRunner()
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        runner.invoke(add, ['Test task'], obj=ctx)
        with open('./todo.txt', 'r') as f:
            lines = f.readlines()
        assert '1\n' in lines
        assert '0