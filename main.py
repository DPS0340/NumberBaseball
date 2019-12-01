import random

class Main:
    def __init__(self):
        self.count = 0
        self.nums = []
        self.win = False

    def init(self):
        self.nums.clear()
        while True:
            temp = input("숫자 몇개로 하시겠습니까? ")
            try:
                int(temp)
            except:
                print("숫자가 아닙니다.")
                continue
            if int(temp) <= 0:
                print("0 이하는 불가능합니다.")
                continue
            if int(temp) >= 10:
                print("10 이상은 불가능합니다.")
                continue
            self.count = int(temp)
            break
        while len(self.nums) < self.count:
            n = random.randint(1, 9)
            if n in self.nums:
                continue
            self.nums.append(n)
        # print(self.nums) # on When Debugging

    def run(self):
        self.init()
        print("규칙: 1~9까지의 자연수 n개를 맞추는 게임")
        print("숫자야구 시작")
        self.loop()
        print("이겼습니다!")

    def loop(self):
        while not self.isWin():
            numbers = self.getNumbersInLoop()
            result = self.check(numbers)
            self.printResult(result)
            if result["strike"] == self.count:
                self.gameWin()

    def check(self, numbers):
        numList = self.splitIntIntoList(numbers)
        print(numList)
        strikeCount = self.countStrike(numList)
        ballCount = self.countBall(numList)
        return {"strike": strikeCount, "ball": ballCount}

    def splitIntIntoList(self, numbers):
        return list(map(int, list(str(numbers))))

    def isDuplicateNumber(self, numbers):
        numList = self.splitIntIntoList(numbers)
        for i in range(len(numList)):
            for j in range(len(numList)):
                if i != j and numList[i] == numList[j]:
                    return True
        return False

    def isNumber(self, number):
        try:
            int(number)
        except:
            return False
        return True

    def isLengthEqualsCount(self, number):
        if len(str(number)) != self.count:
            return False
        return True

    def getInt(self):
        number = input("숫자 %d개 입력(공백 없이): " % self.count)
        if not self.isNumber(number):
            print("숫자가 아님")
            return False
        if not self.isLengthEqualsCount(number):
            print("자릿수가 맞지 않음")
            return False
        if self.isDuplicateNumber(number):
            print("중복된 숫자가 있음")
            return False
        return number

    def isWin(self):
        return self.win

    def gameWin(self):
        self.win = True

    def printResult(self, result):
        if result["ball"] == 0:
            print("노 볼 ", end="")
        else:
            print("%d 볼 " % result["ball"], end="")

        if result["strike"] == 0:
            print("노 스트라이크")
        else:
            print("%d 스트라이크" % result["strike"])

    def getNumbersInLoop(self):
        while True:
            temp = self.getInt()
            if temp:
                return temp

    def countBall(self, numList):
        res = 0
        for i in range(len(self.nums)):
            for j in range(len(numList)):
                if i != j and self.nums[i] == numList[j]:
                    res += 1
        return res

    def countStrike(self, numList):
        res = 0
        for i in range(len(self.nums)):
            if self.nums[i] == numList[i]:
                res += 1
        return res


if __name__ == "__main__":
    main = Main()
    main.run()