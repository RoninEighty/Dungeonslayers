#!/bin/sh

# Remove old site contents
rm -rf _site

# Copy everything needed to new _site
mkdir _site
cp index.md _site/
cp -r grw _site/
cp -r styles _site/

# _site will be our working directory
cd _site

# Create an index file that contains links to all pages
find . -iname "*.md" -exec sh -c 'grep -m 1 "^#" "$1" | cut -d" " -f2- | perl -p -e "s/(.*)/[\1]/" | echo "- $(cat -)($1)" >> alle-seiten.md' sh {} \;

BASE_URL=https://fschne.github.io/Dungeonslayers
#BASE_URL=http://localhost/f-space/ds4srd

# --include-before ../templates/sidebar.html \
# --metadata title:"DS4 SRD+" \
# Transform all markdown files into .md.html files
find . -name "*.md" -exec \
                    pandoc \
                    --standalone \
                    --from=markdown \
                    --to=html5 \
                    --strip-comments \
                    --verbose \
                    --data-dir ../templates/ \
                    --template ../templates/default.html \
                    --metadata lang:de-DE \
                    --variable base-url:"${BASE_URL}" \
                    --css ${BASE_URL}/styles/style.css \
                    --css ${BASE_URL}/styles/layout.css \
                    --include-after ../templates/base-url-anchor-script.html \
                    -o "{}.html" \
                    "{}" \;

# Pandoc leaves links as is, so change all inline links to .md files to the expected .html
find . -name "*.md.html" -exec perl -i -p -e 's/.md">/.html">/ig' "{}" \;
find . -name "*.md.html" -exec perl -i -p -e 's/.md#">/.html#">/ig' "{}" \;

# Rename all .md.html to .html, strip .md infix in filename
find . -name "*.md.html" > mv.sh
perl -i -p -e 's/(.*).md.html/mv $1.md.html $1.html/ig' mv.sh
sh mv.sh
rm -f mv.sh

cd ..