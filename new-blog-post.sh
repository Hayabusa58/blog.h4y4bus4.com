#!/bin/bash
set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <title>"
    exit 1
fi

TITLE="$1"
DIR="$PWD/content/blog/$TITLE"

python3 $PWD/tools/generate-post.py "$TITLE" "$DIR"
