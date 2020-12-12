#!/bin/bash
export COMPOSE_PROJECT_NAME=url_shortener_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run url_shortener unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
