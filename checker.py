import csv
from collections import OrderedDict
import serial
class Checker():

    def __init__(self):
        with open('updater.csv', 'a', newline='') as csvfile:
            s = csv.writer(csvfile, delimiter = ',')
            p = ['New Session', 'Name', 'Time Entered', 'Time Left']
            s.writerow(p)
            self.ser = serial.Serial('/dev/ttyACM0', 9600)
            main_dict = {
                'Mayunk Kulkarni': '70C3F3D',
                'Adarsh Pattanayak': '8060F5D',
                'Param Malhotra': 'FE95A07',
                'krishna chaitanya': 'AE9FCAB',
                'Debjeet Choudhury': 'F0BEF3D',
                'Mukul Joshi': 'DEBAA07',
                'ManuKoushik': 'FCBDA4C',
                'siddharth': '5EF6A17',
                'Rajendra Kotha': '6EA845D',
                'Aparna Roy': '6E90A17',
                'dharmendra baruah': '3E8849D',
                'suraj m': 'C68B408',
                'sebanti dasgupta': '7E06A27',
                'Kuber Nandwani': 'BE6A97D',
                'Shivang Bharadwaj': '4E86A17',
                'Priyanka Singh': 'C0D1F3D',
                'Srikriti Dahagam': '0E11A27',
                'Sharat Chandra': '7053F6D',
                'Nidhish Kamath': '1EAFA17',
                'Lakshya Bevli': 'CEE1A17',
                'Ritesh Patra': 'FE9410D',
                'K S Viswanath': '56B4468',
                'P.Lohit Kumar Reddy': 'DECC0D7',
                'Rishabh Pahuja': '40E6E3D',
                'Chirag Bhati': '609EE5D',
                'Shivang Kedia': 'C01DE8D',
                'manoj bhat': '9371ECE',
                'Pranshu Shubham': 'F000E5D',
                'Prachi Sinha': 'B0FEF3D',
                'Ayush Sinha': 'D2DD36B',
            }
        self.mainD = OrderedDict(sorted(main_dict.items(), key=lambda t: t[0]))
        self.flag = []
        for i in range[1, 50]:
            self.flag.append(0)

    def get_serial(self, r):
        val = self.ser.readline()
        val = str(val)
        val.strip()
        val.replace(" ", "")
        rfid = val[0:7]
        date = val[8:]

        if r == 'rfid':
            return rfid
        if r == 'date':
            return date

    def check_in(self):
        count = 0
        rfid = self.get_serial('rfid')
        date_entry = self.get_serial('date')
        for i in self.mainD.values():
            if rfid == i:
                if self.flag[count] >= 2:
                    if self.flag[count] == 0:
                        self.flag[count] = 1
                        with open('updater.csv', 'a', newline='') as csvfile:
                            s = csv.writer(csvfile, delimiter = ',')
                            p = ['', rfid, date_entry]
                            s.writerows(p)
                    if self.flag[count] == 1:
                        self.flag[count] = 2





if __name__ == '__main__':
    x = Checker()