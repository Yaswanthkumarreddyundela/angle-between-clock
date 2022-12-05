### mini project ###

""" THE BELOW MINI PROJECT IS BASED ON ANGLE
             BETWEEN HOURS HAND AND MINUTES HAND AND WE
                    NEED TO PRINT THE SMALLEST ANGLE BETWEEN THEM"""

# TYPE 1 BY USING IF AND ELSE

HOURS_HAND = int(input("HOURS HAND : "))
MINUTES_HAND = int(input("MINUTES HAND : "))
if 1<=HOURS_HAND<=24  and 1<=MINUTES_HAND<=60 :
    if 1<=HOURS_HAND<=12 :
         HOURS_HAND = HOURS_HAND
    else:
        HOURS_HAND =  HOURS_HAND - 12
    ANGLE_OF_HOURS_HAND = ((HOURS_HAND) * 30 + (MINUTES_HAND) * 1 / 2)   # ANGLE MADE BY HOURS HAND IN CLOCK
    ANGLE_OF_MINUTES_HAND = (MINUTES_HAND) * 6                           # ANGLE MADE BY MINUTES HAND IN CLOCK
    FORMULA = float(ANGLE_OF_HOURS_HAND) - float(ANGLE_OF_MINUTES_HAND)
    if ANGLE_OF_HOURS_HAND > ANGLE_OF_MINUTES_HAND:
        FORMULA = FORMULA
    else:
        FORMULA = -FORMULA
    if FORMULA <= 180:
        print("THE ANGLE BETWEEN HOURS HAND AND MINUTES HAND : ", FORMULA, "DEGREES")
    else:
        print("THE ANGLE BETWEEN HOURS HAND AND MINUTES HAND : ", 360 - FORMULA, "DEGREES")
else:
    print("GIVE VALID HOURS AND MINUTES IN THE INPUT")

# TYPE 2 BY USING DEFAULT FUNCTIONS

def ANGLE():
    HOURS_HAND = int(input("HOURS HAND : "))
    MINUTES_HAND = int(input("MINUTES HAND : "))
    if 1 <= HOURS_HAND <= 24 and 1 <= MINUTES_HAND <= 60:
        if 1 <= HOURS_HAND <= 12:.
            HOURS_HAND = HOURS_HAND
        else:
            HOURS_HAND = HOURS_HAND - 12
        ANGLE_OF_HOURS_HAND = ((HOURS_HAND) * 30 + (MINUTES_HAND) * 1 / 2)   # ANGLE MADE BY HOURS HAND IN CLOCK
        ANGLE_OF_MINUTES_HAND = (MINUTES_HAND) * 6                           # ANGLE MADE BY MINUTES HAND IN CLOCK
        FORMULA = float(ANGLE_OF_HOURS_HAND) - float(ANGLE_OF_MINUTES_HAND)
        if ANGLE_OF_HOURS_HAND > ANGLE_OF_MINUTES_HAND:
            FORMULA = FORMULA
        else:
            FORMULA = -FORMULA
        if FORMULA <= 180:
            print("THE ANGLE BETWEEN HOURS HAND AND MINUTES HAND : ", FORMULA, "DEGREES")
        else:
            print("THE ANGLE BETWEEN HOURS HAND AND MINUTES HAND : ", 360 - FORMULA, "DEGREES")
    else:
        print("GIVE VALID HOURS AND MINUTES IN THE INPUT")
ANGLE()

# TYPE 3 BY USING CLASS

class Input :
    H = int(input("HOURS_HAND: "))
    M = int(input("MINUTES_HAND: "))
    def angle(self,H,M):
        self.H = H
        self.M = M
class angle_between_clock(Input) :
    def Angle(self):
        if 1 <= self.H <= 24 and 1 <= self.M <= 60:
            if 1 <= self.H <= 12:
                self.H = self.H
            else:
                self.H = self.H - 12
            ANGLE_OF_HOURS_HAND = ((self.H) * 30 + (self.M) * 1 / 2)  # ANGLE MADE BY HOURS HAND IN CLOCK

            ANGLE_OF_MINUTES_HAND = (self.M) * 6                      # ANGLE MADE BY MINUTES HAND IN CLOCK
            FORMULA = float(ANGLE_OF_HOURS_HAND) - float(ANGLE_OF_MINUTES_HAND)
            if ANGLE_OF_HOURS_HAND > ANGLE_OF_MINUTES_HAND:
                FORMULA = FORMULA
            else:
                FORMULA = -FORMULA
            if FORMULA <= 180:
                print("THE ANGLE BETWEEN HOURS HAND AND MINUTES HAND : ", FORMULA, "DEGREES")
            else:
                print("THE ANGLE BETWEEN HOURS HAND AND MINUTES HAND : ", 360 - FORMULA, "DEGREES")
        else:
            print("GIVE VALID HOURS AND MINUTES IN THE INPUT")
A = angle_between_clock()
A.Angle()









