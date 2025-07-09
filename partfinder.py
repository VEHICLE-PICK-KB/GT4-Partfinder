import pandas as pd;

def y_otsikko(teksti, leveys=30):
    return teksti.ljust(leveys)

otsikot = {
    'Chassis': "Chassis",
    'Suspension': "Suspension",
    'Drivetrain': "Drivetrain",
    'Increase Rigidity': "Increase Rigidity",
    'Engine': "Engine",
    'Exhaust': "Exhaust",
    'Nitrous Oxide': "Nitrous Oxide",
    'Turbocharger': "Turbocharger",
    'Transmission': "Transmission",
    'LSD': "LSD",
    'Brakes': "Brakes",
    'Tires Front': "Tires Front",
    'Tires Rear': "Tires Rear"
}

running = True


while running == True:
    car_name = input("Car name: ")

    tiedostot = [
        r'C:\Users\matia\Desktop\01 - Chassis, Susp, DriveT.xls',
        r'C:\Users\matia\Desktop\02 - Engine & Parts.xls',
        r'C:\Users\matia\Desktop\03 - Transmission & Parts.xls',
        r'C:\Users\matia\Desktop\04 - Brake & Controller.xls',
        r'C:\Users\matia\Desktop\05 - Tires.xls'
    ]

    for tiedosto in tiedostot:
        xls = pd.ExcelFile(tiedosto, engine='xlrd')
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name, header=2, engine='xlrd')
            mask = df.apply(lambda r: r.astype(str).str.contains(car_name, case=False, na=False).any(), axis=1)
            tulokset = df[mask]
            if not tulokset.empty:
                tulokset = tulokset.dropna(how='all', axis=0)
                tulokset = tulokset.dropna(how='all', axis=1)
                otsikko = otsikot.get(sheet_name, sheet_name)
                print("\n\n"+y_otsikko(otsikko)+"\n")
                print(tulokset.to_string(index=False, header=False))
    selection = input("Quit?")
    if selection == 'y':
        running = False
    else:
        continue