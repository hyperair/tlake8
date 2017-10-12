from flake8.main.mercurial import (
    find_hgrc,
    configparser_for,
    hook as flake8_mercurial_hook,
    install as flake8_mercurial_install)


def hook(*args, **kwargs):
    from tlake8.monkey import patch_flake8
    patch_flake8()

    return flake8_mercurial_hook(*args, **kwargs)


def install():
    ret = flake8_mercurial_install()

    if not ret:
        return ret

    hgrc = find_hgrc(create_if_missing=True)
    hgconfig = configparser_for(hgrc)
    hgconfig.set('hooks', 'commit', 'python:tlake8.main.mercurial.hook')
    hgconfig.set('hooks', 'qrefresh', 'python:tlake8.main.mercurial.hook')

    with open(hgrc, 'w') as fd:
        hgconfig.write(fd)

    return True
