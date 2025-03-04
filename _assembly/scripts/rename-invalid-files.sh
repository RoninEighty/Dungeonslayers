#!/bin/sh

# Exit on error
set -e

# Replace umlauts and spaces, remove all other non numerical special chars.
find . -iname "*.md" -exec rename 's/ä/ae/ig' "{}" \;
find . -iname "*.md" -exec rename 's/ö/oe/ig' "{}" \;
find . -iname "*.md" -exec rename 's/ü/ue/ig' "{}" \;
find . -iname "*.md" -exec rename 's/ß/ss/ig' "{}" \;
find . -iname "*.md" -exec rename 's/\s/-/ig' "{}" \;
find . -iname "*.md" -exec rename 's/[^A-Za-z0-9\/\.\-]//ig' "{}" \;
