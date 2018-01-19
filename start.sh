#!/bin/bash

echo "Running standard agents..."
for agent in SimpleReflexAgent  RandomizedReflexAgent ModelBasedAgent; do
    for world in EmptyRoom FourRooms; do
        python main.py $agent $world.txt 1000 --graph > ${agent}_${world}.csv
        python plot.py ${agent}_${world}.csv
        echo "Output ${agent}_${world}.png"
    done
done

agent=RandomizedReflexAgent
ITERS=50
echo "Running randomized agent $ITERS times"
for world in EmptyRoom FourRooms; do
    for i in `seq $ITERS`; do
        python main.py $agent $world.txt 50 --graph > ${agent}_${world}_$i.csv
    done
    python avg_csv.py ${agent}_${world}_*.csv
    python plot.py averaged_${agent}_${world}.csv
done
