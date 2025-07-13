# Instalacja aplikacji

1.
Trzeba zainstalować [git](https://git-scm.com/downloads/win)

2.
Trzeba zainstalować odpowiednią wersje [python](https://www.python.org/downloads/release/python-31011/)


**Uwaga**
Podczas instalacji pamiętaj aby zaznaczyć opcję na dole
<img width="227" height="31" alt="image" src="https://github.com/user-attachments/assets/f9a58d7c-8aa7-474a-8867-28b534193c93" />


4.
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
