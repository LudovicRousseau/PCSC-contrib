noinst_PROGRAMS = sample

sample_SOURCES = sample.c PCSCv2part10.c PCSCv2part10.h

sample_CFLAGS = $(PCSC_CFLAGS)
sample_LDADD = $(PCSC_LIBS)

doxygen:
	rm -rf libPCSCv2part10 ; doxygen doxygen.conf
