# +---------------------------------------------------------+
# | Single Responsibility Principle | Seperation of Concerns|
# +---------------------------------------------------------+

# SSRP -  Serperation of Concerns

# If you have a class, it should have a primary responsibilities and should not take any
# irrelevant responsibilities

# - Dont overload your program with too many responsibilities
# - Single responsibilty principle will actually avoid anti pattern which is nothing but
# putting too many things in the kitchen sink!

# In the below code, we could understand that different relevent functionalities
# are grouped and seperated based on the purpose they make. So its essential that the
# class should have a single responsibility.


class Journal:
    def __init__(self):
        self.enteries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.enteries.append(f'{self.count}:{text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.enteries)


class HandlePersistance:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


first_log = Journal()
first_log.add_entry("Started Design Patterns")
first_log.add_entry("Nobody Eats a bug")
print(f'Journal Entries:\n{first_log}')

# The Seperation of concerns seperates different functionalities in code

# So the save function is added here seperately to persist the data which is a
# implementation of persiting the data.
print("========================================")
print("The below is an output from reading file")
print("========================================")
file = r'journals.txt'
HandlePersistance.save_to_file(first_log, file)

with open(file) as fh:
    print(fh.read())
