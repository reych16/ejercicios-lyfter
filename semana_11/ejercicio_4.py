class Head:
    def __init__(self):
        self.eyes = 2
        self.mouth = 1
        self.nouse = 1

class Hand:
    def __init__(self):
        self.fingers = 5

class Feet:
    def __init__(self):
        self.toes = 5

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Torso:
    def __init__(self, head, left_arm, rigth_arm, left_leg, rigth_leg):
        self.head = head
        self.left_arm = left_arm
        self.rigth_arm = rigth_arm
        self.left_leg = left_leg
        self.rigth_leg = rigth_leg

class Human:
    def __init__(self, torso):
        self.torso = torso

    def describe(self):
        print("Este humano tiene: ")
        print(f'- {self.torso.head.eyes} ojos')
        print(f'- {self.torso.left_arm.hand.fingers} dedos en la mano izquierda')
        print(f'- {self.torso.rigth_leg.foot.toes} dedos en el pie derecho')

left_hand = Hand()
rigth_hand = Hand()
left_foot = Feet()
rigth_foot = Feet()

left_arm = Arm(left_hand)
rigth_arm = Arm(rigth_hand)
left_leg = Leg(left_foot)
rigth_leg = Leg(rigth_foot)

head = Head()

torso = Torso(head, left_arm, rigth_arm, left_leg, rigth_leg)

human = Human(torso)

human.describe()