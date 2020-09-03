from datetime import datetime

def convertAFD(file, company):
    data = dict()
    appointments = list()
    openFile = open(file, 'r')
    companyFile = openFile.readline()

    if company == companyFile[11:25].strip():

        for line in openFile:

            if line[9].strip() == '3':
                d = datetime.strptime(line[10:18].strip(), '%d%m%Y')
                h = datetime.strptime(line[18:20].strip()+':'+line[20:22].strip()+':00', '%H:%M:%S')

                data['date'] = d.strftime('%Y-%m-%d')
                data['hour'] = h.strftime('%H:%M:%S')
                data['PIS'] = line[22:34].strip()

                appointments.append(data.copy())
                data.clear()
    else:
        print('Arquivo importado não é desta empresa!')

    return appointments