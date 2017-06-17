#!/bin/bash

function usage(){
    echo "Usage: $0 -u username -m agile_module_name -v version -d stone_app_dir -n stone_app_name "
}



function check_parameters(){

    if [ "x$USERNAME" == "x" ]
    then
        echo "PARAM ERROR: USERNAME IS NULL (-u)" >&2
        exit -1
    fi

    if [ "x$AGILE_MODULE_NAME" == "x" ]
    then
        echo "PARAM ERROR: AGILE_MODULE_NAME IS NULL (-m)"
        exit -1
    fi

    if [ "x$VERSION" == "x" ]
    then
        echo "PARAM ERROR: VERSION IS NULL (-v)"
        exit -1
    fi

    if [ "x$STONE_APP_DIR" == "x" ]
    then
        echo "PARAM ERROR: STONE_APP_DIR IS NULL (-d)"
        exit -1
    fi

    if [ "x$STONE_APP_NAME" == "x" ]
    then
        echo "PARAM ERROR: STONE_APP_NAME IS NULL (-n)"
        exit -1
    fi

}


get_curr_dir(){
#    curr_dir_relative=`dirname $(readlink -f $BASH_SOURCE)`
    curr_dir_relative=`pwd` # test on Mac OSX
}


get_curr_dir_path_abs(){
    local dir=$curr_dir_relative
    cd $dir
    abs_path=`pwd`
}


function prepare_python(){
    get_curr_dir
    get_curr_dir_path_abs
    echo 'curr_path_abs= '$abs_path
}


#function run_python(){
#
#
#}




######################### Main #################################
while getopts "u:m:v:d:n:h" opt
do
    case $opt in
        u)
            USERNAME=$OPTARG
            echo "USERNAME= "$USERNAME
        ;;
        m)
            AGILE_MODULE_NAME=$OPTARG
            echo "AGILE_MODULE_NAME= "$AGILE_MODULE_NAME
        ;;
        v)
            VERSION=$OPTARG
            echo "VERSION= "$VERSION
        ;;
        d)
            STONE_APP_DIR=$OPTARG
            echo "STONE_APP_DIR="$STONE_APP_DIR
        ;;
        n)
            STONE_APP_NAME=$OPTARG
            echo "STONE_APP_NAME="$STONE_APP_NAME
        ;;
        *)
            echo "ERROR don't support this parameter" >&2
            usage
            exit -1
        ;;
    esac
done

check_parameters
prepare_python