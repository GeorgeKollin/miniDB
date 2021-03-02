'''
    Αρχείο main.py
    -------------------------------------------
    Προτεινόμενο αρχείο εκκίνησης της miniDB 
    σε περιβάλλον γραμμής εντολών. Περιλαμβάνει
    τα αρχεία εισαγωγής εγγραφών στη βάση, 
    καθώς και μία οικουμενική μέθοδο διαγραφής
    βάσεων δεδομένων.
'''

import shutil

'''
    Αρχεία προς εισαγωγή στη βάση. Καθένα από τα παρακάτω 
    αρχεία δημιουργεί ένα αντικείμενο βάσης 'db'. Έχουν 
    τοποθετηθεί σε δομή επιλογής, καθότι η μαζική εισαγωγή 
    τους στο σύστημα, θα καθιστούσε ορισμένα αντικείμενα 
    βάσης, απροσπέλαστα.
'''
file_index = 4

if file_index == 0:
    exec(open('largeRelationsInsertFilebulk.py').read())
elif file_index == 1:
    exec(open('largeRelationsInsertFile.py').read())
elif file_index == 2:
    exec(open('smallRelationsInsertFilebulk.py').read())
elif file_index == 3:
    exec(open('smallRelationsInsertFile.py').read())
else:
    exec(open('vsmdb.py').read())

'''
    Εξωτερικός ορισμός μεθόδου καταστροφής βάσεων δεδομένων. 
    Ο οικουμενικός ορισμός διασφαλίζει το γεγονός πως η βάση 
    θα καταργηθεί τόσο από το σύστημα αρχείων, όσο και από 
    το χώρο διευθύνσεων στη RAM.
'''
def dropDB(database_object_value):
    '''
            Αναζήτηση και αφαίρεση όλων των αναφορών από τη RAM 
            προς τη βάση.
    '''
    database_object_key = None
    try:
        k = len(globals()) - 1
        for i in range(k + 1):
            if list(list(globals().items())[k - i])[1] == database_object_value:
                database_object_key = list(list(globals().items())[k - i])[0]
                del globals()[database_object_key]
        #   Κατάργηση της βάσης από το σύστημα αρχείων
        shutil.rmtree(database_object_value.savedir)
        return True
    except:
        pass
    return False

