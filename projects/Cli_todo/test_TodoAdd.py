import pytest
import click
from click.testing import CliRunner
from todo import add

class Test_TodoAdd:

    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def ctx(self):
        return {"TASKS": {1: "Task 1", 2: "Task 2"}, "LATEST": 2}

    def test_add_task_to_context(self, runner, ctx):
        result = runner.invoke(add, ['Task 3'], obj=ctx)
        assert ctx["TASKS"] == {1: "Task 1", 2: "Task 2", 3: "Task 3"}
        assert ctx["LATEST"] == 3

    def test_echo_message(self, runner, ctx):
        result = runner.invoke(add, ['Task 3'], obj=ctx)
        assert 'Added task "Task 3" with ID 3' in result.output

    def test_write_to_file(self, runner, ctx):
        runner.invoke(add, ['Task 3'], obj=ctx)
        with open('./todo.txt', 'r') as f:
            lines = f.readlines()
            assert '3