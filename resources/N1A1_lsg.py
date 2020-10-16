# Lösung von N1A1: Serien erstellen
# ---------------------------------


## Series mit 10 zufällig generierten Zahlen aus dem Bereich von 0 bis 1
s_float = pd.Series(np.random.random(10))

## Series mit 10 Elementen, aus der Menge M = {1,2,3,4,5,6}
s_int = pd.Series([1,5,6,3,2,1,4,5,2,1])

## Series mit 10 unterschiedlichen Vornamen (alles klein geschrieben)
s_string = pd.Series(["alex", "paul", "paula","erika", "jan","karl", "vlad", "franziska", "sabrina", "florian"])

## Series `s_mix` mit 10 Einträgen, in der Zeichenketten, ganze Zahlen und Gleitkommazahlen vorkommen 
s_mix = pd.Series([1,"zwei", 3.0, 4, "fünf", 6.111, "zieben", 8, 9.9999, 10])

## Ausgabe der Series
print(s_float, s_int, s_string, s_mix, sep="\n\n")


# Noch mehr Möglichkeiten Series zu erstellen gibt es hier: https://www.geeksforgeeks.org/creating-a-pandas-series/