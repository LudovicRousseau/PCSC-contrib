/*
    sample.c: example of use of libPCSCv2part10 helper functions
    Copyright (C) 2012   Ludovic Rousseau

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include <stdio.h>

#ifdef __APPLE__
#include <PCSC/winscard.h>
#include <PCSC/wintypes.h>
#else
#include <winscard.h>
#endif


#include "PCSCv2part10.h"

/* PCSC error */
#define PCSC_ERROR_EXIT(rv) \
if (rv != SCARD_S_SUCCESS) \
{ \
	printf("Failed at line %d with %s (0x%lX)\n", __LINE__, pcsc_stringify_error(rv), rv); \
	goto end; \
}

int main(void)
{
	LONG rv;
	SCARDCONTEXT hContext;
	SCARDHANDLE hCard;
	int value, ret = -1;
	DWORD dwReaders, dwPref;
	char *mszReaders;

	rv = SCardEstablishContext(SCARD_SCOPE_SYSTEM, NULL, NULL, &hContext);
	PCSC_ERROR_EXIT(rv)

	dwReaders = SCARD_AUTOALLOCATE;
	rv = SCardListReaders(hContext, NULL, (LPSTR)&mszReaders, &dwReaders);
	PCSC_ERROR_EXIT(rv)

	/* use first reader */
	printf("Using reader: %s\n", mszReaders);

	rv = SCardConnect(hContext, mszReaders,
		SCARD_SHARE_DIRECT, SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1,
		&hCard, &dwPref);
	PCSC_ERROR_EXIT(rv)

	/* the interesting part is here */
	ret = PCSCv2Part10_find_TLV_property_by_tag_from_hcard(hCard,
		PCSCv2_PART10_PROPERTY_wIdVendor, &value);
	printf("ret: %d\n", ret);
	printf("value for PCSCv2_PART10_PROPERTY_wIdVendor: 0x%04X\n", value),

	rv = SCardDisconnect(hCard, SCARD_LEAVE_CARD);
	PCSC_ERROR_EXIT(rv)

	rv = SCardFreeMemory(hContext, mszReaders);
	PCSC_ERROR_EXIT(rv)

	rv = SCardReleaseContext(hContext);
	PCSC_ERROR_EXIT(rv)

end:
	return ret;
}
