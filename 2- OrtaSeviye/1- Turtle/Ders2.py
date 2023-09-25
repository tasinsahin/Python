# ------------------------------------------------------------------
# Yönerge:
# https://pypi.org/project/prettytable/
# https://pokemondb.net/pokedex/game/x-y
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
# pypi.org
# pip install prettytable
# Çıktı:
# Uygulama:

from prettytable import  PrettyTable
table  = PrettyTable()
table.add_column("Pokemon Adı",["Pikachu", "Squirtle","Charmender"])
table.add_column("Tipi",["Elektrik", "Su","Ateş"])
table.add_column("Pokemon Adı",["Pikachu", "Squirtle","Charmender"])
table.align="l"
print(table)
 # ------------------------------------------------------------------


