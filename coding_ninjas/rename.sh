#! /usr/bin/bash

# let us say new directory name is passed here

newname=$(echo "$1" | tr -d "_")

# newname now contains the file name with underscore removed from it

echo " new name is $newname"

mv "$1" "$newname"

echo renamed

exit 0
