#!/usr/bin/env python3

import time
import argparse
import findspark
findspark.init()
from pyspark import SparkContext

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = \
                                    'Compute Twitter followers.')
    parser.add_argument('-w','--num-workers',default=1,type=int,
                            help = 'Number of workers')
    parser.add_argument('filename',type=str,help='Input filename')
    args = parser.parse_args()

    start = time.time()
    sc = SparkContext(master = f'local[{args.num_workers}]')

    lines = sc.textFile(args.filename)

    # fill in your code here
    def follower_count(line):
        user_id, followers = line.split(":",1)
        followers = followers.strip()

        if followers == "":
            return []
        
        followed = followers.split()
        #spark expects an iterable, so we return a list of tuples (user_id, followed_user) for each followed user
        return [(user_id, followed_user) for followed_user in followed]
    
    #FlatMap applies helper function to each line and flattens the result into a single RDD.
    user_followers = lines.flatMap(follower_count) 
    follower_counts = user_followers.map(lambda x: (x[1], 1)).reduceByKey(lambda a, b: a + b).cache()  # maps each followed user to a count of 1 and then reduces by key to sum the counts for each user
    # ("123", "45") -> ("45", 1), then reduceByKey sums to ("45", follower_count)
    max_number_users = follower_counts.max(key=lambda x: x[1]) # search tuple with max number of followers, x[1] is the follower count
    total_users = lines.map(lambda line: line.split(":",1)[0]).cache() # extract user ids and cache for later use
    total_followers_all_users = follower_counts.map(lambda x: x[1]).sum()
    number_users = total_users.count()
    count_zero_followers = number_users - follower_counts.count()  
    average_followers = total_followers_all_users / number_users
    
    end = time.time()
    
    total_time = end - start

    # the first ??? should be the twitter id
    print(f'max followers: {max_number_users[0]} has {max_number_users[1]} followers')
    print(f'followers on average: {average_followers}')
    print(f'number of user with no followers: {count_zero_followers}')
    print(f'num workers: {args.num_workers}')
    print(f'total time: {total_time}')

