
class Time:
    def __init__(self, hour1, hour2, min1, min2):
        self.hour1 = hour1
        self.hour2 = hour2
        self.min1 = min1
        self.min2 = min2

    # increments hour on a 12-hour clock (ie. 12am -> 1am)
    def incrementHour(self):
        hour = self.hour1*10 + self.hour2
        if hour == 12:
            self.hour1 = 0
            self.hour2 = 1
        else:
            hour += 1
            self.hour2 = int(hour % 10)
            self.hour1 = int((hour-self.hour1)/10)

    # increments minute based on 60min/hour (ie. 11:30 -> 11:31)
    def incrementMin(self):
        minute = self.min1*10 + self.min2
        if minute == 59:
            self.min1 = 0
            self.min2 = 0
            # increments hour when current minute is 59 (ie. 11:59 -> 12:00)
            self.incrementHour()
        else:
            minute += 1
            self.min2 = int(minute % 10)
            self.min1 = int((minute-self.min2)/10)

    # printing time for test purposes
    def printTime(self):
        print(("{hour1}{hour2}:{min1}{min2}").format(
            hour1=self.hour1, hour2=self.hour2, min1=self.min1, min2=self.min2))

    # checking if the current time value is a favorite time
    def checkArithmetic(self):
        firstDiff = self.hour2-self.hour1
        secondDiff = self.min1-self.hour2
        thirdDiff = self.min2-self.min1
        if self.hour1 == 0:
            if secondDiff == thirdDiff:
                return True

        else:
            if firstDiff == secondDiff and secondDiff == thirdDiff:
                return True

        return False


# can input via command line (just enter a number)
# or input via a file in bash: < filename.in python favTimes.py
inputTime = int(input("Enter D (number of mins): "))


# We know the pattern of favorite times repeats every 12 hours
# Here we find out how many 12 hours cycles the input represents...
# ... as well as the number of minutes remaining after these 12 hour cycles

numRemainder = inputTime % (12 * 60)
numCycles = int((inputTime-numRemainder)/(12*60))

# initialize count of valid outputs to 0 and time to 12:00
favCount = 0
time = Time(1, 2, 0, 0)

# finding the number of favorite times in a 12hr cycle then multiplying by # of cycles
if numCycles > 0:
    for i in range(12*60):
        time.incrementMin()
        if time.checkArithmetic():
            favCount += 1

    favCount *= numCycles

# finding the number of favorite times in the remaining # of minutes
for i in range(numRemainder):
    time.incrementMin()
    if time.checkArithmetic():
        favCount += 1

print("\n# of Favorite Times: {favCount}".format(favCount=favCount))
