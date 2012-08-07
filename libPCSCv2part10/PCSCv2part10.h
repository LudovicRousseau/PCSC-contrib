/*
    PCSCv2part10.h: helper functions for PC/SC v2 part 10 services
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

/*
 * $Id$
 */

/**
 * @file
 */

/**
 * @brief Find an integer value by tag from TLV buffer
 *
 * @param buffer buffer received from FEATURE_GET_TLV_PROPERTIES
 * @param length buffer length
 * @param tag_searched tag searched
 * @param[out] value value found
 * @return Error code
 *
 * @retval 0 success
 * @retval -1 not found
 * @retval -2 invalid length in the TLV
 *
 */
int PCSCv2Part10_find_TLV_property_by_tag_from_buffer(
	unsigned char *buffer, int length, int tag_searched, int * value);

/**
 * @brief Find a integer value by tag from a PC/SC card handle
 *
 * @param hCard card handle as returned by SCardConnect()
 * @param tag_searched tag searched
 * @param[out] value value found
 * @return Error code (see PCSCv2Part10_find_TLV_property_by_tag_from_buffer())
 */
int PCSCv2Part10_find_TLV_property_by_tag_from_hcard(SCARDHANDLE hCard,
	int tag_searched, int * value);

