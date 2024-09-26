import matplotlib.pyplot as plt
import numpy as np
import mplcursors

max_hours = 13
min_hours = 0
time_passed = np.arange(min_hours, max_hours + 1, 1)
initial_salmonella = 10
initial_e_coli = 20
sickness_threshold = 1000


salmonella_growth = [initial_salmonella]
e_coli_growth = [initial_e_coli]
# Making the Growths ( Salmonella doubles every half hour in optimal surrounding; E coli every 20 minutes)
for i in range(1, len(time_passed)):
    # Each time step is an hour; calculate total intervals for Salmonella and E. coli
    salmonella_growth.append(salmonella_growth[-1] * (2 ** (2)))  # 2 intervals for half an hour in one hour
    e_coli_growth.append(e_coli_growth[-1] * (2 ** (3)))  # 3 intervals for 20 minutes in one hour

print(e_coli_growth, f"\n", salmonella_growth, f"\n", time_passed)
fig, ax = plt.subplots()
line1, = ax.plot(time_passed, e_coli_growth, label="E. Coli", color="blue")
line2, = ax.plot(time_passed, salmonella_growth, label="Salmonella", color="green")

ax.axhline(y=sickness_threshold, color='red', linestyle='--', label="Sickness threshold (1000 Bacteria)")

ax.set_yscale("log")

plt.title("Growth of E. Coli and Salmonella in cooked Chicken over Time!")
plt.xlabel("Time passed in Hours")
plt.ylabel("Amount of Bacteria")

plt.legend()
plt.grid(True)

mplcursors.cursor([line1, line2], hover=True).connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()}: {sel.target[1]:.2f}'))

plt.show()