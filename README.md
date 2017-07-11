# Blog

Wir programmieren einen eigenen Blog. Damit decken wir viele wichtigen Web-Themen ab. Als Grundlage müssen wir uns jedoch zuvor noch die Objektorientierung anschauen.

OOP ist die Basis, auf der viele Frameworks basieren. Insbesondere dann, wenn Daten hierarchisch in einer Datenbank gespeichert werden sollen, kann eine Aufteilkung des Codes in
Klassen und Objekte Sinn machen.

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
