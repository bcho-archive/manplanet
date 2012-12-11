#coding: utf-8

import re


def parse_relatives(buf, line_sep=None):
    pattern = re.compile('([\w\d_\-:]+)\(([\dn])\)')
    line_sep = line_sep or '\n'

    return pattern.findall(buf.strip())


def parse_content(buf, line_sep=None):
    re_section = re.compile('(^[A-Z][A-Z ]+[A-Z]$)')
    line_sep = line_sep or '\n'

    ret, prev, prev_keys = {}, '', None
    for line in buf.split(line_sep):
        m = re_section.findall(line)
        if m:
            if prev_keys:
                ret[prev_keys] = prev
            perv, prev_keys = '', m[0]
        else:
            prev += '\n' + line
    if prev_keys and prev:
        ret[prev_keys] = prev

    return ret


def parse(fname, abspath):
    re_name = re.compile('(.*)\.([\dn])\.*')

    if re_name.match(fname):
        name, section = re_name.findall(fname)[0]

        with open(abspath, 'r') as stream:
            buf = '\n'.join(stream.readlines()[1:-1])
            content = parse_content(buf)
            #: TODO not only grab from SEE ALSO
            see_also = content.get('SEE ALSO', None)
            relatives = parse_relatives(see_also) if see_also else None

        return (name, section, content, relatives)

    return None
