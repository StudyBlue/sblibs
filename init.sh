#!/bin/bash
echo "Running init...."

if [ $# -eq 0 ]
then
    echo "You must specify the name of the project as an argument!"
    exit 1
fi

# Replacing every occurence of sblibs with the project name.
echo "Finding all the occurences of 'sblibs' and replacing them with $1..."
for f in `rg sblibs -l`; do 
    sed -i.bak "s/[Ss][Aa][Mm][Pp][Ll][Ee]/$1/g" $f
    find ./ -name '*.bak' -delete
done

touch initialized
