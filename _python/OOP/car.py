# Bmw:
#     attributes:
#         1 windshield
#         4 wheels
        # model name (vary)
        # numdoors (vary)
        # mileage: 0
    # actions:
    #     drive
    #     play radio


class BMW:
    def __init__(self, modelInput, numDoorsInput, ownerName):
        #put your attributes here using keyword self
        self.windshieldCount = 1
        self.numWheels = 4
        self.modelNumber = modelInput
        self.numDoors = numDoorsInput
        self.mileage = 0
        self.owner = ownerName
    
    def drive(self, numMiles):
        self.mileage += numMiles
    
    def playRadio(self, songInput):
        print(f"{self.owner} is playing {songInput} now!! ")

    def displayInfo(self):
        print(f"Owner: {self.owner}, Mileage: {self.mileage}, Model: {self.modelNumber}")

#objects-> instances of a class
car1 = BMW('i8', 2, 'James')
car2 = BMW('535i', 4, 'Maurice')
car3 = BMW('i8', 2, 'Daniel')

car1.drive(10)
car2.drive(2)

car1.displayInfo()
car2.displayInfo()
car3.displayInfo()