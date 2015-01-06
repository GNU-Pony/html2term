#!/usr/bin/env python3
'''
html2term – HTML to ANSI escape sequnce formatted text

Copyright © 2014, 2015  Mattias Andrée (maandree@member.fsf.org)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

CHARACTER_WIDTHS_0000_0FFF = (
    (0x0300, 0x036F, (0, 0)),
    (0x0483, 0x0489, (0, 0)),
    (0x058D, 0x058E, (1, 2)),
    (0x0591, 0x05BD, (0, 0)),
    (0x05BF, 0x05BF, (0, 0)),
    (0x05C1, 0x05C2, (0, 0)),
    (0x05C4, 0x05C5, (0, 0)),
    (0x05C7, 0x05C7, (0, 0)),
    (0x0610, 0x061A, (0, 0)),
    (0x064B, 0x065F, (0, 0)),
    (0x0670, 0x0670, (0, 0)),
    (0x06D6, 0x06DC, (0, 0)),
    (0x06DF, 0x06E4, (0, 0)),
    (0x06E7, 0x06E8, (0, 0)),
    (0x06EA, 0x06ED, (0, 0)),
    (0x0700, 0x070D, (1, 2)),
    (0x0710, 0x072F, (1, 2)),
    (0x0711, 0x0711, (0, 0)),
    (0x0730, 0x074A, (0, 0)),
    (0x074D, 0x074F, (1, 2)),
    (0x07A6, 0x07B0, (0, 0)),
    (0x07EB, 0x07F3, (0, 0)),
    (0x0800, 0x0815, (1, 2)),
    (0x0816, 0x0827, (0, 0)),
    (0x0829, 0x082D, (0, 0)),
    (0x0830, 0x033E, (1, 2)),
    (0x0840, 0x0858, (1, 2)),
    (0x085E, 0x085E, (1, 2)),
    (0x08E4, 0x08FF, (0, 0)),
    (0x0900, 0x0903, (0, 0)),
    (0x0904, 0x0939, (1, 2)),
    (0x093A, 0x093C, (0, 0)),
    (0x093D, 0x093D, (1, 2)),
    (0x093E, 0x094F, (0, 0)),
    (0x0950, 0x0950, (1, 2)),
    (0x0951, 0x0957, (0, 0)),
    (0x0958, 0x0961, (1, 2)),
    (0x0962, 0x0963, (0, 0)),
    (0x0964, 0x097F, (1, 2)),
    (0x0980, 0x0980, (1, 2)),
    (0x0981, 0x0983, (0, 0)),
    (0x0985, 0x09B9, (1, 2)),
    (0x09BC, 0x09BC, (0, 0)),
    (0x09BD, 0x09BD, (1, 2)),
    (0x09BE, 0x09CD, (0, 0)),
    (0x09CE, 0x09CE, (1, 2)),
    (0x09D7, 0x09D7, (0, 0)),
    (0x09DC, 0x09E1, (1, 2)),
    (0x09E2, 0x09E3, (0, 0)),
    (0x09E6, 0x09FB, (1, 2)),
    (0x0A01, 0x0A03, (0, 0)),
    (0x0A05, 0x0A39, (1, 2)),
    (0x0A3C, 0x0A3C, (0, 0)),
    (0x0A3E, 0x0A42, (0, 0)),
    (0x0A47, 0x0A48, (0, 0)),
    (0x0A4B, 0x0A4D, (0, 0)),
    (0x0A51, 0x0A51, (0, 0)),
    (0x0A59, 0x0A6F, (1, 2)),
    (0x0A70, 0x0A71, (0, 0)),
    (0x0A72, 0x0A74, (1, 2)),
    (0x0A75, 0x0A75, (0, 0)),
    (0x0A81, 0x0A83, (0, 0)),
    (0x0A85, 0x0AB9, (1, 2)),
    (0x0ABC, 0x0ABC, (0, 0)),
    (0x0ABD, 0x0ABD, (1, 2)),
    (0x0ABE, 0x0ACD, (0, 0)),
    (0x0AD0, 0x0AE1, (1, 2)),
    (0x0AE2, 0x0AE3, (0, 0)),
    (0x0AE6, 0x0AF1, (1, 2)),
    (0x0B05, 0x0B39, (1, 2)),
    (0x0B3C, 0x0B3C, (0, 0)),
    (0x0B3D, 0x0B3D, (1, 2)),
    (0x0B3E, 0x0B57, (0, 0)),
    (0x0B5C, 0x0B61, (1, 2)),
    (0x0B62, 0x0B63, (0, 0)),
    (0x0B66, 0x0B77, (1, 2)),
    (0x0B82, 0x0B82, (0, 0)),
    (0x0B83, 0x0BB9, (1, 2)),
    (0x0BBE, 0x0BCD, (0, 0)),
    (0x0BD0, 0x0BD0, (1, 2)),
    (0x0BD7, 0x0BD7, (0, 0)),
    (0x0BE6, 0x0BFA, (1, 2)),
    (0x0C00, 0x0C03, (0, 0)),
    (0x0C05, 0x0C3D, (1, 2)),
    (0x0C3E, 0x0C56, (0, 0)),
    (0x0C58, 0x0C61, (1, 2)),
    (0x0C62, 0x0C63, (0, 0)),
    (0x0C66, 0x0C7F, (1, 2)),
    (0x0C81, 0x0C83, (0, 0)),
    (0x0C85, 0x0CB9, (1, 2)),
    (0x0CBC, 0x0CBC, (0, 0)),
    (0x0CBD, 0x0CBD, (1, 2)),
    (0x0CBE, 0x0CD6, (0, 0)),
    (0x0CDE, 0x0CE1, (1, 2)),
    (0x0CE2, 0x0CE3, (0, 0)),
    (0x0CE6, 0x0CF2, (1, 2)),
    (0x0D01, 0x0D03, (0, 0)),
    (0x0D05, 0x0D3D, (1, 2)),
    (0x0D3E, 0x0D57, (0, 0)),
    (0x0D60, 0x0D61, (1, 2)),
    (0x0D62, 0x0D63, (0, 0)),
    (0x0D66, 0x0D7F, (1, 2)),
    (0x0D82, 0x0D83, (0, 0)),
    (0x0D85, 0x0DC6, (1, 2)),
    (0x0DCA, 0x0DDF, (0, 0)),
    (0x0DE6, 0x0DEF, (1, 2)),
    (0x0DF2, 0x0DF3, (0, 0)),
    (0x0DF4, 0x0DF4, (1, 2)),
    (0x0E01, 0x0E30, (1, 2)),
    (0x0E31, 0x0E31, (0, 0)),
    (0x0E32, 0x0E33, (1, 2)),
    (0x0E34, 0x0E3A, (0, 0)),
    (0x0E3F, 0x0E46, (1, 2)),
    (0x0E47, 0x0E4E, (0, 0)),
    (0x0E4F, 0x0E5B, (1, 2)),
    (0x0E81, 0x0EB0, (1, 2)),
    (0x0EB1, 0x0EB1, (0, 0)),
    (0x0EB2, 0x0EB3, (1, 2)),
    (0x0EB4, 0x0EBC, (0, 0)),
    (0x0EBD, 0x0EC6, (1, 2)),
    (0x0EC8, 0x0ECD, (0, 0)),
    (0x0ED0, 0x0EDF, (1, 2)),
    (0x0F02, 0x0F03, (1, 2)),
    (0x0F16, 0x0F17, (1, 2)),
    (0x0F18, 0x0F19, (0, 0)),
    (0x0F35, 0x0F35, (0, 0)),
    (0x0F37, 0x0F37, (0, 0)),
    (0x0F39, 0x0F39, (0, 0)),
    (0x0F3A, 0x0F3B, (1, 2)),
    (0x0F3E, 0x0F3F, (0, 0)),
    (0x0F71, 0x0F84, (0, 0)),
    (0x0F86, 0x0F87, (0, 0)),
    (0x0F8D, 0x0FBC, (0, 0)),
    (0x0FC5, 0x0FC5, (1, 2)),
    (0x0FC6, 0x0FC6, (0, 0)),
    (0x0FC7, 0x0FD0, (1, 2)),
    (0x0FD2, 0x0FDA, (1, 2)),
)
'''
:tuple<(first:int, last:int, (print:int, display:int))>  Measurement of all abnormal characters in the range
                                                         [U+0000, U+0FFF]. Each element in the list is a
                                                         subrange of characters with measurements. The subrange
                                                         is [`first`, `range`]; all assigned characters in this
                                                         range are believed the be `print` columns width by
                                                         the terminal but is printed in `display` columns.
                                                         `display` cannot be lesser than `print`.
'''

CHARACTER_WIDTHS_1000_1FFF = (
    (0x1000, 0x102A, (1, 2)),
    (0x102B, 0x103E, (0, 0)),
    (0x103F, 0x1055, (1, 2)),
    (0x1056, 0x1059, (0, 0)),
    (0x105A, 0x105D, (1, 2)),
    (0x105E, 0x1060, (0, 0)),
    (0x1061, 0x1061, (1, 2)),
    (0x1062, 0x1064, (0, 0)),
    (0x1065, 0x1066, (1, 2)),
    (0x1067, 0x106D, (0, 0)),
    (0x106E, 0x1070, (1, 2)),
    (0x1071, 0x1074, (0, 0)),
    (0x1075, 0x1081, (1, 2)),
    (0x1082, 0x108D, (0, 0)),
    (0x108E, 0x108E, (1, 2)),
    (0x108F, 0x108F, (0, 0)),
    (0x1090, 0x1099, (1, 2)),
    (0x109A, 0x109D, (0, 0)),
    (0x109E, 0x109F, (1, 2)),
    (0x1100, 0x11FF, (2, 2)),
    (0x1200, 0x135A, (1, 2)),
    (0x135D, 0x135F, (0, 0)),
    (0x1360, 0x1360, (1, 2)),
    (0x1363, 0x1365, (1, 2)),
    (0x1368, 0x1368, (1, 2)),
    (0x1380, 0x138F, (1, 2)),
    (0x1395, 0x1395, (1, 2)),
    (0x1397, 0x1398, (1, 2)),
    (0x158E, 0x1594, (1, 2)),
    (0x15E1, 0x15E1, (1, 2)),
    (0x1642, 0x1645, (1, 2)),
    (0x164A, 0x166C, (1, 2)),
    (0x166F, 0x166F, (1, 2)),
    (0x1670, 0x1676, (1, 3)),
    (0x16A1, 0x16A1, (1, 2)),
    (0x1700, 0x1711, (1, 2)),
    (0x1712, 0x1714, (0, 0)),
    (0x1720, 0x1731, (1, 2)),
    (0x1732, 0x1734, (0, 0)),
    (0x1735, 0x1751, (1, 2)),
    (0x1752, 0x1753, (0, 0)),
    (0x1760, 0x1761, (1, 2)),
    (0x1763, 0x1770, (1, 2)),
    (0x1772, 0x1773, (0, 0)),
    (0x1780, 0x17B3, (1, 2)),
    (0x17B4, 0x17D3, (0, 0)),
    (0x17D4, 0x17D5, (1, 2)),
    (0x17D7, 0x17DB, (1, 2)),
    (0x17DD, 0x17DD, (0, 0)),
    (0x17E0, 0x17E9, (1, 2)),
    (0x1800, 0x180A, (1, 2)),
    (0x180B, 0x180E, (0, 0)),
    (0x1810, 0x18A8, (1, 2)),
    (0x18A9, 0x18A9, (0, 0)),
    (0x18AA, 0x18AA, (1, 2)),
    (0x18F2, 0x18F2, (1, 2)),
    (0x1900, 0x191E, (1, 2)),
    (0x1920, 0x193B, (0, 0)),
    (0x1945, 0x194F, (1, 2)),
    (0x1980, 0x19AB, (1, 2)),
    (0x19B0, 0x19C0, (0, 0)),
    (0x19C1, 0x19C7, (1, 2)),
    (0x19C8, 0x19C9, (0, 0)),
    (0x19D0, 0x1A16, (1, 2)),
    (0x1A17, 0x1A1B, (0, 0)),
    (0x1A1E, 0x1A54, (1, 2)),
    (0x1A55, 0x1A7F, (0, 0)),
    (0x1A80, 0x1AAD, (1, 2)),
    (0x1AB0, 0x1B04, (0, 0)),
    (0x1B05, 0x1B33, (1, 2)),
    (0x1B34, 0x1B44, (0, 0)),
    (0x1B45, 0x1B6A, (1, 2)),
    (0x1B6B, 0x1B73, (0, 0)),
    (0x1B80, 0x1B82, (0, 0)),
    (0x1B83, 0x1BA0, (1, 2)),
    (0x1BA1, 0x1BAD, (0, 0)),
    (0x1BAE, 0x1BE5, (1, 2)),
    (0x1BE6, 0x1BF3, (0, 0)),
    (0x1BFC, 0x1C23, (1, 2)),
    (0x1C24, 0x1C37, (0, 0)),
    (0x1C3B, 0x1C4F, (1, 2)),
    (0x1CC0, 0x1CC7, (1, 2)),
    (0x1CD2, 0x1CE8, (0, 0)),
    (0x1CD3, 0x1CD3, (1, 2)),
    (0x1CD4, 0x1CE8, (0, 0)),
    (0x1CE9, 0x1CEC, (1, 2)),
    (0x1CED, 0x1CED, (0, 0)),
    (0x1CEE, 0x1CF1, (1, 2)),
    (0x1CF2, 0x1CF4, (0, 0)),
    (0x1CF5, 0x1CF6, (1, 2)),
    (0x1CF8, 0x1CF9, (0, 0)),
    (0x1DC0, 0x1DFF, (0, 0)),
)
'''
:tuple<(first:int, last:int, (print:int, display:int))>  Measurement of all abnormal characters in the range
                                                         [U+1000, U+1FFF]. Each element in the list is a
                                                         subrange of characters with measurements. The subrange
                                                         is [`first`, `range`]; all assigned characters in this
                                                         range are believed the be `print` columns width by
                                                         the terminal but is printed in `display` columns.
                                                         `display` cannot be lesser than `print`.
'''

CHARACTER_WIDTHS_2000_FFFF = (
    (0x200B, 0x200F, (0, 0)),
    (0x2028, 0x202F, (0, 0)),
    (0x2060, 0x206F, (0, 0)),
    (0x20D0, 0x20F0, (0, 0)),
    (0x2189, 0x2189, (1, 2)),
    (0x2329, 0x232A, (1, 2)),
    (0x23E9, 0x23FA, (1, 2)),
    (0x269E, 0x269F, (1, 2)),
    (0x26BD, 0x26BF, (1, 2)),
    (0x26C4, 0x26FF, (1, 2)),
    (0x2700, 0x2700, (1, 2)),
    (0x270A, 0x270B, (1, 2)),
    (0x274C, 0x274C, (1, 2)),
    (0x274E, 0x274E, (1, 2)),
    (0x2753, 0x2755, (1, 2)),
    (0x2757, 0x2757, (1, 2)),
    (0x275F, 0x2760, (1, 2)),
    (0x2795, 0x2797, (1, 2)),
    (0x27BF, 0x27BF, (1, 2)),
    (0x27CB, 0x27CB, (1, 2)),
    (0x27CD, 0x27CF, (1, 2)),
    (0x2B4D, 0x2B4D, (1, 2)),
    (0x2B50, 0x2BD1, (1, 2)),
    (0x2C0F, 0x2C0F, (1, 2)),
    (0x2C1F, 0x2C1F, (1, 2)),
    (0x2C27, 0x2C29, (1, 2)),
    (0x2C3F, 0x2C3F, (1, 2)),
    (0x2C4F, 0x2C4F, (1, 2)),
    (0x2C57, 0x2C59, (1, 2)),
    (0x2CCE, 0x2CCF, (1, 2)),
    (0x2CE7, 0x2CE7, (1, 2)),
    (0x2CEA, 0x2CEE, (1, 2)),
    (0x2CEF, 0x2CF1, (0, 0)),
    (0x2D00, 0x2D25, (1, 2)),
    (0x2D30, 0x2D41, (1, 2)),
    (0x2D43, 0x2D4E, (1, 2)),
    (0x2D50, 0x2D50, (1, 2)),
    (0x2D52, 0x2D56, (1, 2)),
    (0x2D58, 0x2D63, (1, 2)),
    (0x2D65, 0x2D65, (1, 2)),
    (0x2D7F, 0x2D7F, (0, 0)),
    (0x2D80, 0x2DDF, (1, 2)),
    (0x2DE0, 0x2DFF, (0, 0)),
    (0x2E0E, 0x2E11, (1, 2)),
    (0x2E13, 0x2E15, (1, 2)),
    (0x2E1E, 0x2E1F, (1, 2)),
    (0x2E2A, 0x2E2D, (1, 2)),
    (0x2E80, 0x3029, (2, 2)),
    (0x302A, 0x302F, (0, 0)),
    (0x3030, 0x303E, (2, 2)),
    (0x3041, 0x3096, (2, 2)),
    (0x3099, 0x309A, (0, 0)),
    (0x309B, 0xA4CF, (2, 2)),
    (0xA4D0, 0xA4F7, (1, 2)),
    (0xA500, 0xA62B, (1, 2)),
    (0xA644, 0xA644, (1, 2)),
    (0xA64C, 0xA64D, (1, 2)),
    (0xA650, 0xA651, (1, 2)),
    (0xA654, 0xA657, (1, 2)),
    (0xA65E, 0xA65E, (1, 2)),
    (0xA660, 0xA668, (1, 2)),
    (0xA66A, 0xA66E, (1, 2)),
    (0xA66F, 0xA672, (0, 0)),
    (0xA674, 0xA67D, (0, 0)),
    (0xA68A, 0xA68B, (1, 2)),
    (0xA692, 0xA694, (1, 2)),
    (0xA698, 0xA699, (1, 2)),
    (0xA69F, 0xA69F, (0, 0)),
    (0xA6F0, 0xA6F1, (0, 0)),
    (0xA726, 0xA728, (1, 2)),
    (0xA732, 0xA73D, (1, 2)),
    (0xA74A, 0xA74A, (1, 2)),
    (0xA74C, 0xA74C, (1, 2)),
    (0xA74E, 0xA74F, (1, 2)),
    (0xA754, 0xA754, (1, 2)),
    (0xA756, 0xA756, (1, 2)),
    (0xA758, 0xA758, (1, 2)),
    (0xA760, 0xA760, (1, 2)),
    (0xA773, 0xA774, (1, 2)),
    (0xA7FA, 0xA7FA, (1, 2)),
    (0xA7FD, 0xA7FD, (1, 2)),
    (0xA7FF, 0xA7FF, (1, 2)),
    (0xA800, 0xA801, (1, 2)),
    (0xA802, 0xA802, (0, 0)),
    (0xA803, 0xA805, (1, 2)),
    (0xA806, 0xA806, (0, 0)),
    (0xA807, 0xA80A, (1, 2)),
    (0xA80B, 0xA80B, (0, 0)),
    (0xA80C, 0xA822, (1, 2)),
    (0xA823, 0xA827, (0, 0)),
    (0xA828, 0xA82B, (1, 2)),
    (0xA830, 0xA839, (1, 2)),
    (0xA840, 0xA877, (1, 2)),
    (0xA880, 0xA881, (0, 0)),
    (0xA882, 0xA8B3, (1, 2)),
    (0xA8B4, 0xA8C4, (0, 0)),
    (0xA8CE, 0xA8D9, (1, 2)),
    (0xA8E0, 0xA8F1, (0, 0)),
    (0xA8F2, 0xA8FB, (1, 2)),
    (0xA900, 0xA925, (1, 2)),
    (0xA926, 0xA92D, (0, 0)),
    (0xA92E, 0xA946, (1, 2)),
    (0xA947, 0xA953, (0, 0)),
    (0xA95F, 0xA97C, (1, 2)),
    (0xA980, 0xA983, (0, 0)),
    (0xA984, 0xA9B2, (1, 2)),
    (0xA9B3, 0xA9C0, (0, 0)),
    (0xA9C1, 0xA9DF, (1, 2)),
    (0xA9E1, 0xA9E4, (1, 2)),
    (0xA9E5, 0xA9E5, (0, 0)),
    (0xA9E8, 0xA9EE, (1, 2)),
    (0xA9F9, 0xA9FC, (1, 2)),
    (0xA9FE, 0xA9FE, (1, 2)),
    (0xAA00, 0xAA28, (1, 2)),
    (0xAA29, 0xAA36, (0, 0)),
    (0xAA40, 0xAA42, (1, 2)),
    (0xAA43, 0xAA43, (0, 0)),
    (0xAA44, 0xAA4B, (1, 2)),
    (0xAA4C, 0xAA4D, (0, 0)),
    (0xAA50, 0xAA7A, (1, 2)),
    (0xAA7B, 0xAA7D, (0, 0)),
    (0xAA7E, 0xAAAF, (1, 2)),
    (0xAAB0, 0xAAB0, (0, 0)),
    (0xAAB1, 0xAAB1, (1, 2)),
    (0xAAB2, 0xAAB4, (0, 0)),
    (0xAAB5, 0xAAB6, (1, 2)),
    (0xAAB7, 0xAAB8, (0, 0)),
    (0xAAB9, 0xAABD, (1, 2)),
    (0xAABE, 0xAABF, (0, 0)),
    (0xAAC0, 0xAAC0, (1, 2)),
    (0xAAC1, 0xAAC1, (0, 0)),
    (0xAAC2, 0xAAC2, (1, 2)),
    (0xAADB, 0xAAEA, (1, 2)),
    (0xAAEB, 0xAAEF, (0, 0)),
    (0xAAF0, 0xAAF4, (1, 2)),
    (0xAAF5, 0xAAF6, (0, 0)),
    (0xAB00, 0xAB2F, (1, 2)),
    (0xABC0, 0xABE2, (1, 2)),
    (0xABE3, 0xABEA, (0, 0)),
    (0xABEB, 0xABEB, (1, 2)),
    (0xABEC, 0xABED, (0, 0)),
    (0xABF0, 0xABF9, (1, 2)),
    (0xAC00, 0xD7AF, (2, 2)),
    (0xD7B0, 0xD7FF, (1, 2)),
    (0xF900, 0xFAFF, (2, 2)),
    (0xFB1E, 0xFB1E, (0, 0)),
    (0xFCAD, 0xFCAF, (1, 2)),
    (0xFCB1, 0xFCB7, (1, 2)),
    (0xFCE7, 0xFCEA, (1, 2)),
    (0xFCFB, 0xFCFE, (1, 2)),
    (0xFD17, 0xFD1A, (1, 2)),
    (0xFD2D, 0xFD32, (1, 2)),
    (0xFD34, 0xFD39, (1, 2)),
    (0xFD50, 0xFDFD, (1, 2)),
    (0xFE00, 0xFE0F, (0, 0)),
    (0xFE10, 0xFE1F, (1, 2)),
    (0xFE20, 0xFE2F, (0, 0)),
    (0xFE30, 0xFE4F, (1, 2)),
    (0xFE50, 0xFE6F, (2, 2)),
    (0xFEFF, 0xFEFF, (0, 0)),
    (0xFF00, 0xFF60, (2, 2)),
    (0xFFE0, 0xFFE6, (2, 2)),
    (0xFFF9, 0xFFFB, (0, 0)),
)
'''
:tuple<(first:int, last:int, (print:int, display:int))>  Measurement of all abnormal characters in the range
                                                         [U+2000, U+FFFF]. Each element in the list is a
                                                         subrange of characters with measurements. The subrange
                                                         is [`first`, `range`]; all assigned characters in this
                                                         range are believed the be `print` columns width by
                                                         the terminal but is printed in `display` columns.
                                                         `display` cannot be lesser than `print`.
'''

CHARACTER_WIDTHS_10000_10FFFF = (
    (0x10080, 0x100FF, (1, 2)),
    (0x102E0, 0x102E0, (0, 0)),
    (0x102E1, 0x102FF, (1, 2)),
    (0x10308, 0x10308, (1, 2)),
    (0x1030C, 0x1030C, (1, 3)),
    (0x1030D, 0x10311, (1, 2)),
    (0x10319, 0x10319, (1, 2)),
    (0x10376, 0x1037A, (0, 0)),
    (0x10A01, 0x10A0F, (0, 0)),
    (0x10A38, 0x10A3F, (0, 0)),
    (0x10AE5, 0x10AE6, (0, 0)),
    (0x11000, 0x11002, (0, 0)),
    (0x11038, 0x11046, (0, 0)),
    (0x1107F, 0x11082, (0, 0)),
    (0x110B0, 0x110BA, (0, 0)),
    (0x11100, 0x11102, (0, 0)),
    (0x11127, 0x11134, (0, 0)),
    (0x11173, 0x11173, (0, 0)),
    (0x11180, 0x11182, (0, 0)),
    (0x111B3, 0x111C0, (0, 0)),
    (0x111E0, 0x111FF, (1, 2)),
    (0x1122C, 0x11237, (0, 0)),
    (0x112DF, 0x112EA, (0, 0)),
    (0x11301, 0x11303, (0, 0)),
    (0x1133C, 0x1133C, (0, 0)),
    (0x1133E, 0x11357, (0, 0)),
    (0x11362, 0x11374, (0, 0)),
    (0x114B0, 0x114C3, (0, 0)),
    (0x115AF, 0x115C0, (0, 0)),
    (0x11630, 0x11640, (0, 0)),
    (0x116AB, 0x116B7, (0, 0)),
    (0x16AF0, 0x16AF4, (0, 0)),
    (0x16B30, 0x16B36, (0, 0)),
    (0x16F51, 0x16F92, (0, 0)),
    (0x1BC9D, 0x1BC9D, (0, 0)),
    (0x1BCA0, 0x1BCAF, (0, 0)),
    (0x1D159, 0x1D159, (0, 0)),
    (0x1D165, 0x1D169, (0, 0)),
    (0x1D16D, 0x1D182, (0, 0)),
    (0x1D185, 0x1D18B, (0, 0)),
    (0x1D1AA, 0x1D1AD, (0, 0)),
    (0x1D242, 0x1D244, (0, 0)),
    (0x1D300, 0x1D35F, (1, 2)),
    (0x1D400, 0x1D7F5, (1, 2)),
    (0x1F030, 0x1F061, (1, 2)),
    (0x1F0A0, 0x1F0FF, (1, 2)),
    (0x1F600, 0x1F64F, (1, 2)),
    (0x20000, 0xDFFFF, (2, 2)),
    (0xE0001, 0xE0001, (0, 0)),
    (0xE0020, 0xE007F, (0, 0)),
    (0xE0100, 0xE01EF, (0, 0)),
)
'''
:tuple<(first:int, last:int, (print:int, display:int))>  Measurement of all abnormal characters in the range
                                                         [U+10000, U+10FFFF]. Each element in the list is a
                                                         subrange of characters with measurements. The subrange
                                                         is [`first`, `range`]; all assigned characters in this
                                                         range are believed the be `print` columns width by
                                                         the terminal but is printed in `display` columns.
                                                         `display` cannot be lesser than `print`.
'''


def measure_character(character):
    '''
    Get the widths of a character
    
    @param   character:chr              The character
    @return  :(print:int, display:int)  The widths of the character, arbitrary measurements if the character
                                        is not assigned. The character is believed `print` columns width by
                                        the terminal but is printed in `display` columns. `display` cannot be
                                        lesser than `print`.
    '''
    c = ord(character)
    if   0x0000 <= c <= 0x0FFF:  measurements = CHARACTER_WIDTHS_0000_0FFF
    elif 0x1000 <= c <= 0x1FFF:  measurements = CHARACTER_WIDTHS_1000_1FFF
    elif 0x2000 <= c <= 0xFFFF:  measurements = CHARACTER_WIDTHS_2000_FFFF
    else:                        measurements = CHARACTER_WIDTHS_10000_10FFFF
    for first, last, r in measurements:
        if first > c:
            return 1, 1
        if last >= c:
            return r
    return 1, 1


def measure_string(string):
    '''
    Measure a string a construct a string that can be printed without overlapping characters
    
    @param   string:str     The string
    @return  :(:str, :int)  The printable string, and the column-width of the string
    '''
    rc_str, rc_len = '', 0
    for c in string:
        a, b = measure_character(c)
        rc_str += c + ' ' * (b - a)
        rc_len += b
    return rc_str, rc_len


def concatenate(left, right):
    if len(left) == 0:  return right
    if len(right) == 0:  return left
    return left[:-1] + [tuple(left[-1][i] + right[0][i] for i in range(2))] + right[1:]

def format_(lines, fmt, prestr = '', prelen = 0, sufstr = '', suflen = 0):
    def replace_(text):
        text = text.replace('\033[00m', '\033[00;%sm' % fmt)
        text = text.replace('\033[00;', '\033[00;%s;' % fmt)
        return text
    if fmt is not None:
        f = lambda text : '%s\033[%sm%s\033[00m%s' % (prestr, fmt, replace_(text), sufstr)
    else:
        f = lambda text : prestr + text + sufstr
    return [(f(text), prelen + length + suflen) for text, length in lines]

format_b          = lambda lines, **_attrs : format_(lines, '01')
format_strong     = lambda lines, **_attrs : format_(lines, '01;31')
format_em         = lambda lines, **_attrs : format_(lines, '01;04')
format_u          = lambda lines, **_attrs : format_(lines, '04')
format_s          = lambda lines, **_attrs : format_(lines, '41')
format_strike     = lambda lines, **_attrs : format_(lines, '41')
format_del        = lambda lines, **_attrs : format_(lines, '31')
format_ins        = lambda lines, **_attrs : format_(lines, '32')
format_i          = lambda lines, **_attrs : format_(lines, '34')
format_tt         = lambda lines, **_attrs : format_(lines, '35')
format_var        = lambda lines, **_attrs : format_(lines, '04;34')
format_code       = lambda lines, **_attrs : format_(lines, '35', '`', 1, '`', 1)
format_kbd        = lambda lines, **_attrs : format_(lines, '35')
format_rbi        = lambda lines, **_attrs : lines
format_rbo        = lambda lines, **_attrs : lines
format_time       = lambda lines, **_attrs : lines
format_data       = lambda lines, **_attrs : lines
format_figure     = lambda lines, **_attrs : lines
format_iframe     = lambda lines, **_attrs : lines
format_font       = lambda lines, **_attrs : lines
format_basefont   = lambda lines, **_attrs : lines
format_noscript   = lambda lines, **_attrs : lines
format_span       = lambda lines, **_attrs : lines
format_div        = lambda lines, **_attrs : lines
format_html       = lambda lines, **_attrs : lines
format_body       = lambda lines, **_attrs : lines
format_footer     = lambda lines, **_attrs : lines
format_header     = lambda lines, **_attrs : lines
format_main       = lambda lines, **_attrs : lines
format_nav        = lambda lines, **_attrs : lines
format_figcaption = lambda lines, **_attrs : format_(lines, None, ' ' * 2, 2)
format_mark       = lambda lines, **_attrs : format_(lines, '43')
format_q          = lambda lines, **_attrs : format_(lines, None, '“', 1, '”', 1)
format_samp       = lambda lines, **_attrs : format_(lines, None, '‘', 1, '’', 1)
format_cite       = lambda lines, **_attrs : format_(lines, None, '‘', 1, '’', 1)
format_h1         = lambda lines, **_attrs : format_(lines, '01;44')
format_h2         = lambda lines, **_attrs : format_(lines, '44', ' ' * 2, 2)
format_h3         = lambda lines, **_attrs : format_(lines, '44', ' ' * 4, 4)
format_h4         = lambda lines, **_attrs : format_(lines, '44', ' ' * 6, 6)
format_h5         = lambda lines, **_attrs : format_(lines, '44', ' ' * 8, 8)
format_h6         = lambda lines, **_attrs : format_(lines, '44', ' ' * 10, 10)
format_dd         = lambda lines, **_attrs : lines
format_dt         = lambda lines, **_attrs : format_(lines, '01')
format_big        = lambda lines, **_attrs : format_(lines, '42')
format_small      = lambda lines, **_attrs : format_(lines, '36')
format_blockquote = lambda lines, **_attrs : format_(lines, None, '\033[01;31m│\033[00m', 3)
format_center     = lambda lines, **_attrs : format_(lines, None, ' ' * 20, 20)
format_small      = lambda lines, **_attrs : format_(lines, '47;30')
format_small      = lambda lines, **_attrs : format_(lines, '01;33')
format_thead      = lambda lines, **_attrs : lines
format_tbody      = lambda lines, **_attrs : lines
format_tfoot      = lambda lines, **_attrs : lines
format_address    = lambda lines, **_attrs : format_(lines, '33', ' ' * 4, 4)
format_article    = lambda lines, **_attrs : lines
format_section    = lambda lines, **_attrs : lines

def format_a(lines, **attrs):
    if ('href' not in attrs) or ((len(lines) == 1) and (lines[0][0] == attrs['href'])):
        return lines
    if len(lines) == 0:
        return 0
    (text, length) = lines[0]
    lines[0] = ('%s (%s)' % (attrs['href'], text), length + 3)
    return lines

def format_hr(lines, **_attrs):
    return ['─' * 20, 20] + lines

def format_br(lines, **_attrs):
    return ['', 0] + lines


def print_lines(lines):
    for text, _length in lines:
        print(text)

_ = lambda s : [measure_string(s)]
print_lines(format_h2(format_code(concatenate(format_b(_('hello')), _(' world')))))


#  <head>
#    <title>
#    <base>
#  <p>
#  <pre width="wrapping column">  line breaks are included verbatim, tabs is 8
#  <xmp> = <listing> = <pre>
#  <ul type="0"/"1"/"a"/"A"/"i"/"I"||"."/""/")"> <ol>
#    <li>
#  <dir>  columnated
#  <menu> = <ul type="1.">
#  <dl>  definition list
#  <table>
#     <th rowspan= colspan=> <td rowspan= colspan=> <tr>
#  <sub> <sup>
#  <dfn title=> <acronym title=> <abbr title="world wide web">www</abbr>
#  <video src=> <audio src=> <track src= label=> <img src= alt=>
#      <source src=>
#  <ruby>text<rt>small text above</rt><rtc>long small text beneath</rtc></ruby>
#  <ruby>top<rb>bottom</rb><rt>stack right of top</rt><rt>stack right of bottom</rt></ruby>
#      <rp>  only visible during inlining

