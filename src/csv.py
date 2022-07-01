import csv


def read_csv(file):
    with open(file, encoding="utf-8") as f:
        lines = csv.reader(f)
        next(lines, None)  # skip headers
        return [[column for column in line] for line in lines]


def write_csv(file, headers, classified_backlog):
    with open(file, "w+", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(headers)
        writer.writerows(classified_backlog)


def get_headers(file):
    with open(file, encoding="utf-8") as f:
        lines = csv.reader(f)
        return next(lines, None)
