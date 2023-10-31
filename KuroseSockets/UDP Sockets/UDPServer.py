# Εισαγωγή του απαραίτητου module socket
from socket import *

# Ορισμός της θύρας του διακομιστή
serverPort = 12000

# Δημιουργία ενός socket αντικειμένου χρησιμοποιώντας IPv4 διεύθυνση και πρωτόκολλο UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Δέσμευση του socket στην καθορισμένη διεύθυνση IP ("192.168.44.89" σε αυτήν την περίπτωση) και στη θύρα που καθορίσατε
serverSocket.bind(("192.168.44.89", serverPort))

# Εκτύπωση μηνύματος για να δείξετε ότι ο διακομιστής είναι έτοιμος να δεχτεί πακέτα
print("The server is ready to receive")

# Εισαγωγή σε μια ατέλειωτη βρόχο για την χειρισμό των πακέτων που έρχονται από τους πελάτες
while True:
 # Λήψη ενός πακέτου και της διεύθυνσης του πελάτη που το έστειλε
 message, clientAddress = serverSocket.recvfrom(2048)

 # Μετατροπή του μηνύματος που λήφθηκε σε μια συμβολοσειρά και μετατροπή της σε κεφαλαία γράμματα
 modifiedMessage = message.decode().upper()

 # Αποστολή του τροποποιημένου μηνύματος πίσω στον πελάτη με τη χρήση της διεύθυνσης του πελάτη
 serverSocket.sendto(modifiedMessage.encode(), clientAddress)
