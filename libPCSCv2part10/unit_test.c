#include <stdio.h>
#include <string.h>

#include <winscard.h>

#include "PCSCv2part10.h"

#define ASSERT(x) do { if (!(x)) { printf("Fail at line %d\n", __LINE__); ok = 0; } } while(0)
int main(void)
{
	SCARDHANDLE hCard;
	int property;
	int value;
	int ret;
	int ok = 1;

	/* SCardControl fails */
	hCard = -1;
	property = 0;
	ret = PCSCv2Part10_find_TLV_property_by_tag_from_hcard(hCard, property,
		&value);
	ASSERT(-1 == ret);

	/* property NOT found */
	hCard = 0;
	property = 1234;
	ret = PCSCv2Part10_find_TLV_property_by_tag_from_hcard(hCard, property,
		&value);
	ASSERT(-1 == ret);

	/* property found */
	hCard = 0;
	property = PCSCv2_PART10_PROPERTY_wIdVendor;
	ret = PCSCv2Part10_find_TLV_property_by_tag_from_hcard(hCard, property,
		&value);
	ASSERT(0 == ret);
	ASSERT(0x08E6 == value);

	if (ok)
		printf("No error\n");
	return ! ok;
}

LONG SCardControl(SCARDHANDLE hCard, DWORD dwControlCode, LPCVOID
	pbSendBuffer, DWORD cbSendLength, LPVOID pbRecvBuffer, DWORD
	cbRecvLength, LPDWORD lpBytesReturned)
{
	unsigned char buffer_CM_IOCTL_GET_FEATURE_REQUEST[] = {
		FEATURE_GET_TLV_PROPERTIES, /* tag */
		0x04, /* length */
		0x42, 0x33, 0x00, 0x12 /* value */
	};
	unsigned char buffer_FEATURE_GET_TLV_PROPERTIES[] = {
		PCSCv2_PART10_PROPERTY_wLcdLayout, /* tag */
		0x02, /* length */
		0x00, 0x00,
		PCSCv2_PART10_PROPERTY_bTimeOut2,
		0x01,
		0x00,
		PCSCv2_PART10_PROPERTY_sFirmwareID,
		0x12, 0x47, 0x65, 0x6D, 0x54, 0x77, 0x69, 0x6E, 0x2D, 0x56,
		0x32, 0x2E, 0x30, 0x30, 0x2D, 0x47, 0x46, 0x30, 0x33,
		PCSCv2_PART10_PROPERTY_bPPDUSupport,
		0x01,
		0x00,
		PCSCv2_PART10_PROPERTY_wIdVendor,
		0x02,
		0xE6, 0x08,
		PCSCv2_PART10_PROPERTY_wIdProduct,
		0x02,
		0x37, 0x34,
		PCSCv2_PART10_PROPERTY_dwMaxAPDUDataSize,
		0x04,
		0x00, 0x00, 0x01, 0x00
	};

	(void)pbSendBuffer;
	(void)cbSendLength;

	if (hCard < 0)
		return SCARD_E_INVALID_HANDLE;

	if (cbRecvLength < sizeof buffer_FEATURE_GET_TLV_PROPERTIES)
		return SCARD_E_INSUFFICIENT_BUFFER;

	switch (dwControlCode)
	{
		case CM_IOCTL_GET_FEATURE_REQUEST:
			// printf("CM_IOCTL_GET_FEATURE_REQUEST\n");
			memcpy(pbRecvBuffer,
				buffer_CM_IOCTL_GET_FEATURE_REQUEST,
				sizeof buffer_CM_IOCTL_GET_FEATURE_REQUEST);
			*lpBytesReturned = sizeof buffer_CM_IOCTL_GET_FEATURE_REQUEST;
			break;

		case 0x42330012:
			// printf("FEATURE_GET_TLV_PROPERTIES\n");
			memcpy(pbRecvBuffer,
				buffer_FEATURE_GET_TLV_PROPERTIES,
				sizeof buffer_FEATURE_GET_TLV_PROPERTIES);
			*lpBytesReturned = sizeof buffer_FEATURE_GET_TLV_PROPERTIES;
			break;

		default:
			printf("Unknown dwControlCode: 0x%08lX\n", dwControlCode);
			return SCARD_E_INVALID_PARAMETER;
	}

	return SCARD_S_SUCCESS;
}
