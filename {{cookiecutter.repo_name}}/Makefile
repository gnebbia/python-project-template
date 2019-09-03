.PHONY: default, lint

default:
	python -m {{ cookiecutter.repo_name }}
lint:
	pylint {{ cookiecutter.repo_name }}
pep8:
	autopep8 {{ cookiecutter.repo_name }} --in-place --recursive --aggressive --aggressive
