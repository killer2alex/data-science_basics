# Lösung von N1A3: Methoden von Series
# ------------------------------------

## gibt die Anzahl aller Werte in `s_mix` aus, die nicht `np.NaN` sind.
print(s_mix.count())

## Gib die Summe aller Werte von `s_int` aus
print(s_float.sum())

## Gib den Durchschnitt und die Standardabweichung von `s_int` aus.
print(s_int.mean(), s_int.std())

## gib alle vorhandenen (eindeutigen) Elemente von `s_int` aus.
print(s_int.unique())

## Gib die 3 größten Werte von `s_float` aus.
print(s_float.nlargest(3))