#!/usr/bin/env bash


if [[ $1 = "init" ]]; then
    $(info [INIT PROJECT FOR DEV])
	pipenv --python 3.6
	pipenv install --dev

else
    pipenv run python -m builder "$@"
fi


