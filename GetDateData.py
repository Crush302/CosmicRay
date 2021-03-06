import os

def Date_C2P(date):
    temp = date.split("-")
    year = int(temp[0]) - 2000
    month = int(temp[1])
    day = int(temp[2])
    return str(year*10000 + month*100 + day).rjust(6, "0")

def GetDataDate(date):
    if not os.path.isdir("DataDates/" + date):
        os.mkdir("DataDates/" + date)

    Parentfile = open('RawData/NLDN/Raw_NLDN.txt', 'r')
    for line in Parentfile:
        columns = line.split()
        datePF = Date_C2P(columns[0])

        if datePF == date:
            Datefile = open('DataDates/' + date + '/NLDN.txt', 'a')
            Datefile.write(line)
            Datefile.close()
    Parentfile.close()

    if not os.path.isfile('DataDates/' + date + '/NLDN.txt'):
        open('DataDates/' + date + '/NLDN.txt', 'a')

    for filename in os.listdir("RawData/L0L1/"):
        Parentfile = open('RawData/L0L1/' + filename, 'r')

        for line in Parentfile:
            columns = line.split()
            datePF = columns[0]

            if datePF == date:
                Datefile = open('DataDates/' + date + '/L0L1.txt', 'a')
                Datefile.write(line) #line
                Datefile.close()
        Parentfile.close()

if __name__ == '__main__':
    date = input("What date do you want to get data for? ")

    GetDataDate(date)
