# APPUNTI


-- pacchetto = {type: < command-outcome > , specific: <> , args: []}
-- pacchetto messaggio = args: [sender, recipient, message]
-- pacchetto messaggio = args: {}
-- lista new_mess(questi liste
                  vengono messi in un coda): {}
-- _msg_history = {
    '<sender>': {
        '<msg_hash>': {'<state>': Bool, '<self>': '', '<msg>': ''}
    }
}

command e outcome sono uno la conseguenza dell'altro, notifications viaggiano anche senza un comando inserito

- non transforamre il file.ui in un file.py
- aggiungere controllo che ti fa usare le funzioni solo se hai dato un nome univoco al client
- aggiungere parametro che decide se salvare i messaggi in ram o sul disco
- guardare sincronizzazione quando un utente chiude il programma ma l'altro no
- finire friend request
- segnalare una notifica al sistema 
- aggiungere informazioni a set_name (se il nome è gi stato preso)
- non usare direttamente _name del client
- fare le notifiche che fanno la stessa cosa in un unico case.const....
- puoi mandare messaggi solo ai contatti con cui sei amico
- decidere se aggiungere controlli o lasciare il lavoro a chi usa il framework
- risolvere none che arrivano a caso
- controllo che non ti fa mandare a richiesta ad uno con cui sei gia amico
- essere sicuri che gli id dei messaggi non siano mai doppi
- no far ricaricare tutta la chat ma solo imessaggi aggiunti

DOVE CONTINUARE:


DIFFERENZA TRA OUTCOME E NOTIFICATION:
un outcome è una risposta che aspetti per continuare il programma mentre le
notifiche arrivano in momenti non conosciuti

FORMATTAZIONE PACCHETTI:
    COMMAND:
        SET_NAME: da mandare al server che ti da una risposta in outcome
        DISCONNECT: disconnette l'applicazione dal server
        SEND_MESS: aspetti la risposta dal server per sapere che il messaggio è stato mandato, da cambiare in notifica
        SEND_FRIEND_REQUEST: forse da cambiare in notifica
    OUTCOME:
        SET_NAME: ti dice se il nome è già stato preso
    NOTIFICATION:
        MESSAGE: ti notifica che è arrivato un messaggio
        VISUALIZED_MESS: notifica che il messagiio è stato visualizzato
        ARRIVED_MSG: