#!/bin/bash

# Scripts to find all the zombie process and kill them
kill_zombie_process() {
    #Find all zombie processes
    zombies=$(ps -eo stat,pid | grep -w Z)

    if [  -n "zombies" ]; then
      echo "found zombies"
      echo "$zombies"
      echo "killing zombies"

      echo "$zombies" | awk  '{print $2}' | xargs kill -9
      echo "zombies killed"
    else
      echo "no zombie process found"
    fi
}