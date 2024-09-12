#!/usr/bin/env python3
from itertools import chain
import sys
import os
import csv

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

# Solution influenced by:
#   * https://stackoverflow.com/a/19438403
#   * https://docs.python.org/3/library/csv.html
#   * https://stackoverflow.com/a/13595210
#   * https://stackoverflow.com/a/3925147
#
# CSV formatting inspired by:
#   * https://partnerhelp.netflixstudios.com/hc/en-us/articles/215581437-Netflix-Accepted-Glyph-List

with TTFont(
    sys.argv[1], 0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1
) as ttf:
    chars = chain.from_iterable(
        [y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables
    )
    filename = 'SupportedCodePointsInFont__' + os.path.basename(sys.argv[1]) + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        supportedCodes = {}
        fieldnames = [
            'Unicode Code Point',
            'Character',
            'Name',
            'Description'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for c in chars:
            supportedCodes[c[0]] = (c[1], c[2])
        for code in sorted(supportedCodes):
            glyph = ('\\U' + format(code, '08X')).encode().decode('unicode-escape')
            desc = supportedCodes[code]
            writer.writerow({
                'Unicode Code Point': '0x' + format(code, '04X'),
                'Character': glyph,
                'Name': desc[0],
                'Description': desc[1]
            })
