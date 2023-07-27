from pip import *
import random, tkinter, time

base = None
#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("Rebondir.py", base=base)]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
        'random':random,
        'tkinter':tkinter,
        'time':time
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Rebondir Jeu",
    options = options,
    version = "1.0",
    description = 'Je vous présente Rebondire le jeu de raquette si connu',
    executables = executables
)
