#!/bin/bash
# 1 gigabyte is usually 2**30 bytes (though you can use 10**9 for 109 bytes instead). The * 3/4 part accounts for Base64 overhead, making the encoded output 1 GB.

openssl rand -out random.txt -base64 $(( 2**30 * 3/4 * 25 )) # generate 25gb file
