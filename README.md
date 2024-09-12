A python script to dump out the supported Unicode code points from a font (font must be provided in `.ttf` format).

The solution was mainly influenced by the following links:
* https://stackoverflow.com/a/19438403
* https://docs.python.org/3/library/csv.html
* https://stackoverflow.com/a/13595210
* https://stackoverflow.com/a/3925147

The formatting of the CSV was inspired by the [Netflix Accepted Glyph List](https://partnerhelp.netflixstudios.com/hc/en-us/articles/215581437-Netflix-Accepted-Glyph-List),
though I chose to also add a column for the name of the character.

Makes use of the [fonttools](https://github.com/fonttools/fonttools/tree/main) library, which must be installed first:
```
pip install fonttools
```

The only argument for the script is the path to the `.ttf` file for the font, for example:
```
./dump-supported-code-points.py ~/Path/To/SuperFancyFont.ttf
```

The above should dump the output into a CSV named `SupportedCodePointsInFont__SuperFancyFont.ttf.csv`.
