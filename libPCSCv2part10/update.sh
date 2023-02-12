#!/bin/sh

set -x
rm -rf libPCSCv2part10
make doxygen

rsync --recursive --verbose --update --rsh=ssh libPCSCv2part10 muscle.apdu.fr:Serveurs_web/muscle.apdu.fr/
