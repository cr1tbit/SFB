 dirlist=$(find $1 -mindepth 2 -maxdepth 2 -type d)

for dir in $dirlist
do(
    echo compiling $dir...
    asciidoctor -a data-uri $dir/content.adoc -s
)
done