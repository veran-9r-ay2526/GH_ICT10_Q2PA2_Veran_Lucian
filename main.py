# Practical Activity 2
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ' '

    # Variables
    f_name = document.getElementById('fname').value.title().strip()
    l_name = document.getElementById('lname').value.title().strip()
    grade_7 = {'Walter White', 'Jesse Pinkman', 'Gustavo Fring', 'Saul Goodman', 'Lalo Salamanca', 'Tuco Salamanca', 'Mike Ehrmantraut'}
    grade_8 = {'Mark Grayson', 'Nolan Grayson', 'Cecil Stedman', 'Angstrom Levy', 'David Anders', 'Thragg', 'Conquest', 'Allen the Alien'}
    grade_9 = {'Kasli the Bane', 'Lasvoss the Ultimate', 'Kratos, the God of War', 'Wargod Mitsuhide', 'Dragon Emperor Daliasan', 'Lightmother Aset'}
    grade_10 = {'Mark Fischbach', 'Sean Mcloughlin', 'Rhett Mcloughlin', 'Link Neal', 'Albert Aretz', 'Cory Williams', 'Dontai Ethridge', 'Hamzah Al-Emad', 'Martin Andrijasevic'}
    # Combining the sets
    super_set = grade_7 | grade_8 | grade_9 | grade_10
    # Combining the name
    full_name = f_name + " " + l_name
    # Adding the given name
    super_set.add(full_name)

    display(super_set, target="div1")
    display(len(super_set), target="div1")