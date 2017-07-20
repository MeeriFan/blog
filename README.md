# Blog

Wir programmieren einen eigenen Blog. Damit decken wir viele wichtigen Web-Themen ab. Als Grundlage müssen wir uns jedoch zuvor noch die Objektorientierung anschauen.

OOP ist die Basis, auf der viele Frameworks basieren. Insbesondere dann, wenn Daten hierarchisch in einer Datenbank gespeichert werden sollen, kann eine Aufteilkung des Codes in
Klassen und Objekte Sinn machen.

[Dieses Tutorial](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/) sieht sinnvoll aus.

## Vorbereitung

Lies dich über Objektorientierung schlau. Du solltest folgende Fragen beantworten können:

1) Was ist eine Klasse?
2) Was sind Objekte (oder Instanzen)?
3) Wie funktioniert Vererbung (Polymorphismus)

Habe dabei immer im Kopf, dass wir später einen Blog bauen möchten.

## Klassen für einen Blog anlegen

In einem Blog kann ich mir die folgenden Klassen vorstellen. Implementiere sie und orientiere dich an den Vorschlägen für das Interface.
Wir wollen in diesem Schritt noch keine Datenbank und auch noch keine Webapp haben. Es geht nur um die Klassen und ihre Beziehung zueinander.

Schreibe ein kurzes Nutzungsbeispiel, nachdem du alle Klassen implementiert hast. In diesem Beispiel erstellst du ein paar Instanzen für jede Klasse
und verknüpfst die Objekte miteinander. Beispiel: erzeuge zwei User mit jeweils zwei Posts und ein paar Comments.

### User

Fields: `email: str, first_name: str, last_name: str, posts: list of Posts`  
Methods: `full_name(): str, posts(): list of Posts`

### Post

Fields: `title: str, body: str, publish_date: datetime, created_at: datetime, author: User`  
Methods: `is_published(): boolean`

### Comment

Fields: `author_email: str, body: str, created_at: datetime, post: Post`  
Methods: ...

## Restful Routes

Nun, da wir User anlegen können und uns auch als User einloggen können, wird es Zeit, auch ohne Datenbankzugriff mit Usern interagieren zu können. Da wir einen Blog schreiben, wollen wir auch eine Übersicht über alle User(=Autoren) haben.

Neue Routen:

`GET /users` -> Zeige eine Liste mit allen Usern und Verlinkung auf die Detailseiten eines Users  
`GET /users/{userid}` -> wobei {userid} eine variable Zahl ist. Zeigt die Detailseite eines Users an. Aktuell würde ich einfach Vorname und Nachname anzeigen, später kommen hier noch die Posts der User hin.  

## Userprofil

Ein User braucht einen Profiltext, der frei befüllbar sein soll. Das ist eine Fingerübung für das Verfassen von Posts.

* wenn ich eingeloggt bin und mein Profil besuche
  * kann ich in einer `textarea` einen Profiltext editieren und speichern
* wenn ich das Profil anderer User besuche, kann ich deren Profiltext nur lesen, aber nicht bearbeiten

Dazu braucht die Usertabelle ein neues Feld. Achte auf den korrekten Datentyp in SQLite: TEXT

Bearbeiten kann ich mein Profil unter `GET /profile`. Das Formular soll Updates per `POST` an `/profile` senden. Später werden wir das ändern.
