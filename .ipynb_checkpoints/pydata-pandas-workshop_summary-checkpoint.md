

# Das Notebook erklären (0)
    verschiedene Zellen:
        Markdown
            - stellt ähnlich zu HTML eine Markoutlanguae dar und kann zu Erklärungen, Dokumentierung und Strukturierung genutzt werden.
        Code
            - Das letzte in der Zeil wird automatisch ausegegeben --> können uns print sparen
            - mit ";" kann eine Ausgabe verhindert werden
        Output
    Shortcuts:
        ESC + m : Markdown-Zelle erstellen
        SHIFT + RETURN : Zelle ausführen und neue erstellen
        STRG + RETURN : Zelle ausführen
    InCell action:
        ? : Hilfemenü
        %<Magic> : 
            %timeit : ermöglicht das messen von Zeit, wie lange die Zelle für die Ausführung braucht
            %load : lädt Code aus einer Datei in das Notebook
            %run : führt ein Python-Skript aus
            %store (-r) : speichert (und lädt) Daten zur Verarbeitung 
        ! <Shell-Befehle> : Einen (odere mehrere) Shellbefehle ausführen

# Daten lesen und schreiben (1)
    Code den ich brauche
        ```
        import pandas as pd  # pandas importieren 
        %pwd  # momentanes Verzeichnis anzeigen
        %ls  # Verzeichnis betrachten
        
        pd.read_excel('../data/blooth_sales_data.xlsx', usecols='A:B')  # mit Excel-Dateien arbeiten (für das exportieren --> https://xlsxwriter.readthedocs.io/
        
        pd.read_csv('<path>')  # CSV einlesen
        parse_dates=['birthday', 'orderdate']  # es gibt verschiedene Möglichkeiten zu sagen, was die Daten eig. sein sollen
        sep=';', decimal=','  # es kann mit sep und decimal eingestellt werden, was als Seperator und was als Dezimalstelle verwendet wird
        
        pd.read_json(...)  # Json einlesen .auf formatierung der Dataframes achten!
        datetime.datetime.strptime(j['orderdate'], "%Y-%m-%d %H:%M:%S.%f")  # erstellt "ordentliches Date-Object 

    Daten exploration
        pandas Einstellungen
            ```
            pd.set_option('display.max_rows', 10000) : verändert
            die mögliche Anzahl, an Reihen, die gezeigt werden
            ```
        string = object in Pandas
        pandas Code zur exploration
        ```
            <dataframe>.head(x)  # gibt die ersten x Zeilen des Dataframes an
            <dataframe>.tail(x)  
            <dataframe>.info()  # gibt Infos über die Objekte im Dataframe an
            <dataframe>.describe()  # gibt nähere Informationenn über alle Numerischen Werte (Min, Max, Median)
            sales_data = pd.read_csv('../data/blooth_sales_data.csv', parse_dates=['birthday','orderdate'])  # es gibt verschiedene Möglichkeiten zu sagen, was die Daten eig. sein sollen 
            # es kann mit sep und decimal eingestellt werden, was als Seperator und was als Dezimalstelle verwendet wird

Daten Auswahl und Indexing (2)
    pd.IndexSlice[:, 2]: Einen Bereich in Abhängigkeit des Indexes (x-Achse) nehmen
    
    #Konzept Dataframe: stellt eine Matrix mit ihren Einträgen dar
        Zeilen: 0-Axis
        Spalten: 1-Axis
        .style.apply : Teile des Dataframes markieren
        .display(...): Anwendung von Style auf einen Bereich oder das ganze Frame.
        df[x]: Damit wird eine Spalte ausgewählt
        df[x:y]: damit wird eine Zeile ausgewählt
        df.iloc[r1:r2,c1:c2]: integer locationgeber
        df.at[1,"rrt"]: einzelner Wert anstelle von loc
        df[list_of_column_indexes] : damit wird nur der Teil der Spalten angegeben, die das Kriterium erfüllen
        df.index = list :Index wird mit der Liste ersetzt
        df.columns = list : Spalten Namen werden mit Liste ersetzt
        df.loc[r1:r2,c1:c2]: Localisation mit den echten Namen der Zeilen und Spalten
        .len(): gibt Anzahl an Reihen an
        .head(x) : gibt die ersten Einträge des Dataframes aus
        .tail(x) : gibt die letzten Einträge des Dataframes aus
        .style
            .highlight_min(): kleinstes Element zeigen in jeder Spalte
            .apply(function): wird auf eine einzelne Zeile übergeben https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.apply.html

    #Konzept Series: stellt eine einzige Spalte (und ihre Einträge) dar (kann mit einer Liste erstellt werden und ist mit ihr vergleichbar)
        zugriff mittels Position oder Slice: genau wie bei einer Liste ist es möglich mittels `series[0]` oder `series[3:6]` zu arbeiten. Ist das selbe wie `series.iloc[3:6]` dabei werden [] und nicht () verwendet 
        zugriff mittels Label:
            einer Serie ein label zuordnen: mit der index Funktion kann einer Serie ein Label zugeordnet werden. `series.index = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"][:len(series)]`
            Über ein Label auf eine Serie zugreifen: mittels `series[D]` und series[D:F] (end ist mit enthalten) Dabei kann auch `loc()` verwendet werden.
        mehrere Serien kombinieren: Serien können mit der `pd.concat()` Funktion kombiniert werden pd.concat([series['D':'F'], series['I':'J']])

    Boolean Indexes
        verwendet für: das Filtern und auswählen von Daten
        df[x] > 60 : erzeugt Serie mit Boolean-Werten
        df [boolean-filter]: filtert Einträge nach den Filterwerten
        &: und 
        |: oder

    Filter mittels df.filter(filter_option, axis) 
        verändert nicht den Inhalt eines Dataframes, sondern nur die Labels des Dataframes 
        default ist die Spalten (1-Axis) (1) als Filter
        mögliche Filteroptionen
            like
            regex


# Veränderungen auf Dataframes (3)
    Manipulation von Dataframes
        Spalte hinzufügen : `<dataframe>[name_der_neuenZeile]= <list>  aufpassen, soll eine Serie hinzugefügt werden, müssen die Indizies abgestimmt werden 
        Spalte entfernen : `del <dataframe>[name_der_neuen_Zeile]` oder, um Fehler zu ignorieren `df.drop(['C12'], errors='ignore')`
      
        es können alle Numpy Operationen verwendet werden um neue Daten zu erzeugen:
        `sales_data['turnover'] = sales_data['unitprice'] * sales_data['units']`
    <datafram>[index].mean(), .sum(), .median()
    Funktionen und `series.map()`, `df.apply`, `df.applymap()
        series.map(x)  # mapped jeden Wert der Serie,des Dicts oder der Funktion x auf die Elemente der Serie series von der es ausgeführt wird
            Funktionen müssen für die Elemente der Serie series ausgerichtet sein.
        df.apply(): führt eine Funktion auf jede Spalte/Zeile eines Dataframes aus. default ist Spalte
        df.applymap(): führt eine Funktion auf jedes Element eines Dataframes aufs
        Dabei wird immer nur eine Kopie erstellt. das Dataframe selbst bleibt unberührt
    Mit NaN arbeiten
        series.isnull() übergibt alle Einträge bei denen NaN vorkommen. None und np.NaN --> True. Der Rest False '' und np.inf zählen nicht
        series.notna() gegenteil von isnull
        series.dropna() entfernt alle NaN Werte
        df/series.fillna(x) : ersetzt alle NaN-Werte mit x oder was man will
# Visualisierung (4.)

    benutzen matplotlib für einfache visualisierung (für andere kann Seaborn verwendet werden)
        import Code:
            ```python
            import matplotlib.pyplot as plt
            # nicht notwendig plt.style.use('default')
            %matplotlib inline  # damit es inline angezeigt wird
            ```
        Code für Diagramme
            ```python
            dataframe.plot()  # automatische Interaktion mit
            Matplotlib von Pandas
            dataframe.plot.hist(bins=15)
            dataframe.plot.bar()
            ```
        Zusatzinformationen
            standard ist linechart
            es können noch andere Parameter übergeben werden:
                figzize=(x,y)
                title= "title des Diagramms"
                legend=True
                    fontsize= 14
                colormap = "color"
                grid=True
                linestyle = '--'
                ...
            wenn ich das Plot an ein ax übergebe, kann ich noch andere Sachen mit einfügen Bsp.:
                Linien
                Pfeile
                Text   

    df.groupby("category") und df.groupby(list) kann ich nach gewissen Ausprägungen von Items gruppieren
        ist sehr möchtig und ermöglicht das erstellen von Multiindexen

## Daten aggregation
  was heißt das?: Daten aus mehreren Datenbanken besorgen und verbinden/kombinieren
  sort_values("kategorie, ascending=False)
  Was bedeuten die Funktionen agg()?
  mit Pivoting können große Datenmengen nach bestimmten Kriterien zusammengefasst werden und dafür gibt es pd.pivot_table(...)
  melt-Befehl um Daten mit mehreren Dimensionen zu Daten mit weniger Dimensionen zur erstellen
  Merge von mehreren Datensätzen
    Möglichkeit 1: als Spalte einfach hinzufügen
      dabei einfach eine neue Serie erstellen und diese dann hinzufügen.
      Alle Daten der Serie bleiben erhalten, auch wenn nur die zu sehen sind,
      die sie sich mit den anderen teilt
    Möglichkeit 2: Inner Join
    Möglichkeit 3: Outer Join

## Scaling Performance - Optimierung

# Notes


alles was nicht anders betitelt ist, ist ein Dataframe