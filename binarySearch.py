'''
    Αρχείο binarySearch.py 
    --------------------------------------------------------------------
    Η κατασκευαστική μέθοδος αρχικοποιεί το παρόν αντικείμενο της βάσης, 
    το οποίο δέχεται και ως παράμετρο. Η κλάση χρησιμοποιεί το αντικεί- 
    μενο αυτό, για να καλέσει απευθείας τη μέθοδο ταξινόμησης στηλών πί- 
    νακα 'sort', αλλά και για να προσπελάσει τα απαραίτητα για τη δυαδι- 
    κή αναζήτηση υπο-αντικείμενά του.
'''

class BinarySearch:
    
    #   Κατασκευαστική μέθοδος
    def __init__(self, database_object):
        self.database_object = database_object
        
    '''
        Η μέθοδος 'binarySearch' καλείται επί του ορισμένου αντικειμένου 
        δυαδικής αναζήτησης. Δηλαδή η κλήση έχει την κατωτέρω μορφή: 
        <database:Database object key>.<binarySearch:BinarySearch object key>.binarySearch(<arguments>)
        
        Η μέθοδος αυτή εκκινεί τη δυαδική αναζήτηση του στοιχείου <query_obj> 
        στη στήλη <column_name>, του πίνακα <table_name>.
    '''
    def binarySearch(self, table_name, column_name, query_obj):
        try:
            self.database_object.sort(table_name, column_name, True)
        except:
            return f'Couldn\'t sort column "{column_name}" from table "{table_name}". Please, make sure that the "sort" function of the class "{self.database_object.__class__.__name__}", is properly defined.'
        self.table_column = self.database_object.tables[table_name].columns[self.database_object.tables[table_name].column_names.index(column_name)]
        query_obj_index = self.binarySearchRecursion(0, len(self.table_column) - 1, query_obj)
        return query_obj_index
        
    '''
        Η μέθοδος 'binarySearchRecursion' καλείται αυτόματα από την 'binarySearch' 
        και είναι αυτή που πραγματοποιεί τη δυαδική αναζήτηση, με αναδρομικό τρόπο 
        και με βάση τα ορίσματα που έχουν δοθεί.
    '''
    def binarySearchRecursion(self, min_index, subcolumn_length, query_obj):
        middle_index = int((min_index + subcolumn_length) / 2)
        if query_obj == self.table_column[middle_index]:
            return middle_index
        elif (subcolumn_length - min_index) < 1:
            return -1
        elif query_obj < self.table_column[middle_index]:
            return self.binarySearchRecursion(min_index, middle_index - 1, query_obj)
        elif query_obj > self.table_column[middle_index]:
            return self.binarySearchRecursion(middle_index + 1, subcolumn_length, query_obj)
        return -1

