#!/bin/bash

echo "Enter a definition:"
read -r input

# regex for string
 regex="^-?[a-z]+_to_-?[a-z]+\s-?[0-9.]+$"



 # Check the variable with regex expressions
 if [[ $input =~ $regex ]]; then
    echo "The definition is correct!"
else
    echo "The definition is incorrect!"
fi