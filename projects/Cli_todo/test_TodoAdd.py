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
            add_task = "Buy milk"
            add(ctx, add_task)
            assert ctx['TASKS'][0] == add_task

    @pytest.mark.regression
    def test_output_message_after_adding_task(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS': {}, 'LATEST': 0}
            add_task = "Buy eggs"
            result = runner.invoke(add, [ctx, add_task])
            assert result.output == f'Added task "{add_task}" with ID {ctx["LATEST"]}\n'

    @pytest.mark.regression
    def test_latest_index_after_adding_task(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS': {}, 'LATEST': 0}
            add_task = "Buy bread"
            add(ctx, add_task)
            assert ctx['LATEST'] == 1

    @pytest.mark.regression
    def test_write_tasks_to_file(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS': {}, 'LATEST': 0}
            add_task = "Buy butter"
            add(ctx, add_task)
            with open('./todo.txt', 'r') as f:
                lines = f.readlines()
            assert lines[1].strip() == f'0