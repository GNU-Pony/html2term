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

def td(lines, **attrs):
    try:     rows = max(1, int(attrs['rowspan']))
    except:  rows = 1
    try:     cols = max(1, int(attrs['colspan']))
    except:  cols = 1
    return lines, rows, cols

def tr(cells, **_attrs):
    return cells

def table(rows, **_attrs):
    # Get table cells
    matrix = {}
    for r, cells in enumerate(rows):
        c = 0
        for lines, rows, cols in cells:
            while (r, c) in matrix:
                c += 1
            matrix[(r, c)] = (lines, rows, cols)
            for re in range(rows):
                for ce in range(cols):
                    if (r + re, c + ce) not in matrix:
                        matrix[(r + re, c + ce)] = (r, c)
            c += cols
    # Measure table
    max_r, max_c = 0, 0
    for r, c in matrix.keys():
        max_r = max(max_r, r)
        max_c = max(max_c, c)
    # Construct matrix
    rc = [[None] * (max_c + 1) for _ in range(max_r + 1)]
    for r, c in matrix.keys():
        rc[r][c] = matrix[(r, c)]
    # `None`-patch matrix
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            if rc[r][c] is None:
                if   c > 0:  rc[r][c] = rc[r][c - 1]
                elif r > 0:  rc[r][c] = rc[r - 1][c]
                else:        rc[r][c] = (('', 0), 1, 1)
    # Pad lines
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            cell = rc[r][c]
            if len(cell) == 3:
                (lines, _1, _2) = cell
                maxlen = max(length for _, length in lines)
                lines = [((text + ' ' * (maxlen - length)), maxlen) for text, length in lines]
                rc[r][c] = lines
    return table_to_text(rc)

def table_to_text(matrix):
    rn, cn = len(matrix), len(matrix[0])
    for r in range(rn):
        for c in range(cn):
            pass
    return matrix
    

th = td

# ─│┌┐└┘├┤┬┴┼

