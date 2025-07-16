#!/bin/bash

# Prints the input, without the random seed
echo "${@:1:$#-1}"
