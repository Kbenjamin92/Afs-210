from enum import Enum

class States(Enum):
    New_Jersey = 200
    New_York = 400
    Virginia = 150
    Califorina = 500
    Florida = 350
    North_Carolina = 170

for data in States:
    print(f'{data.name} = {data.value}')