import pytest
from todo import add
import click
from click.testing import CliRunner
import os

class Test_TodoAdd:
    
    @pytest.mark.regression
    def test_add_task_to_context(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS':{}, 'LATEST':1}
            add_task = "new task"
            add(ctx, add_task)
            assert ctx['TASKS'][ctx['LATEST']] == add_task
            assert ctx['LATEST'] == 1

    @pytest.mark.regression
    def test_echo_message(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS':{}, 'LATEST':1}
            add_task = "new task"
            result = runner.invoke(add, [ctx, add_task])
            assert result.output == 'Added task "' + add_task + '" with ID ' + str(ctx['LATEST']) + '\n'

    @pytest.mark.regression
    def test_write_to_file(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            ctx = {'TASKS':{}, 'LATEST':1}
            add_task = "new task"
            add(ctx, add_task)
            with open('todo.txt', 'r') as f:
                lines = f.readlines()
                assert lines[0].strip() == '2'
                assert lines[1].strip() == '1