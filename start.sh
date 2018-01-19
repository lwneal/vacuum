#!/bin/bash

for agent in SimpleReflexAgent  RandomizedReflexAgent ModelBasedAgent; do
    for world in EmptyRoom FourRooms; do
        python main.py $agent $world.txt 1000 --graph > ${agent}_${world}.csv
        python plot.py ${agent}_${world}.csv
        echo "Output ${agent}_${world}.png"
    done
done
