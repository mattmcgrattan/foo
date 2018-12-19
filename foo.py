import csv
import glob

stuff = []

with open('sample.csv', newline='') as csvfile:
    foo = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    fieldnames = foo.fieldnames
    r = next(foo)


with open('sample2.csv', 'w') as newcsv:
    bar = csv.DictWriter(newcsv, delimiter=",", quotechar='"', fieldnames=fieldnames)
    jpxs = glob.glob('*.jp2')
    bar.writeheader()
    for i, x in enumerate(jpxs):
        row = r
        r["Line"] = i
        r["Space"] = 22
        r["Origin"] = "https://mattmcgrattan.github.io/foo/" + str(x)
        r["Reference1"] = "Vol250"
        r["NumberReference1"] = x.split("_")[-1].replace(".jp2","")
        bar.writerow(r)

