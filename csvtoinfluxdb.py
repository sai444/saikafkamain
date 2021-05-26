import datetime
import random
import time
import os
import csv
from csv import reader
import argparse
# from influxdb import client as influxdb


# db = influxdb.InfluxDBClient("127.0.0.1", 8086, "", "", "stocks")


def read_data(filename):
    print (filename)
    with open(filename) as f:
        lines = f.readlines()[1:]

    return lines

if __name__ == '__main__':
    filename = r"data.csv"
    lines = read_data(filename)
    for rawline in lines:
        line = rawline.split(",")
      #   d= getPythonDateTimeFromStr(line[0], line[1])
        #EVERYTHING UP TO HERE WORKS. Not sure how to create the json below
        #====================================
        json_body = [
        {
            "measurement": "quote",
            "tags": {
            "project": line[0],
           
           },
            # "time": d,
            "fields": {
                "owner": line[1],
              
            }
        }
        ]

        print (json_body)

      #   db.write_points(json_body )