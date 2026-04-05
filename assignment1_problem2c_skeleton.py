#!/usr/bin/env python3

import sys
import duckdb

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write(f'Usage: {sys.argv[0]} <input_csv> <SQL query>\n')
        sys.exit(1)
    
    input_csv = sys.argv[1]
    sql_query = sys.argv[2]

    with duckdb.connect(database=":memory:") as con:
        con.execute('CREATE VIEW hour AS SELECT * FROM ' + 
                    f'read_csv_auto(\'{input_csv}\', header=True);')
        print(con.execute(sql_query).df())