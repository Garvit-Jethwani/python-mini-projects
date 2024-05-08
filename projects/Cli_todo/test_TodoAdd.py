import pytest
import os
import click
from todo import add

class Test_TodoAdd:
    @pytest.mark.positive
    def test_add_valid_task(self, tmpdir):
        ctx = click.Context(add, obj={'TASKS': {}, 'LATEST': 0})
        tmpdir.chdir()
        add_task = 'Test Task'
        add(ctx, add_task)
        assert ctx.obj['TASKS'][0] == add_task
        assert ctx.obj['LATEST'] == 0
        with open('./todo.txt', 'r') as f:
            assert f.readline().strip() == '0'
            assert f.readline().strip() == '0