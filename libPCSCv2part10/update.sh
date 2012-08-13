#!/bin/sh

set -x
rm -rf libPCSCv2part10
make doxygen

rsync --recursive --verbose --update --rsh=ssh libPCSCv2part10 anonscm.debian.org:pcsclite_htdocs/
