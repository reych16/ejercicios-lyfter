class Computer:

    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
        self.is_on = False
        print(f'Computer {self.brand} created whit {self.ram} RAM.')
    

    def turn_on(self):
        self.is_on = True
        print(f'The computer {self.brand} is now ON.')
    

    def turn_off(self):
        self.is_on = False
        print(f'The computer {self.brand} has been turned OFF.')


class GamerFeatures:

    def activate_gaming_mode(self):
        print('Gaming mode activated.')
    
    def show_fps(self):
        print('FPS: 144')


class GamingLaptop(Computer, GamerFeatures):

    def __init__(self, brand, ram, gpu):
        super().__init__(brand, ram)
        self.gpu = gpu
        print(f'Gaming laptop ready whit GPU: {self.gpu}')


laptop = GamingLaptop('ASUS', '16GB', 'NVIDIA RTX 4060')

laptop.turn_on()
laptop.activate_gaming_mode()
laptop.show_fps()
laptop.turn_off()
