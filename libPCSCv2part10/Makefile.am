noinst_PROGRAMS = sample unit_test

sample_SOURCES = sample.c PCSCv2part10.c PCSCv2part10.h

sample_CFLAGS = $(PCSC_CFLAGS)
sample_LDADD = $(PCSC_LIBS)

unit_test_SOURCES = unit_test.c PCSCv2part10.c PCSCv2part10.h

unit_test_CFLAGS = $(PCSC_CFLAGS)

doxygen:
	rm -rf libPCSCv2part10 ; doxygen doxygen.conf
