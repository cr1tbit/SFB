#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: ./generate_article_stub.sh 'category' 'article name' "
    exit
fi

CATEGORY=$1
ART_NAME=$2

#1. create stub-name out of the title
STUB_NAME=$(sed "s/ /-/g" <<< "$ART_NAME")

#2. create folder for the category, and the article
mkdir -p $CATEGORY/$STUB_NAME

#3. customize JSON 
sed "s/{tag}/$STUB_NAME/; s/{title}/$ART_NAME/; s/{timestamp}/$(date +'%Y-%m-%d %H:%M')/g; s/{category}/$CATEGORY/" template_meta.json > $CATEGORY/$STUB_NAME/meta.json 

#4. copy markdown stub
cp template_content.md $CATEGORY/$STUB_NAME/content.md

