#!/bin/sh

# Exit on error
set -e

# Remove old site contents
rm -rf _site

# Copy everything needed to new _site
mkdir _site
cp -r _assembly/styles _site/
cp -r _assembly/fonts _site/
cp *.md _site/
cp -r abenteuer _site/
#cp -r bestiarium _site/
cp -r fanwerk _site/
cp -r grw _site/
cp -r spielwiese _site/
cp -r images _site/
#cp -r talente _site/
#cp -r zauber _site/

# _site will be our working directory
cd _site

# Create an index file that contains links to all pages
# TODO nice format etc..

echo "---" > alle-seiten.md
echo "title: Übersicht über alle Seiten" >> alle-seiten.md
echo "---" >> alle-seiten.md
echo "" >> alle-seiten.md
echo "# Übersicht über alle Seiten" >> alle-seiten.md
echo "" >> alle-seiten.md
find . -iname "*.md" -exec sh -c 'grep -m 1 "^#" "$1" | cut -d" " -f2- | perl -p -e "s/(.*)/[\1]/" | echo "- $(cat -)($1)" >> alle-seiten.md.tmp' sh {} \;
sort alle-seiten.md.tmp >> alle-seiten.md
rm -f alle-seiten.md.tmp

REPO_URL=https://raw.githubusercontent.com/RoninEighty/Dungeonslayers/refs/heads/main

BASE_URL=https://immersieg.de
BASE_URL_ESCAPED=https:\\\/\\\/immersieg.de
#BASE_URL=https://ronineighty.github.io/Dungeonslayers
#BASE_URL_ESCAPED=https:\\\/\\\/ronineighty.github.io\\\/Dungeonslayers
#BASE_URL=https://fschne.github.io/Dungeonslayers
#BASE_URL_ESCAPED=https:\\\/\\\/fschne.github.io\\\/Dungeonslayers
#BASE_URL=http://localhost/f-space/ds4srd-test
#BASE_URL_ESCAPED=http:\\\/\\\/localhost\\\/f-space\\\/ds4srd-test

# Inject BASE_URL_ESCAPED in style.css
perl -pi -e "s/BASE_URL/${BASE_URL_ESCAPED}/g" styles/fonts.css

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
                    --metadata title-prefix="Immersieg" \
                    --metadata lang:de-DE \
                    --variable base-url:"${BASE_URL}" \
                    --variable repo-url:"${REPO_URL}" \
                    --css ${BASE_URL}/styles/fonts.css \
                    --css ${BASE_URL}/styles/layout.css \
                    --css ${BASE_URL}/styles/style.css \
                    --include-in-header ../_assembly/templates/javascript.html \
                    -o "{}.html" \
                    "{}" \;

# Pandoc leaves links as is, so change all inline links to .md files to the expected .html
find . -name "*.md.html" -exec perl -i -p -e 's/\.md">/.html">/ig' "{}" \;
find . -name "*.md.html" -exec perl -i -p -e 's/\.md#(.*?)">/.html#$1">/ig' "{}" \;

# Links to source files had been added with .ref suffix to prevent the change from .md to .html
# Now rewrite the links to .md and strip the leading ./ in the link title, too
find . -name "*.md.html" -exec perl -i -p -e 's/\.ref"/"/ig' "{}" \;

# Rename all .md.html to .html, strip .md infix in filename
find . -name "*.md.html" > mv.sh
perl -i -p -e 's/(.*).md.html/mv $1.md.html $1.html/ig' mv.sh
sh mv.sh

# Leave _site
cd ..
