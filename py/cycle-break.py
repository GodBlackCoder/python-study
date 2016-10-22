#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sum = 0
x = 1
while True:
	x = x + 1
	if x > 100:
		break
	if x % 2 == 0:
		continue
	sum = sum + x
print sum
