# -*- encoding: utf-8 -*-
# {{ cookiecutter.project_name }} v{{ cookiecutter.version }}
# {{ cookiecutter.project_short_description }}
# Copyright © {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
# See /LICENSE for licensing information.

"""
Main routine of {{ cookiecutter.project_name }}.

:Copyright: © {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
:License: BSD (see /LICENSE).
"""
from {{ cookiecutter.project_name }}.main import main


__all__ = ('main',)



if __name__ == '__main__':
    main()
