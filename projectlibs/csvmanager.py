import csv
import json
from filemanagers import FileManager
import datetime as dt

class CSVManager(FileManager):
    """
        CSV Dosyalarını işlemek üzere oluşturulan ve
        FileManager dan implement edilen sınıf
    """

    def open_file(self, file_path:str, mode:str):
        self.file = open(file_path, mode, newline="")

    def close_filel(self):
        if self.file:
            self.file.close()

    def read_entire_file(self,file_path:str)->list:
        data = []
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            for row in content:
                data.append(row)
        return data

    def read_line_from_file(self, file_path:str)->list:
        """ Bu fonksiyon csv dosyasının sadece başlıklarını verir"""
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            return next(content)
        
    def write_to_file(self, file_path:str, data:list):
        with open(file_path, "w",newline="") as csv_file:
            content = csv.writer(csv_file)
            content.writerows(data)

    def append_to_file(self, file_path:str, data:list):
        with open(file_path, "a", newline="") as csv_file:
            content=csv.writer(csv_file)
            content.writerows(data)
    
    def csv_to_json(self,csv_file_path:str,json_file_path:str):
        """
            CSV dosyalarını, json formatına dönüştüren fonksiyon
        """
        #TODO : burda patlak olma ihtimali var. Bug a açık dosya.

        data = {}
        headers = self.read_line_from_file(csv_file_path)
        for header in headers:
            data[header] = []

        with open(csv_file_path,newline="") as csv_file:
            content=csv.reader(csv_file)

            for i, row in enumerate(content):
                if i == 0 :
                    continue
                for key_, value_ in zip(headers,row):
                    data[key_].append(value_)

        with open(json_file_path, "w", newline="") as json_file:
            json.dump(data,json_file,indent=4)
        
    def update_value_in_cell(self, file_path:str,value_to_replace:str,new_value:str):
        """
         Değiştirilecek olan değerin konumunu bulacak ve yeni ifade ile değiştirecek olan fonksiyon.
        """
        with open(file_path) as file :
            content = file.read()
        content = content.replace(value_to_replace, new_value)
        
    def update_cell_by_ref(self,
                           file_path:str,
                           reference_col:str,
                           col_to_change,
                           reference_val:str,
                           new_val:str):
        """_summary_

        Args:
            file_path (str): Değişiklik yapılacak olan dosyanın yolu
            refrence_col (str): _description_
            col_to_change (_type_): _description_
            reference_val (str): _description_
            new_val (str): _description_
        """
        data =[]
        ref_cow_index = 0
        ref_col_index = 0
        
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            
            ref_row_index = headers.index(reference_col)
            ref_col_index = headers.index(col_to_change)
            
            data.append(headers)
            for row in content:
                if row[ref_row_index] == reference_val:
                    row[ref_col_index] == new_val
                data.append(row)
                
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
            
        # data[Malzeme adı][?] -> data[?][çıkış miktarı]

    def delete_file(self, file_path:str):
        super().delete_file(file_path)

    def get_file_size(self, file_path:str)->int:
        return super().get_file_size(file_path)

    def get_file_creation_time(self, file_path:str)->dt:
        return super().get_file_creation_time(file_path)
    
    def get_modification_time(self,file_path:str)->dt:
        return super().get_modification_time(file_path)
    
