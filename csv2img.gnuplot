#!/usr/bin/gnuplot -persist
if (!exists("fileoutput")) fileoutput='123.dat'

set terminal png size 336,300 enhanced font "Helvetica,10"
set output fileOut
set datafile separator ","
set tics out
plot fileIn using 2 with line notitle
