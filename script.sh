#!/bin/bash

NUM1=1
NUM2=2

if [ $NUM1 < $NUM2 ]; then
    echo "${NUM1} is lower}"
else
    echo "${NUM1} is higher"
fi