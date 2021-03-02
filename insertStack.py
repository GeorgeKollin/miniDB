'''
    Αρχείο insertStack.py 
    ------------------------------------
    Η κατασκευαστική μέθοδος αρχικοποιεί 
    τη στοίβα εισαγωγών.
'''

class InsertStack:
    
    #   Κατασκευαστική μέθοδος
    def __init__(self):
        self.insert_stack = []
        
    '''
        Η μέθοδος 'addToInsertStack' προσθέτει στη στοίβα εισαγωγών 
        μία μικρή υπολίστα, η οποία περιλαμβάνει τον πίνακα <table_name>, 
        στον οποίο έγινε η εισαγωγή, καθώς και το δείκτη γραμμής της 
        νεοεισαχθείσας εγγραφής. Δηλαδή, η στοίβα εισαγωγών λαμβάνει την 
        κατωτέρω μορφή: 
        [[<table_name_1>, <tb_1_new_row_index>], 
        [<table_name_2>, <tb_2_new_row_index>], ..., 
        [<table_name_n>, <tb_n_new_row_index>]]
    '''
    def addToInsertStack(self, table_name, row_index):
        row_to_be_inserted = [table_name, row_index]
        self.insert_stack.append(row_to_be_inserted)
        return row_to_be_inserted
    
    '''
        Η μέθοδος 'updateInsertStack' ενημερώνει τους δείκτες των νεοεισαχθέντων 
        γραμμών του πίνακα <table_name> που υπάρχουν στη στοίβα εισαγωγών, με 
        βάση την αλλαγή <referrer> που αυτός υπέστη (διαγραφή γραμμής ή ταξινόμηση 
        στήλης).
    '''
    def updateInsertStack(self, table_name, referrer, indexes_to_be_processed):
        if indexes_to_be_processed is not None:
            insert_stack_size = len(self.insert_stack)
            if (referrer == 'delete_rows'):
                for i in range(insert_stack_size):
                    k = insert_stack_size - i - 1
                    if (self.insert_stack[k][0] == table_name) and (self.insert_stack[k][1] in indexes_to_be_processed):
                        self.insert_stack.pop(k)
            elif (referrer == 'sort_rows'):
                for i in range(insert_stack_size):
                    if (self.insert_stack[i][0] == table_name) and (self.insert_stack[i][1] in indexes_to_be_processed):
                        self.insert_stack[i][1] = indexes_to_be_processed.index(self.insert_stack[i][1])
        return
                




