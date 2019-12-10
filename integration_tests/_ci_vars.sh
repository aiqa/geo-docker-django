#!/usr/bin/env bash

# AIQA CI SCRIPTS
# https://aiqa.tech
#
# (c)2019 AIQA Technologies
#
# ver. 0.1.35


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


CI_DEFAULT_RUN=

# PARALLEL
CI_PARALLEL_LOG_FILENAME=__ci_parallel.log
CI_PARALLEL_NUMBER_OF_THREADS="-j 1"

# max: 2 failures
CI_PARALLEL_EXIT_STRATEGY="--halt soon,fail=2"

# max:3% failures
#CI_PARALLEL_EXIT_STRATEGY="--halt soon,fail=3%"


CI_SCENARIOS_LIST_FILENAME=__ci_scenarios_list.txt


CI_TEST_RUNNER_COMMAND="pytest {}"


CI_SCENARIOS_DIR="tc"
CI_SCENARIOS_FILEMASK=


CI_BACKEND_DIR="backend-python"

CI_CUSTOM_RELOAD=0
CI_CUSTOM_BUILD=0

if [ -f "_ci_vars_personal.sh" ]; then
    source _ci_vars_personal.sh
fi


# vim:ts=4:sw=4:et:syn=sh: