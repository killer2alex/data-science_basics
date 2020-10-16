# Lösung von N1A2: Eigenschaften von Serien
# -----------------------------------------

## Gib die Anzahl an Elementen in `s_float` zurück.
print(s_float.size)

## überprüfe, ob `s_mix` und `s_string` den selben Datentyp besitzen
print(s_mix.dtype == s_string.dtype)

## gibt die Werte von `s_string` als Liste zurück
print(s_string.values)

## setze den index von von `s_int` auf `s_string`
s_int.index = s_string
print(s_int)

## setze den 4. Wert von `s_string` auf 'noname'
s_string[3] = 'noname'
print(s_string)'

## stetze den 10. Wert von `s_max` auf `np.NaN`
# Hinweis: `np.NaN` steht für "Not a Number" und wird häufig für fehlende oder fehlerhafte Werte verwendet
s_mix[9] = np.NaN
print(s_mix)