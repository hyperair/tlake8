import re

import flake8.main.git
import flake8.main.mercurial
import flake8.processor

import tlake8.main.git
import tlake8.main.mercurial


class tabfilteredfile(file):
    """
    `file` derivative class that replaces indentation tabs with 4 spaces to
    please flake8
    """
    indentation_regex = re.compile(r'^(\t+)')

    def readline(self, *args, **kwargs):
        line = super(tabfilteredfile, self).readline(*args, **kwargs)
        strtype = type(line)
        line = self.indentation_regex.sub(
            lambda idn: strtype(' ') * len(idn.group(1)), line)

        return line

    def readlines(self):
        def gen():
            while True:
                buf = self.readline()
                if not buf:
                    break
                yield buf
        return list(gen())


def filtering_open(*args, **kwargs):
    return tabfilteredfile(*args, **kwargs)


def patch_flake8():
    flake8.processor.open = filtering_open
    flake8.main.git._HOOK_TEMPLATE = tlake8.main.git._HOOK_TEMPLATE
    flake8.main.mercurial.hook = tlake8.main.mercurial.hook


def unpatch_flake8():
    flake8.processor.open = open
