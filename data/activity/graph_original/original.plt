set terminal postscript eps enhanced "Helvetica" 25 color
set size 3.0,0.8
set output 'original.eps'
set border 11
set datafile separator ','

set style line 1 lt 1 lw 2 pt 3 ps 0.5 lc rgb 'black'
set timefmt "%Y/%m/%d %H:%M"
set format x "%m/%d"

set xdata time
set xrange ["2016/09/23 00:00":"2016/09/24 00:00"]
set yrange [10: 100000]
set key top right
set ytics (10, 100, 1000, 10000, 100000)
set title "Original"

# set autoscale y
set ytics nomirror font "Helvetica,22"
set ytics textcolor rgb "red"

set xlabel 'Time' offset 1,0 font "Helvetica,28"
set ylabel 'Log Traffic Rate (KB/min)' offset 1,0 font "Helvetica,28"
set logscale y 10

plot 'original.csv' using 1:($2/1024) title '' with lines ls 1
