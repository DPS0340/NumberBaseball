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
                if int(temp) > 9:
                    print("10 이상은 불가능합니다.")
                    continue
                self.count = int(temp)
                break
            except:
                print("숫자가 아닙니다.")
                continue
        while len(self.nums) < self.count:
            n = random.randint(1, 9)
            if n in self.nums:
                continue
            else:
                self.nums.append(n)
        print(self.nums) # 디버깅 모드

    def check(self, numbers):
        numList = list(map(int, list(str(numbers))))
        print(numList)
        strikeCount = 0
        ballCount = 0
        for i in range(len(self.nums)):
            if self.nums[i] == numList[i]:
                strikeCount += 1
        for i in range(len(self.nums)):
            for j in range(len(numList)):
                if i != j and self.nums[i] == numList[j]:
                    ballCount += 1
        return {"strike": strikeCount, "ball": ballCount}

    def isDuplicateNumber(self, numbers):
        numList = list(map(int, str(numbers).split()))
        for i in range(len(numList)):
            for j in range(len(numList)):
                if i != j:
                    if numList[i] == numList[j]:
                        return True
        return False

    def getInt(self):
        number = input("숫자 %d개 입력(공백 없이): " % self.count)
        try:
            number = int(number)
            if len(str(number)) != self.count:
                print("자릿수가 맞지 않음")
                return False
            elif self.isDuplicateNumber(number):
                print()
            else:
                return number
        except:
            print("숫자가 아님")
            return False

    def run(self):
        self.init()
        print("규칙: 1~9까지의 자연수 n개를 맞추는 게임")
        print("숫자야구 시작")
        while not self.win:
            numbers = 0
            while True:
                temp = self.getInt()
                if temp:
                    numbers = temp
                    break
            result = self.check(numbers)
            if result["ball"] == 0:
                print("노 볼 ")
            else:
                print("%d 볼 " % result["ball"])
            if result["strike"] == 0:
                print("노 스트라이크")
            else:
                print("%d 스트라이크" % result["strike"])
            if result["strike"] == self.count:
                self.win = True
        print("이겼습니다!")


if __name__ == "__main__":
    main = Main()
    main.run()