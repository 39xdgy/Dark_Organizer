class item:
    def __init__(self, contect, important_level, process_state, color, due_date):
        self.contect = contect
        self.IL = important_level
        self.PS = process_state
        self.color = color
        self.DD = due_date

    def change_contect(self, new_contect):
        self.contect = new_contect

    def return_contect(self):
        return self.contect

    def change_level(self, new_level):
        self.IL = new_level

    def return_level(self):
        return self.IL

    def change_PS(self, new_process_state):
        self.PS = new_process_state

    def return_PS(self):
        return self.PS

    def change_color(self, new_color):
        self.color = new_color

    def return_color(self):
        return self.color

    def change_DD(self, new_date):
        self.DD = new_date

    def return_DD(self):
        return self.DD

    def string_form(self):
        return str(self.contect) + ", " + str(self.IL) + ", " + str(self.PS) + ", " + str(self.color) + ", " + str(self.DD)

    
    def write_file(self, file_name):
        txt = open(file_name, "a")
        txt.write(self.string_form() + "\n")
        txt.close()

