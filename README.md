# Offline bank application for your financial calculations


# Descriptions available in Turkish, English, German, and Italian:


# Türkçe:

Bu uygulamanın amacı 3 farklı parabiriminde bir banka similasyonu oluşturup hesapları rahat ve görünür şekilde yapabilmektir.

Kodları kendinize göre düzenleyip istediğiniz oranları kullarak gerçek hayattaki bankanızda işlem yapmadan önce hesabınızı yönetebilirsiniz.
Bu sayede ise hem harcamalarınızı daha ölçekli tutup hemde kendinizi ekonomik anlamda olacaklara hazırlayabilirsiniz.

Eğer doviz.py # Yani TRY/USD/EUR dönüşümlerinin yapıldığı modül # API key hatası verirse diye kodun içine yedek API key ekledim.
Yedek API key kullanmanız sonucunda da API key hatası veriyorsa telaş etmeyin yapmanız gereknler çok basit

Fixer.io sitesine gidin ve ücretsiz bir hesap oluşturun. İsteğe bağlı ücretli hesaplarada göz atabilirsiniz.
Hesabınızda dashboarda size tanımlı olan API key olacak.
Onu alın ve kodda bulunan API key ile değiştirin.
Bu sayede sorun çözülmüş olacak. (İşin güzel tarafı artık sadece sizin kullanacağınız bir API key elde etmiş oldunuz.)

API key aktifleştirme işlemini başarılı bir şekilde yapamadıysanız basit bir internet araması ile sorunu kolayca çözeceğinizden eminim.

Uygulamayı kullandığınız için teşekkür ederim. Umarım finansal anlamda işinize yaramıştır :)
# Uygulamadaki dosyalar ve işlevleri:
bank_balance.py = Bankanın kasasında bulunan parayı veritabanı oluşturup kaydetmeyi ve diğer banka kasasında bulunan bakiyelerle ilgili işlemlerin kodlarını içerir.

choosemoney = Parabirimi seçmeniz ve kodun seçtiğiniz parabirimine göre çalışması için gerekli olan kodları içerir.

doviz.py = İnternetten parabirimleri arasındaki fiyat hepsalama işlemleri için gerekli kodları içerir.

faiz.py = Faiz işlemleri hesaplamak için gerekli kodları içerir.

kumar.py = Şans oyunları için gerekli kodları içerir.

lang.py = Dil değiştirmek için gerekli kodları içerir.

library.py = Dil değiştirdikten sonra yazıların çevirileceği dildeki karşılığını ekrana yazdırmak için gereken sözlük yapısındaki modüldür.

main.py = Kullanıcı girişi, kullanıcı kaydı, para işlemleri, ve tüm fonksiyornları çalıştırıp kendi içlerindeki denetimler dışında da denetleyen menu fonksiyonunu içeririr.

money_transfer = Para transfer işlemleri için gerekli kodları içerir. Kendi hesaplarınız arasında dahi para transferi yapabilirsiniz. Güncel kur hesaplanıp ona göre yansıyacaktır.

user.py = Kayıt olma, giriş yapma, hesap oluşturma gibi daha birçok işlemin yapılması için gereken fonksiyonlar için ayrılmış bir bölümdür.


# English:
The purpose of this application is to create a bank simulation in three different currencies, making calculations easy and visible.

You can adjust the code as you like and manage your finances using the exchange rates you prefer before making any transactions with your real bank. This way, you can keep your expenses more measured and prepare yourself for possible economic scenarios.

If you encounter an API key error in the doviz.py module (where TRY/USD/EUR conversions are handled), I have added a backup API key inside the code. If you still get an API key error after using the backup key, don't worry. The solution is very simple.

Go to the Fixer.io website and create a free account. You can also check out the paid options if you want. In your account dashboard, you will find your assigned API key. Copy it and replace the one in the code. This will resolve the issue. (The great part is that now you have an API key that only you can use!)

If you are unable to activate the API key successfully, I'm confident you can resolve the problem with a quick internet search.

Thank you for using this application. I hope it has been helpful to you financially! :)
# Files and Functions in the Application:

bank_balance.py: Contains the code for creating and storing a database of the money in the bank's vault, as well as for handling operations related to the balances in other bank vaults.
choosemoney: Contains the code necessary for selecting the currency and making sure the code works according to the selected currency.
doviz.py: Contains the code for retrieving exchange rates between currencies from the internet.
faiz.py: Contains the code for calculating interest operations.
kumar.py: Contains the code for games of chance.
lang.py: Contains the code for changing languages.
library.py: Contains the dictionary-like structure needed to display translations in the language selected after changing it.
main.py: Contains the functions for user login, user registration, money transactions, and running all functions, including checks beyond their internal controls.
money_transfer: Contains the code for money transfer operations, allowing transfers even between your own accounts. The current exchange rate will be calculated and reflected accordingly.
user.py: Contains the functions needed for operations such as registration, login, account creation, and more.


# German:
Zweck dieser Anwendung ist es, eine Bankensimulation in drei verschiedenen Währungen zu erstellen, um Berechnungen einfach und übersichtlich zu gestalten.

Du kannst den Code nach Belieben anpassen und deine Finanzen mit den gewünschten Wechselkursen verwalten, bevor du Transaktionen mit deiner realen Bank durchführst. Auf diese Weise kannst du deine Ausgaben besser im Blick behalten und dich auf mögliche wirtschaftliche Entwicklungen vorbereiten.

Falls im doviz.py Modul (wo TRY/USD/EUR-Konvertierungen durchgeführt werden) ein API-Schlüssel-Fehler auftritt, habe ich einen Backup-API-Schlüssel im Code eingefügt. Falls nach der Verwendung des Backup-Schlüssels immer noch ein API-Schlüssel-Fehler auftritt, keine Sorge – die Lösung ist ganz einfach.

Besuche die Website Fixer.io und erstelle ein kostenloses Konto. Optional kannst du auch die kostenpflichtigen Optionen anschauen. Im Dashboard deines Kontos findest du deinen zugewiesenen API-Schlüssel. Kopiere diesen und ersetze den im Code vorhandenen Schlüssel. Dadurch wird das Problem gelöst. (Das Tolle daran ist, dass du jetzt einen API-Schlüssel hast, den nur du verwenden kannst.)

Solltest du den API-Schlüssel nicht erfolgreich aktivieren können, bin ich sicher, dass du das Problem mit einer schnellen Internetsuche leicht lösen kannst.

Vielen Dank, dass du diese Anwendung nutzt. Ich hoffe, sie hat dir finanziell geholfen! :)

# Dateien und Funktionen in der Anwendung:

bank_balance.py: Enthält den Code zum Erstellen und Speichern einer Datenbank des Geldes im Bankschließfach sowie zur Verwaltung von Operationen, die mit den Kontoständen in anderen Bankschließfächern zusammenhängen.
choosemoney: Enthält den Code, der erforderlich ist, um die Währung auszuwählen und sicherzustellen, dass der Code gemäß der ausgewählten Währung funktioniert.
doviz.py: Enthält den Code zum Abrufen von Wechselkursen zwischen Währungen aus dem Internet.
faiz.py: Enthält den Code zur Berechnung von Zinsoperationen.
kumar.py: Enthält den Code für Glücksspiele.
lang.py: Enthält den Code zum Ändern der Sprache.
library.py: Enthält die dictionary-ähnliche Struktur, die benötigt wird, um Übersetzungen in der nach dem Wechsel ausgewählten Sprache anzuzeigen.
main.py: Enthält Funktionen für die Benutzeranmeldung, Benutzerregistrierung, Geldtransaktionen und zum Ausführen aller Funktionen, einschließlich der Überprüfungen über die internen Kontrollen hinaus.
money_transfer: Enthält den Code für Geldtransaktionsoperationen, einschließlich Überweisungen zwischen eigenen Konten. Der aktuelle Wechselkurs wird berechnet und entsprechend berücksichtigt.
user.py: Enthält die Funktionen, die für Operationen wie Registrierung, Anmeldung, Kontoerstellung und mehr erforderlich sind.


# Italian:
Lo scopo di questa applicazione è creare una simulazione bancaria in tre diverse valute, rendendo i calcoli facili e visibili.

Puoi adattare il codice come preferisci e gestire le tue finanze utilizzando i tassi di cambio desiderati, prima di effettuare transazioni con la tua banca reale. In questo modo, potrai mantenere le tue spese più sotto controllo e prepararti a possibili scenari economici.

Se incontri un errore della chiave API nel modulo doviz.py (dove vengono gestite le conversioni TRY/USD/EUR), ho aggiunto una chiave API di backup all'interno del codice. Se ricevi ancora un errore dopo aver usato la chiave di backup, non preoccuparti: la soluzione è molto semplice.

Vai sul sito Fixer.io e crea un account gratuito. Se vuoi, puoi anche dare un'occhiata alle opzioni a pagamento. Nel tuo account, nel dashboard, troverai la chiave API assegnata. Copiala e sostituisci quella presente nel codice. Questo risolverà il problema. (La parte migliore è che avrai una chiave API che solo tu potrai usare!).

Se non riesci ad attivare correttamente la chiave API, sono sicuro che con una semplice ricerca su internet risolverai facilmente il problema.

Grazie per aver utilizzato questa applicazione. Spero che ti sia stata utile dal punto di vista finanziario! :)

# File e Funzioni nell'Applicazione:

bank_balance.py: Contiene il codice per creare e memorizzare un database del denaro nella cassaforte della banca, oltre a gestire le operazioni relative ai saldi nelle altre casseforti bancarie.
choosemoney: Contiene il codice necessario per selezionare la valuta e assicurarsi che il codice funzioni in base alla valuta scelta.
doviz.py: Contiene il codice per ottenere i tassi di cambio tra le valute da internet.
faiz.py: Contiene il codice per calcolare le operazioni di interesse.
kumar.py: Contiene il codice per i giochi d'azzardo.
lang.py: Contiene il codice per cambiare lingua.
library.py: Contiene la struttura tipo dizionario necessaria per visualizzare le traduzioni nella lingua selezionata dopo il cambiamento.
main.py: Contiene le funzioni per il login utente, la registrazione dell'utente, le transazioni di denaro e per eseguire tutte le funzioni, comprese le verifiche al di fuori dei controlli interni.
money_transfer: Contiene il codice per le operazioni di trasferimento di denaro, consentendo trasferimenti anche tra i propri conti. Il tasso di cambio attuale sarà calcolato e riflesso di conseguenza.
user.py: Contiene le funzioni necessarie per operazioni come registrazione, accesso, creazione di account e altro ancora.





# What You Need to Use the Application:

1- SQLite3
2- SQLite3DB
3- Python
4- Some Python Repos

# How do I install the required files?

# Arch Linux :

1- $ sudo pacman -S python
2- $ sudo pacman -S sqlite
3- $ sudo pacman -S python-sqlite
4- $ sudo pacman -S sqlitebrowser
5- $ sudo pacman -S python-requests

# Fedora :

1- $ sudo dnf install python3
2- $ sudo dnf install sqlite
3- $ sudo dnf install python3-sqlite / pip install sqlite
4- $ sudo dnf install python3-requests / pip install requests
5- $ sudo dnf install sqlitebrowser

# Debian/Ubuntu : 

1- $ sudo apt-get install python3
2- $ sudo apt-get install sqlite3
3- $ sudo apt-get install python3-sqlite
4- $ sudo apt-get install python3-requests / pip install requests
5- $ sudo apt-get install sqlitebrowser



# USAGE

You can open the terminal for Linux, PowerShell or CMD for Windows, and the terminal for MacOS users.

Make sure Git is installed on your computer. If Git is not installed, you can download and run it as a zip file.


I assume you have uploaded it to the Downloads folder.
$ git clone https://github.com/BedirMirac/bankApp.git

$ cd Download/bankApp

$ python main.py

If you have completed the necessary installations successfully, the program will open.

# Final Remarks:

"Thank you for installing the application. I hope you make progress financially."

:)
