class Buttons:

    def __init__(self, buttons_dict=None):
        self.init_buttons()
        if buttons_dict is not None:
            self.dict_to_object(buttons_dict)

    def init_buttons(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.Y = False
        self.B = False
        self.X = False
        self.A = False
        self.L = False
        self.R = False

    def reset(self):
        """Reset all button states to False."""
        self.init_buttons()

    def dict_to_object(self, buttons_dict):
        self.up = buttons_dict.get('Up', False)
        self.down = buttons_dict.get('Down', False)
        self.left = buttons_dict.get('Left', False)
        self.right = buttons_dict.get('Right', False)
        self.Y = buttons_dict.get('Y', False)
        self.B = buttons_dict.get('B', False)
        self.X = buttons_dict.get('X', False)
        self.A = buttons_dict.get('A', False)
        self.L = buttons_dict.get('L', False)
        self.R = buttons_dict.get('R', False)

    def object_to_dict(self):
        return {
            'Up': self.up,
            'Down': self.down,
            'Left': self.left,
            'Right': self.right,
            'Y': self.Y,
            'B': self.B,
            'X': self.X,
            'A': self.A,
            'L': self.L,
            'R': self.R
        }