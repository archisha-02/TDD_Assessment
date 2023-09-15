import unittest

class Chandrayaan3:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move(self, command):
        if command == 'f':
            if self.direction == 'N':
                self.y += 1
            elif self.direction == 'S':
                self.y -= 1
            elif self.direction == 'E':
                self.x += 1
            elif self.direction == 'W':
                self.x -= 1
            elif self.direction == 'Up':
                self.z += 1
            elif self.direction == 'Down':
                self.z -= 1
        elif command == 'b':
            if self.direction == 'N':
                self.y -= 1
            elif self.direction == 'S':
                self.y += 1
            elif self.direction == 'E':
                self.x -= 1
            elif self.direction == 'W':
                self.x += 1
            elif self.direction == 'Up':
                self.z -= 1
            elif self.direction == 'Down':
                self.z += 1

    def rotate(self, command):
        directions = ['N', 'E', 'S', 'W', 'Up', 'Down']
        current_idx = directions.index(self.direction)
        
        if command == 'l':
            self.direction = directions[(current_idx - 1) % 6]
        elif command == 'r':
            self.direction = directions[(current_idx + 1) % 6]

    def execute_commands(self, commands):
        for command in commands:
            if command in ['f', 'b']:
                self.move(command)
            elif command in ['l', 'r']:
                self.rotate(command)
            elif command in ['u', 'd']:
                self.rotate(command)

        return (self.x, self.y, self.z), self.direction

class TestChandrayaan3(unittest.TestCase):
    def test_move_forward(self):
        chandrayaan = Chandrayaan3(0, 0, 0, 'N')
        chandrayaan.move('f')
        self.assertEqual(chandrayaan.execute_commands([]), ((0, 1, 0), 'N'))

    def test_rotate_left(self):
        chandrayaan = Chandrayaan3(0, 0, 0, 'N')
        chandrayaan.rotate('l')
        self.assertEqual(chandrayaan.execute_commands([]), ((0, 0, 0), 'W'))

    # Add more test cases for other methods as needed

if __name__ == "__main__":
    unittest.main()
