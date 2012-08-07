#include <stdio.h>

#ifdef __APPLE__
#include <PCSC/winscard.h>
#include <PCSC/wintypes.h>
#else
#include <winscard.h>
#endif
#include <reader.h>


#include "PCSCv2part10.h"

int main(void)
{
	SCARDHANDLE hCard = 0;
	int value, ret;

	ret = PCSCv2Part10_find_TLV_property_by_tag_from_hcard(hCard, PCSCv2_PART10_PROPERTY_wIdVendor, &value);

	printf("This sample does nothing.\n");
	printf("It is just used to check compilation and link\n");

	return ret;
}
