#!/usr/bin/env python

all:
	pip install pyinstaller
	pyinstaller --onefile arith.py
	mv dist/arith .
	rm arith.spec 
	rm -r __pycache__ build dist

main:
	python3 arith.py

clean:
	rm arith