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


th = td


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
                rc[r][c] = (('', 0), 1, 1)
    # Pad lines
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            cell = rc[r][c]
            if len(cell) == 3:
                (lines, rows, cols) = cell
                maxlen = max(length for _, length in lines)
                lines = [((text + ' ' * (maxlen - length)), maxlen) for text, length in lines]
                rc[r][c] = (lines, rows, cols)
    return table_to_text(rc)


def table_to_text(matrix):
    rn, cn = len(matrix), len(matrix[0])
    # Calculate widths
    h_ends = []
    for c in range(cn):
        maxend = 0 if len(h_ends) == 0 else h_ends[-1]
        h_ends.append(maxend)
        for r in range(rn):
            cell = (r, c)
            while len(cell) == 2:
                (r_, c_) = cell
                cell = matrix[r_][c_]
            (lines, _rows, cols) = cell
            if c_ + cols == c + 1:
                maxend = max(maxend, h_ends[c_] + lines[0][1])
        h_ends[c] = maxend + 1
    # Calculate heights
    v_ends = []
    for r in range(rn):
        maxend = 0 if len(v_ends) == 0 else v_ends[-1]
        v_ends.append(maxend)
        for c in range(cn):
            cell = (r, c)
            while len(cell) == 2:
                (r_, c_) = cell
                cell = matrix[r_][c_]
            (lines, rows, _cols) = cell
            if r_ + rows == r + 1:
                maxend = max(maxend, v_ends[r_] + len(lines))
        v_ends[r] = maxend + 1
    # Fix widths
    h_ends = [0] + h_ends
    for r in range(rn):
        for c in range(cn):
            cell = matrix[r][c]
            if len(cell) == 3:
                (lines, rows, cols) = cell
                end_col = c + cols
                newlen = h_ends[end_col] - h_ends[c]
                extra = newlen - lines[0][1] - 1
                lines = [((text + ' ' * extra + '│'), newlen) for text, _ in lines]
                matrix[r][c] = (lines, rows, cols)
    # Fix heights
    v_ends = [0] + v_ends
    for r in range(rn):
        for c in range(cn):
            cell = matrix[r][c]
            if len(cell) == 3:
                (lines, rows, cols) = cell
                end_row = r + rows
                newlen = v_ends[end_row] - v_ends[r]
                extra = newlen - len(lines)
                lines += [(' ' * (lines[0][1] - 1) + '│', lines[0][1])] * (extra - 1)
                lines += [('─' * (lines[0][1] - 1) + '┘', lines[0][1])]
                matrix[r][c] = (lines, rows, cols)
    # Make table
    for r in range(rn):
        for c in range(cn):
            cell = matrix[r][c]
            if len(cell) == 3:
                (lines, _rows, _cols) = cell
                for line, _ in lines:
                    print(line)
    return matrix


# ─│┌┐└┘├┤┬┴┼

