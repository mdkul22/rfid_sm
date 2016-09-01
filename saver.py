import serial
ser = serial.Serial('COM6', 9600)

class Saver():

    def readr(self):
        self.x = ser.readline()
        s = str(self.x)
        s = s.replace("b'Card UID:", "")
        s = s.replace(" ", "")
        s = s[0:7]
        print(s)
        self.name = input("Write your name: ")
        f = open('details', 'a')
        f.write(str(self.name) + "," + s + "\n")


if __name__ == '__main__':
    x = Saver()
    while True:
        x.readr()