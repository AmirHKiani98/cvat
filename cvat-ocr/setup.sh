#!/bin/bash
pip install -r requirements.txt

if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install ccache
    python -m pip install --pre paddlepaddle -i https://www.paddlepaddle.org.cn/packages/nightly/cpu/
fi