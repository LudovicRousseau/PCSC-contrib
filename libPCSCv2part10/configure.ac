# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])

AC_INIT([libPCSCv2part10],[0.1.0])
AC_CONFIG_SRCDIR(PCSCv2part10.c)
AC_CONFIG_AUX_DIR([.])
AM_INIT_AUTOMAKE(1.8 dist-bzip2 no-dist-gzip)
AC_CONFIG_HEADERS([config.h])

AC_CONFIG_MACRO_DIR(m4)

# silent build by default
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

# Automake boilerplate.
AC_CANONICAL_HOST

# Options
AM_MAINTAINER_MODE

# Checks for programs.
AC_PROG_CC
AM_PROG_CC_C_O
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_MAKE_SET
AC_PROG_LN_S
AM_PROG_AR
PKG_PROG_PKG_CONFIG

# check pcsc-lite version
PKG_CHECK_EXISTS([libpcsclite],
	[PKG_CHECK_MODULES(PCSC, libpcsclite, [],
	[
	if test -f /usr/local/lib/pkgconfig/libpcsclite.pc -a "x$PKG_CONFIG" != x ; then
		AC_MSG_ERROR([use PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./configure])
	  else
		AC_MSG_WARN([install pcsc-lite])
	  fi
	])],
	[AC_MSG_WARN([libpcsclite not found by pkg-config])]
)

saved_CPPFLAGS="$CPPFLAGS"
CPPFLAGS="$CPPFLAGS $PCSC_CFLAGS"
PCSC_ERROR_MSG="install pcsc-lite, or use ./configure PCSC_CFLAGS=..."
AC_CHECK_HEADERS(reader.h)
CPPFLAGS="$saved_CPPFLAGS"

# Write Makefiles.
AC_CONFIG_FILES(Makefile)

AC_OUTPUT

