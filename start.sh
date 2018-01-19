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


ITERS=50
echo "Running randomized agent $ITERS times"
for agent in RandomizedReflexAgentA RandomizedReflexAgentB RandomizedReflexAgentC; do
    for world in EmptyRoom FourRooms; do
        fn=time_to_90_${agent}_$world.txt
        rm -f $fn
        for i in `seq $ITERS`; do
            python main.py $agent $world.txt 10000 --time-to-90 >> $fn
        done
    done
    echo "Best 45 run times for $agent $world:"
    cat $fn | sort -n | tail -45
done

