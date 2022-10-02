import pandas as pd
import datetime
import json
import os


def convert_1979():
    """
    Handles shallow moonquake locations file from Nakamura 1979.

    Converts year, day of year, hour, minute, second, into one datetime value, labels rows, and outputs to file.
    """
    columns = ["year", "day", "hour", "minute", "second", "lat", "lng", "magnitude", "comments"]
    file_path_in = os.path.join(os.getcwd(), "data", "nakamura", "nakamura_1979_sm_locations.csv")
    shallow_mq = pd.read_csv(file_path_in, names=columns, header=0)

    # convert days of year to dates
    shallow_mq["date"] = pd.to_datetime(shallow_mq["year"]*1000 + shallow_mq["day"], format="%Y%j")

    # combine hours, minutes, and seconds
    shallow_mq["time"] = shallow_mq.apply(lambda x: datetime.time(x["hour"], x["minute"], x["second"]), axis=1)

    # combine dates and times
    shallow_mq["date"] = (pd.to_datetime(shallow_mq["date"].astype(str) + " " + shallow_mq["time"].astype(str))).astype(str)

    shallow_mq = shallow_mq.drop(index=14)  # nan lat lon
    shallow_mq = shallow_mq.drop(["year", "day", "hour", "minute", "second", "comments", "time"], axis=1)
    shallow_mq["label"] = "Nakamura (1979)"

    # output
    file_path_out = os.path.join(os.getcwd(), "data", "nakamura", "nakamura_1979_sm_locations.json")
    with open(file_path_out, "w") as file_out:
        file_out.write(json.dumps(shallow_mq.to_dict("records"), indent=4))


if __name__ == "__main__":
    convert_1979()
