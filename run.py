import logging
import random

from src.csv import *
from src.nlp import *


def main():
    headers = get_headers("./data/dataset.csv")
    dataset = read_csv("./data/dataset.csv")

    logging.basicConfig(filename="log.txt", filemode='w', level=logging.DEBUG)

    dataset_prep = []
    project_list = []

    result = []
    compare = []

    statistics = []

    for row in dataset:
        index = int(row[0])
        project = row[1].lower()
        description = preprocess(row[2])
        weight = int(row[3])

        dataset_prep.append([index, project, description, weight])
        project_list.append(project)

    project_list = list(set(project_list))
    project_list.sort(key=lambda f: int(f.split(" ")[1]))

    while len(project_list) > 3:
        p1 = random.choice(project_list)
        project_list.remove(p1)

        p2 = random.choice(project_list)
        project_list.remove(p2)

        test_data = [row for row in dataset_prep if row[1] in {p1, p2}]

        for item in test_data:
            item_index = item[0]
            best_index = 0
            best_value = 0

            for row in dataset_prep:
                if item[1] == row[1]:
                    continue
                similarity = item[2].similarity(row[2])
                if similarity > best_value:
                    best_value = similarity
                    best_index = row[0]

            if best_value >= 0.85:
                expected = dataset[item_index - 1][-1:]
                got = dataset[best_index - 1][-1:]

                result.append(dataset[item_index - 1][:-1] + got)
                compare.append(
                    dataset[item_index - 1][:-1] +
                    expected +
                    got
                )

                statistics.append(abs(int(got[0]) - int(expected[0])))

                logging.debug(
                    f"\n{dataset[item_index - 1][1]}"
                    f"\n{dataset[item_index - 1][2]}"
                    f"\n{dataset[best_index - 1][2]}"
                    f"\n{dataset_prep[item_index - 1][2]}"
                    f"\n{dataset_prep[best_index - 1][2]}"
                    f"\n{best_value}\n"
                )

    mean = sum(statistics) / len(statistics)
    variance = sum([((x - mean) ** 2) for x in statistics]) / len(statistics)
    std_dev = variance ** 0.5

    for index, row in enumerate(compare):
        row.append(statistics[index])
        row.append("{:.2f}".format(mean))
        row.append("{:.2f}".format(variance))
        row.append("{:.2f}".format(std_dev))

    result.sort(key=lambda f: int(f[0]))

    write_csv("./data/result.csv", headers, result)
    write_csv(
        "./data/compare.csv",
        headers + ["Estimativa", "Distância", "Média", "Variância", "Desvio Padrão"],
        compare
    )


main()
