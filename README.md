# Instalacja aplikacji

1.
Trzeba zainstalować [git](https://git-scm.com/downloads/win)

2.
Trzeba zainstalować odpowiednią wersje [python](https://www.python.org/downloads/release/python-31011/)

3.
kopiujemy plik komendą
```
git clone https://github.com/doktorb42/App.git
```
Następnie wchodzimy w folder
```
cd App
```

4.
Tworzymy środowisko
```
py -3.10 -m venv venv
```
i następnie wchodzimy w nasze utworzone środowisko
```
.\venv\Scripts\activate.bat
```

5.
Instalujemy potrzebne biblioteczki
```
pip install -r requirements.txt
```
i możemy odpalić grę
```
python main.py
```
