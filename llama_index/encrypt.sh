#!/bin/bash

usage() {
    echo "Usage: $0 <password>"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
fi

# Encrypt a file using a password
pushd persist

for i in *; do
    openssl enc -aes-256-ecb -a -e -pbkdf2 -md sha512 -in $i -out $i.enc -k $1
    rm $i
done

popd
echo Done