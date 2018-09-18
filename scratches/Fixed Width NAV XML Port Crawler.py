
def read_file():
    file = open(r"", "r")
    lista = dict()
    with file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if ';2 ;' in line:
                splittine = line.split(r";")
                avain = splittine[2].replace(" ", "")
                y = i + 1
                while not 'Width=' in lines[y]:
                    y += 1
                pituussplit = lines[y].split('Width=')
                pituus = pituussplit[1][:2]
                lista[avain] = pituus

    startpossa = 1
    for k, v in lista.items():
        formatted = k +"\t" + v + "\t" + "{startpossa}".format(startpossa=startpossa)
        print(formatted)
        startpossa += int(float(v))

    file.close()


def main():
    read_file()


if __name__ == "__main__":
    main()