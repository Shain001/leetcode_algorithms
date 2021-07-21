a0 = (400000 * 700 * 2.354) / (22164 * 43000000 * 4)
Fcity = 41.5546/29
Fhwy = 38.6013/35
Pcity, Phwy = 0, 0
HONDA_Cd = 0.325
HONDA_Af = 2.3
HONDA_Cr = 1.75
HONDA_c1 = 0.0328
HONDA_c2 = 4.575
HONDA_ACC = 3.75
HONDA_MASS = 1469

G = 9.8
DRIVEN_EFFICIENCY = 0.9
AIR_DENSITY = 1.2256
a = 1.1
cr = HONDA_Cr
c1 = HONDA_c1
c2 = HONDA_c2
cd = HONDA_Cd
m = HONDA_MASS
af = HONDA_Af
Tcity = 1875
Thwy = 766
v = 0
for i in range(1875):
    if v < 25:
        v += a
    Pcity += ((m * (a) + (m * G * cr / 1000) * (c1 * v + c2) + 0.5 * AIR_DENSITY * af * cd * v * v + m * G * 0) * (v / (1000 * DRIVEN_EFFICIENCY)))

v2 = 0
for i in range(766):
    if v2 < 25:
        v2 += a
    Phwy += ((m * (a) + (m * G * cr / 1000) * (c1 * v + c2) + 0.5 * AIR_DENSITY * af * cd * v * v + m * G * 0) * (v / (1000 * DRIVEN_EFFICIENCY)))

P2city = Pcity * Pcity
P2hwy = Phwy * Phwy

a2 = ((Fcity-Fhwy*(Pcity/Phwy)) - (Tcity-Thwy*Pcity/Phwy)*a0)/(P2city-P2hwy*(Pcity/Phwy))
a1 = (Fhwy-Thwy*a0 - P2hwy*a2)/Phwy

print("a0: " + str(a0) + " a1: " + str(a1) + " a2: " + str(a2))