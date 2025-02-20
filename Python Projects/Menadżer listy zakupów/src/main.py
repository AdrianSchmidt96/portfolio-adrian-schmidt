import sys
import os

# Dodajemy pełną ścieżkę do folderu 'src', aby Python widział folder 'menu_and_choices'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from menu_and_choices.menu import Menu
from menu_and_choices.first_choice import FirstChoice
from menu_and_choices.second_choice import SecondChoice
from menu_and_choices.third_choice import ThirdChoice

menu = Menu()
menu.logicChoice()