class OreoCookie:

    def __init__(self):
        self.calorie = 52.3
        self.sodium = 63.3
        self.carbohydrate = 8.3
        self.fat = 2.3
        self.maximumAllowedCalories = 2000


    def cosumedCookiesCalculation(self, eatenCookies):
        print("\nYou currently get {} calories from eating {} cookies, "
              "\nand you'll be allowed another {} calories today.\n".format(self.calculateCalories(eatenCookies), eatenCookies, self.remainingCalories(eatenCookies)))


    def calculateCalories(self, eatenCookies):
        return float(eatenCookies) * float(self.calorie)


    def remainingCalories(self, eatenCookies):
        remainedCalories = float(self.maximumAllowedCalories) - float(eatenCookies) * float(self.calorie)

        if(remainedCalories <= 0):
            print(textColors.FAIL + "\nAlthough this cookie is delicious, you have to stop eating it because you've had the "
                  "\nmaximum number of calories for the day, which is {}.".format(self.maximumAllowedCalories) + textColors.ENDC)
            return 0
        else:
            return remainedCalories


class textColors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


if __name__ == '__main__':

    eaten_OreoCookie = OreoCookie()
    print(textColors.BOLD + textColors.HEADER + "\nOreo Cookie calorie calculator\n" + textColors.ENDC)

    print(textColors.WARNING + 
          "-------------------------------------------\n"
          "The nutritional value of each cookie is:\n\n"
          "Calories: {}\n"
          "Sodium: {}\n"
          "Carbohydrate: {}\n"
          "Fat: {}\n"
          "-------------------------------------------\n"
          .format(eaten_OreoCookie.calorie, eaten_OreoCookie.sodium, eaten_OreoCookie.carbohydrate, eaten_OreoCookie.fat)
           + textColors.ENDC)

    while True:
        action = input("How much cookie you ate today? ")
        if not action.isnumeric():
            print("I don't know how to do that!")
            continue
        else:
            eaten_OreoCookie.cosumedCookiesCalculation(action)
            

#Written by (Mehdi Daustany) at the request of the University of the Netherlands
#https://github.com/daustany/OreoCookie.git