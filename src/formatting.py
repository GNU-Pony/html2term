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
format_code       = lambda lines, **_attrs : format_(lines, '45', '`', 1, '`', 1)
format_kbd        = lambda lines, **_attrs : format_(lines, '33')
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
format_caption    = lambda lines, **_attrs : format_(lines, '01;33')
format_thead      = lambda lines, **_attrs : lines
format_tbody      = lambda lines, **_attrs : lines
format_tfoot      = lambda lines, **_attrs : lines
format_address    = lambda lines, **_attrs : format_(lines, '33', ' ' * 4, 4)
format_article    = lambda lines, **_attrs : lines
format_section    = lambda lines, **_attrs : lines
format_hr         = lambda lines, **_attrs : ['─' * 20, 20] + lines
format_br         = lambda lines, **_attrs : ['', 0] + lines

def format_a(lines, **attrs):
    if ('href' not in attrs) or ((len(lines) == 1) and (lines[0][0] == attrs['href'])):
        return lines
    if len(lines) == 0:
        return []
    (text, length) = lines[0]
    lines[0] = ('%s (%s)' % (attrs['href'], text), length + 3)
    return lines


FORMAT_MAP  = 'b strong em u s strike del ins i tt var code kbd rbi rbo time data figure iframe'
FORMAT_MAP += ' font basefont noscript span div html body footer header main nav figcaption mark'
FORMAT_MAP += ' q samp cite h1 h2 h3 h4 h5 h6 dd dt big small blockquote center small caption'
FORMAT_MAP += ' thead tbody tfoot address article section hr br a'
FORMAT_MAP = dict((f, globals()['format_' + f]) for f in FORMAT_MAP.split(' '))

