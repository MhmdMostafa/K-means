import math, pandas

data = [
    ["USA", 10633715, 246732, 6621711, 3765272],
    ["India", 8684039, 128164, 8064548, 491327],
    ["Brazil", 5730361, 163078, 5064344, 502939],
    ["Poland", 618813, 8805, 242875, 367133],
    ["Chile", 524804, 14633, 501426, 8745],
    ["Iraq", 508508, 11482, 436657, 60369],
    ["KSA", 351849, 7021, 338702, 7557],
    ["Pakistan", 348184, 163078, 320065, 21098],
    ["Romania", 324094, 8389, 218086, 97619],
    ["Israel", 321235, 2699, 310061, 8475],
    ["Qatar", 134887, 233, 131926, 2728],
]


column = [
    "Country Name",
    "Total Cases",
    "Total Deaths",
    "Total Recovered",
    "ActiveCases",
]
cluster_columns = ["Country Name", "C1"]
rows = [i for i in range(len(data))]


def dist(x1, y1, z1, x2, y2, z2):
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    z = (z2 - z1) ** 2

    return math.sqrt(x + y + z)


def select_column():
    count = 0
    columns = []
    for i in range(1, len(column)):
        print(f"{column[i]} = [{i}]")
    while True:
        ch_col = int(input(f"Choose the Column {count+1}: "))
        if not ch_col in columns and ch_col < len(column) and ch_col > 0:
            columns.append(ch_col)
            count += 1
        if count == 3:
            return columns


def calc_avg():
    ch_col = select_column()
    row_ch = []
    count = 0
    rows_num = int(input("choose number rows:"))
    avg = [0] * len(ch_col)
    for i in range(rows_num):
        row_ch.append(int(input(f"choose {i+1} row number:")))
    print(row_ch)
    for j in ch_col:
        for i in row_ch:
            avg[count] += data[i][j]
        avg[count] /= len(row_ch)
        avg[count] = float("{:.3f}".format(avg[count]))
        count += 1
    return avg, ch_col


def main():
    pandas.options.display.float_format = "{:.3f}".format
    print(pandas.DataFrame(data, rows, column,))
    choice = int(input("calc avg 1\ncalc kmean 2\nchoice: "))
    if choice == 1:
        print(calc_avg())
    elif choice == 2:
        c = []
        cho2 = int(input("Choose a Cluster by row[1] or avg[2] : "))
        if cho2 == 1:
            ch = []
            chosen_columns = select_column()
            print(f"Clusters: {[i[0] for i in data]}")
            cluster = input("Choose a Cluster: ")
            for i in data:
                if i[0] == cluster:
                    ch = i
                    break
            for i in data:
                ans = dist(
                    ch[chosen_columns[0]],
                    ch[chosen_columns[1]],
                    ch[chosen_columns[2]],
                    i[chosen_columns[0]],
                    i[chosen_columns[1]],
                    i[chosen_columns[2]],
                )
                c.append([i[0], ans])
        elif cho2 == 2:
            avg, chosen_columns = calc_avg()
            for i in data:
                ans = dist(
                    avg[0],
                    avg[1],
                    avg[2],
                    i[chosen_columns[0]],
                    i[chosen_columns[1]],
                    i[chosen_columns[2]],
                )
                c.append([i[0], ans])
        df = pandas.DataFrame(c, rows, cluster_columns)
        print(df)


if __name__ == "__main__":
    main()
