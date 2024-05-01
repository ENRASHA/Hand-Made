std={
    "ali b.":{"phy1":80,"ma2":90},
    "aishe g.":{"phy1":78,"ma2":89},
    "nur d.":{"phy1":60,"ma2":76},
    "mehmet c.":{"phy1":100,"ma2":84},
    "usama h.":{"phy1":98,"ma2":90},
    "hamza k.":{"phy1":70,"ma2":80},
    "farouk t.":{"phy1":67,"ma2":73},
    "deniz a.":{"phy1":99,"ma2":91},
    "yasmine r.":{"phy1":87,"ma2":100},
    "ahmet s.":{"phy1":93,"ma2":91},
    }
print("std name,  grade of phy1,  grade of ma2")
for std, grade in std.items():
    print(f"({std}):  {grade["phy1"]}, {grade["ma2"]}")
    

         

