#!/usr/bin/env bash

while [ -n "$1" ]
do
    case $1 in
        "--input_folder")
            input_folder=$2
            ;;
        "--extension")
            extencion=$2
            ;;       
        "--backup_folder")
            backup_folder=$2
            ;;
        "--backup_archive_name")
            backup_archive_name=$2
            ;;
    esac
    shift 2
done

mkdir $backup_folder
find $input_folder -name "*.$extencion" | xargs cp --parents -t $backup_folder
tar -czf $backup_archive_name $backup_folder 

echo "done"
