# Lösung von N1A4: Umgang mit DataFrame
# -------------------------------------

# Löse die folgenden Aufgaben und gib das Ergebnis aus.

## gib für `df_grades` alle Einträge aus, die größer sind als 170
display(df_grades.query("size > 170"))

## zeige in `df_football` lediglich den Namen und die Fähigkeiten an
display(df_football["Name"])

## Ändere die Spaltenüberschriften für `df_fruit` in die deutschen Übersetzungen
df_fruit.columns = ["Name", "Anzahl", "Kosten"]
display(df_fruit)

## bestimme den Mittelwert und die Standardabweichung der Spalten `size` und `grade` von `df_grades`
display(df_grades.describe())

## Zeige an, wie die Verteilung an Noten in `df_grades` ist.
display(df_grades.groupby("grade").count())

## Sortiere das DataFrame `df_grades` absteigend nach der Größe
display(df_grades.sort_values("size"))

## ändere den ersten Buchstaben aller Namen in der Spalte `name` in `df_grades` in Großbuchstaben
def cap(word):
    return word.capitalize()

df_grades["name"] = df_grades["name"].apply(cap)
display(df_grades)