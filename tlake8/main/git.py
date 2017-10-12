from flake8.main.git import config_for, hook as flake8_git_hook


def hook(*args, **kwargs):
    from tlake8.monkey import patch_flake8

    patch_flake8()
    return flake8_git_hook(*args, **kwargs)


_HOOK_TEMPLATE = """#!{executable}
import sys

from tlake8.main import git

if __name__ == '__main__':
    sys.exit(
        git.hook(
            strict=git.config_for('strict'),
            lazy=git.config_for('lazy'),
        )
    )
"""

__all__ = (
    'hook',
    'config_for',
    '_HOOK_TEMPLATE',
)
