# -*- encoding: utf-8 -*-
# {{ cookiecutter.project_name }} v{{ cookiecutter.version }}
# {{ cookiecutter.project_short_description }}
# Copyright {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
# See /LICENSE for licensing information.

"""
INSERT MODULE DESCRIPTION HERE.

:Copyright: {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
:License: GPLv3 (see /LICENSE).
"""

__all__ = ()

import sys
from {{ cookiecutter.project_name }}.cl_parser import parse_args



def main():
    """Main routine of {{ cookiecutter.project_name }}."""

    print("Hello World")
    args = parse_args(sys.argv[1:])
    cmd_params = vars(args)
    print(cmd_params)
