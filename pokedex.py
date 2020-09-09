import csv

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np


num = None

while num != "exit":

    num = input("Let me know the number of the Pokemon you want to see his information\nIf you want to close the Pokedex enter: exit\n")

    try:
        num = int(num)
    except:
        if num != "exit":
            print("The input must be a number\n")
    else:

        with open('database.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)

            try:
                infoPokemon = [row for idx, row in enumerate(csv_reader) if idx in [num]]
                imagePokemon = infoPokemon[0][5]
            except:
                print("There is no Pokemon in the Pokedex with this number sorry\n")

            else:

                img=mpimg.imread(imagePokemon)
                imgplot = plt.imshow(img)
                plt.axis('off')
                plt.text(0.02, 0.5, infoPokemon[0][2], fontsize=14, transform=plt.gcf().transFigure)
                plt.text(0.02, 0.4, "Evol. " + infoPokemon[0][3]+"/"+infoPokemon[0][4], fontsize=14, transform=plt.gcf().transFigure)

                plt.subplots_adjust(left=0.3)

                title = plt.title("Nº " + infoPokemon[0][0] + " " + infoPokemon[0][1])
                plt.setp(title, color='black', fontsize=14, fontweight='bold')
                plt.show()



print("Goodbye!")
