#!/bin/sh

# Exit on error
set -e

# Remove old site contents
rm -rf _site

# Copy everything needed to new _site
mkdir _site
cp -r _assembly/styles _site/
cp -r _assembly/fonts _site/
cp index*.md _site/
cp -r grw _site/
cp -r fanwerk _site/

# _site will be our working directory
cd _site

# Create an index file that contains links to all pages
# TODO nice format etc..

echo "# Übersicht über alle Seiten" > alle-seiten.md
echo "" >> alle-seiten.md
find . -iname "*.md" -exec sh -c 'grep -m 1 "^#" "$1" | cut -d" " -f2- | perl -p -e "s/(.*)/[\1]/" | echo "- $(cat -)($1)" >> alle-seiten.md.tmp' sh {} \;
sort alle-seiten.md.tmp >> alle-seiten.md
rm -f alle-seiten.md.tmp

#BASE_URL=https://ronineighty.github.io/Dungeonslayers
BASE_URL=https://fschne.github.io/Dungeonslayers
#BASE_URL=https://www.f-space.de/ds4srd-neuton
#BASE_URL=https://www.f-space.de/ds4srd-gelasio
#BASE_URL=http://localhost/f-space/ds4srd


# Transform all markdown files into .md.html files
find . -name "*.md" -exec \
                    pandoc \
                    --standalone \
                    --from=markdown \
                    --to=html5 \
                    --strip-comments \
                    --table-of-contents \
                    --data-dir ../_assembly/templates/ \
                    --template ../_assembly/templates/default.html \
                    --metadata title="DS4 SRD+" \
                    --metadata lang:de-DE \
                    --variable base-url:"${BASE_URL}" \
                    --css ${BASE_URL}/styles/style.css \
                    --css ${BASE_URL}/styles/layout.css \
                    --include-in-header ../_assembly/templates/javascript.html \
                    -o "{}.html" \
                    "{}" \;

# Pandoc leaves links as is, so change all inline links to .md files to the expected .html
find . -name "*.md.html" -exec perl -i -p -e 's/.md">/.html">/ig' "{}" \;
find . -name "*.md.html" -exec perl -i -p -e 's/.md#(.*?)">/.html#$1">/ig' "{}" \;

# Rename all .md.html to .html, strip .md infix in filename
find . -name "*.md.html" > mv.sh
perl -i -p -e 's/(.*).md.html/mv $1.md.html $1.html/ig' mv.sh
sh mv.sh

# Leave _site
cd ..
