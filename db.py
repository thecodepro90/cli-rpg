import os
import base64
import random
import uuid
import string


def encrypt(data, encryption_level):
    e_data = data
    for i in range(encryption_level):
        data_bytes = e_data.encode("ascii")
        base64_bytes = base64.b64encode(data_bytes) 
        base64_string = base64_bytes.decode("ascii") 
        e_data = base64_string
    return e_data

def decrypt(data, encryption_level):
    d_data = data
    for i in range(encryption_level):
        data_bytes = d_data.encode("ascii") 
        string_bytes = base64.b64decode(data_bytes) 
        string = string_bytes.decode("ascii") 
        d_data = string
    return d_data

def get_uuid():
    r_uuid = uuid.uuid4().hex
    random_char = random.choice(string.ascii_letters)
    r_uuid = random_char + r_uuid
    return r_uuid
class DB_DEPRECIATED:
    def __init__(self, name, encryption_level):
        self.db_name = name
        self.encryption_level = encryption_level
        self.db_path = self.db_name+"-DBINFO.txt"
        file = os.path.isfile(self.db_path)
        
        
        
        self.tables = []
        if file:
            with open(self.db_path, "r") as f:
                data = f.readlines()
                for i in data:
                    self.tables.append(self._decrypt(i).strip("\n"))
        else:
            f = open(self.db_path, "w")
            
        
    def _encrypt(self, data):
        e = encrypt(data, self.encryption_level)
        return e
        
    def _decrypt(self, data):
        d = decrypt(data, self.encryption_level)
        return d
    
    def _add_table(self, table):
        with open(self.db_path, "a+") as f:
            f.write(self._encrypt(table)+"\n")
        
        
    def create_table(self, name): 
        file_path = self.db_name+"-"+name+".txt"
        file = os.path.isfile(file_path)
        if not file:
            f = open(file_path, "w")
            self._add_table(file_path)
            self.tables.append(file_path)
        
    def update(self, table, row, data):
        for i in self.tables:
            if self.db_name+"-"+table+".txt" == i:
                rows = self.return_rows(table)
                rows[int(row)] = data
                with open(i, "w") as f:
                    for j in rows:   
                        f.write(self._encrypt(j)+"\n")
                    
    def append(self, table, data):
        for i in self.tables:
            if self.db_name+"-"+table+".txt" == i:
                with open(i, "a") as f:
                   f.write(self._encrypt(data)+"\n") 
                
                    
    def get_row(self, table, string):
        rows = self.return_rows(table)
        for row, data in enumerate(rows):
            if string == data:
                return row
            
    
    def return_row_data(self, table, row):
        rows = self.return_rows(table)
        return rows[row]
                
    def return_rows(self, table):
        rows = []
        for i in self.tables:
            stripped_table = i.replace(".txt", "")
            stripped_table = stripped_table.replace(self.db_name+"-", "")
            if table == stripped_table:
              with open(i, "r") as f:
                    lines = f.readlines()
                    for i in lines:
                        rows.append(str(self._decrypt(i)))
        return rows
    
    def remove(self, table, row):
        rows = self.return_rows(table)
        rows.pop(row)
        with open("{}-{}.txt".format(self.db_name, table), "w") as f:
            f.write(rows)
            
    def delete_table(self, table):
        tables = []
        for i in self.tables:
            if not i == "{}-{}.txt".format(self.db_name, table):
                tables.append(self._encrypt(i))
                with open(self.db_path, "w") as f:
                    f.writelines(tables)
            else:
                os.remove(i)

class Table:
    def __init__(self, name, columns):
        self.table_name = name
        self.table_path = f"{self.table_name}.txt"
        self.columns = columns
        self.rows = []
        if not os.path.isfile(self.table_path):
            with open(self.table_path, "w") as f:
                f.write(' '.join(columns))
                
        else:
            data = open(self.table_path, "r").readlines()
            self.columns = data[0].strip("\n").split(" ")
            unformated_rows = data[1:]
            for row in unformated_rows:
                self.rows.append(row.strip("\n").split(" "))
            print(self.rows)
            print(self.columns)
            
    def get_row(self, row):
        return self.rows[row]

    def get_column(self, column):
        for i, j in enumerate(self.columns):
            if j == column:
                column = i
        columns = []
        for row in self.rows:
            columns.append(row[column])
            
        return columns
            
                
        
            

table = Table("users", ["uname", "upwd"])
print(table.get_column("uname"))

class DB:
    def __init__(self, name):
        self.db_name = name
        self.db_path = f"{self.db_name}-INFO.txt"
        self.tables = []
        if not os.path.isfile(self.db_path):
            f = open(self.db_path, "x")
        else:
            
            data = open(self.db_path, "r").readlines()
            for i in data:
                self.tables.append(i.strip("\n"))
        # print(self.tables)

db = DB("users")