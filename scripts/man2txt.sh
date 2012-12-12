#! /bin/sh

to_gzip() {
    if [ $# -le 0 ]
    then
        return -1
    fi

    name=$1
    full_path=$1

    IFS='/'
    for i in $name; do
        name=$i
    done

    IFS=''
    gzip -cd $full_path > raw/$name.txt
}


for i in $@; do
    to_gzip $i
done
