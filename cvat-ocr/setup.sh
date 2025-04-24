#!/bin/bash
pip install -r requirements.txt

if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install ccache
fi