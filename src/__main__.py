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

from measurement import *
from formatting import *
from tables import *


def concatenate(left, right):
    if len(left) == 0:  return right
    if len(right) == 0:  return left
    return left[:-1] + [tuple(left[-1][i] + right[0][i] for i in range(2))] + right[1:]

def print_lines(lines):
    for text, _length in lines:
        print(text)

tr_1 = tr([th([measure_string('1')], colspan = 2, rowspan = 2),
           th([measure_string('2')], colspan = 2),
           th([measure_string('3')], rowspan = 2),
           th([measure_string('4')])])
tr_2 = tr([td([measure_string('5')], colspan = 2, rowspan = 2),
           td([measure_string('6')])])
tr_3 = tr([td([measure_string('7')]),
           td([measure_string('8')]),
           td([measure_string('9')], colspan = 2)])
t = table([tr_1, tr_2, tr_3])

print(t)

#  <head>
#    <title>
#    <base>
#  <p>
#  <pre width="wrapping column">  line breaks are included verbatim, tabs is 8
#  <xmp> = <listing> = <pre>
#  <ul type="0"/"1"/"a"/"A"/"i"/"I"||"."/""/")"> <ol> { <li> }
#  <dir>  columnated
#  <menu> = <ul type="1.">
#  <sub> <sup>
#  <ruby>text<rt>small text above</rt><rtc>long small text beneath</rtc></ruby>
#  <ruby>top<rb>bottom</rb><rt>stack right of top</rt><rt>stack right of bottom</rt></ruby>
#    <rp>  only visible during inlining

