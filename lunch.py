import random
import smtplib



lunchOptions = []
filePath = '/home/zewanimal/Documents/Lunch_Options.txt'

with open(filePath) as lunchFile:
    for line in lunchFile:
        lunchOptions.append(line)


listSize = len(lunchOptions)-1
print listSize

todaysWinner = random.randint(0, listSize)
print lunchOptions[todaysWinner]




smtpObj = smtplib.SMTP


def getCurrentAnaBitRate(self, port):
    """
    :param port: Checks the current, or instantaneous, bit rate received  by
                an Analyzer on a given port.
    :return: Instantaneous bit rate value as a string.
    """
    self.cli.execute("show status ana {}".format(port))
    return self.cli.parse(self.cli.parsers["status_ana"].format(i=port)).group("cur_bit_rate")