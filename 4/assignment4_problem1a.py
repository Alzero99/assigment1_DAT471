#!/usr/bin/env python3

import time
import argparse
import findspark
findspark.init()
from pyspark import SparkContext

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = \
                                    'Compute Twitter follows.')
    parser.add_argument('-w','--num-workers',default=1,type=int,
                            help = 'Number of workers')
    parser.add_argument('filename',type=str,help='Input filename')
    args = parser.parse_args()

    start = time.time()
    sc = SparkContext(master = f'local[{args.num_workers}]')

    lines = sc.textFile(args.filename)

    # fill in your code here
    # Helper function to compute the number of follows for each user similar to assignment 3, but now we will use Spark transformations and actions.
    def user_following_count(line):
        user_id, follows = line.split(":",1)
        follows = follows.strip()
        user_id = user_id.strip()

        if follows == "":
            following_count = 0
        else:
            following_count = len([x for x in follows.split(",") if x.strip() != ""])  # count the number of non-empty follows])
        return (user_id, following_count)
    
    user_following_counts = lines.map(user_following_count).cache()  # parsinfg the data and caching it for later use
    max_number_users = user_following_counts.max(key=lambda x: x[1]) # search tuple with max number of follows, x[1] is the following count
    total_following_all_users = user_following_counts.map(lambda x: x[1]).sum()
    number_users = user_following_counts.count()
    count_zero_following = user_following_counts.filter(lambda x: x[1] == 0).count()  # filters the RDD to only include users with zero following and counts them 
    average_following = total_following_all_users / number_users
    end = time.time()
    
    total_time = end - start

    # the first ??? should be the twitter id
    print(f'max follows: {max_number_users[0]} follows {max_number_users[1]}')
    print(f'users follow on average: {average_following:.5f}')
    print(f'number of user who follow no-one: {count_zero_following}')
    print(f'num workers: {args.num_workers}')
    print(f'total time: {total_time}')

