#!/usr/bin/env python3

import sys
import duckdb

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f'Usage: {sys.argv[0]} <input_csv>\n')
        sys.exit(1)
    
    input_csv = sys.argv[1]
    sql_query = sys.argv[2]

    with duckdb.connect(database=":memory:") as con:
        con.execute('CREATE VIEW hour AS SELECT * FROM ' + 
                    f'read_csv_auto(\'{input_csv}\', header=True);')

        print("How many rows of data there are in the file?")
        print(con.execute("SELECT COUNT(*) AS row_count FROM hour").df())    
        print("What was the average hourly count of bike rentals?")  
        print(con.execute("SELECT AVG(cnt) AS avg_hourly FROM hour").df())
        print("Which were the top-5 busiest hours in terms of average bike rentals?")
        print(con.execute("SELECT hr,AVG(cnt) AS avg_hourly FROM hour GROUP BY hr ORDER BY avg_hourly DESC LIMIT 5").df())
        print("What was the average daily count of bike rentals in the month of January 2012?")
        print(con.execute("SELECT AVG(daily_count) AS avg_daily FROM ( SELECT dteday, SUM(cnt) AS daily_count FROM hour WHERE yr=1 AND mnth=1 GROUP BY dteday )").df())
