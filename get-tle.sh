#!/bin/bash
wget http://celestrak.com/NORAD/elements/amateur.txt
wget http://celestrak.com/NORAD/elements/visual.txt
wget http://celestrak.com/NORAD/elements/weather.txt
wget http://celestrak.com/NORAD/elements/cubesat.txt
wget http://celestrak.com/NORAD/elements/science.txt
wget http://celestrak.com/NORAD/elements/engineering.txt

./populate-db.py amateur.txt
./populate-db.py visual.txt
./populate-db.py weather.txt
./populate-db.py cubesat.txt
./populate-db.py science.txt
./populate-db.py engineering.txt
