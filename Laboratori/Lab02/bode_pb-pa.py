import math

files = ["passabasso.txt", "passaalto.txt"]

for filename in files:    
    list = []
    file = open(filename, "r")
    
    line_split = file.readline().split(" ")
    R = float(line_split[0])
    C = float(line_split[1])
    ts = float(line_split[2])
    
    print("--- ", filename, " ---")
    print("Specifics = ")
    print("\tR = ", R, "\n\tC = ", C, "\n\tts = ", ts)
    ft = round(1 / (2 * math.pi * R * C), 2)
    print("\tFreq Taglio = ", ft)
    tau = round(ts / (0.35 * 2 * math.pi), 10)
    print("\tTau = ", tau)
    ftm = round(1 / (2 * math.pi * tau), 2)
    print("\tFreq Taglio (mis) = ", ftm, "\n")
    
    for line in file:
        line_split = line.split(" ")
        freq = float(line_split[0])
        Vin = float(line_split[1])
        Vout = float(line_split[2])
        list.append({"freq": freq, "Vin": Vin, "Vout": Vout})
    
    for element in list:
        dBValue = round(20 * math.log(element["Vout"] / element["Vin"], 10), 2)
        print("Freq = ", element["freq"], "\n\tdB Value = ", dBValue, "\n")
    
    file.close()
