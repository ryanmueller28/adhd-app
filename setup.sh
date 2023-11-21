#!/bin/bash

#curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
#rustup default nightly

#cargo install diesel_cli --no-default-features --features postgres

python -m ensurepip --upgrade
pip install pyyaml
python3 setup.py
