import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

url = args.url
df = pd.read_csv(url, sep="\t", names = ["course_col"])

course_col = df[df["course_col"].str.contains("https")]

courseID = course_col["course_col"].str.split("]").apply(lambda x: x[0].replace("[", "").split()[3])
course_link = course_col["course_col"].str.split("]").apply(lambda x: x[1].replace("(", "").replace(")", "").split()[0])

clone = "git clone " + course_link + ".git"
cd = "cd " + courseID + "_students && rm -rf .git"

clone.apply(lambda x: os.system(x))
cd.apply(lambda x: os.system(x))
