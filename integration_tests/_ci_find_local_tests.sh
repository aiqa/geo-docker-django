#!/usr/bin/env bash

# AIQA CI SCRIPTS
# https://aiqa.tech
#
# (c)2019 AIQA Technologies
#
# ver. 0.1.35

set -x

source _ci_vars.sh

find ${CI_SCENARIOS_DIR} -type f | grep -v "__pycache__" | grep -v "__init__" | sort -d > ${CI_SCENARIOS_LIST_FILENAME}

# vim:ts=4:sw=4:et:syn=sh: