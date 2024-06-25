from filemanagerss import FileManager
import datetime as dt

class TextManager(FileManager):
    """
        FileManager Classından implement edilmiş Text dosyası
    """
    
    def open_file(self, file_path:str, mode:str):
        self.file = open(file_path,mode)
        
    def close_file(self):
        if self.file :
            self.file.close()
    
    def create_file(self, file_path:str):
        with open(file_path,"w") as file:
            pass #sadece boş dosya yaratır
            
    def read_entire_file(self, file_path: str) -> str:
        with open(file_path) as file:
            return file.read()
        
    def read_line_from_file(self, file_path: str) -> str:
        with open(file_path) as file:
            return file.readline()
        
    def read_lines_from_file(self, file_path: str) -> list:
        with open(file_path) as file:
            return file.readlines()
        
    def write_to_file(self, file_path: str, data: str):
        with open(file_path,"w" ) as file:
            file.write(data)
            
    def append_to_file(self, file_path: str, data: str):
        with open(file_path,"a" ) as file:
            file.write(data+"\n")
            
    def delete_file(self, file_path: str):
        super().delete_file1(file_path)
        
    def get_file_size(self, file_path: str) -> int:
        return super().get_file_size(file_path)
    
    def get_file_creation_time(self, file_path: str) -> dt:
        return super().get_file_creation_time(file_path)
    
    def get_file_modification_time(self, file_path: str) -> dt:
        return super().get_file_modification_time(file_path)
    
    def find_text_in_file(self, file_path:str, text_to_search:str)->list:
        word_location_list = []
        
        with open(file_path) as file:
            for line_num, lien in enumerate(file):
                char_index=line.find(text_to_search)
                if char_index!=-1:
                    word_location_list.append((char_index,line_num))
        return word_location_list
    
    def replace_text_in_file(self, file_path:str,old_text:str,new_text:str)->int:
        with open(file_path) as file:
            content = file.read()
        change_count = content.count(old_text)
        new_content = content.replace(old_text,new_text)
        
        with open(file_path,"w") as file:
            file.write(new_content)
            
        return change_count
    
if __name__=="__main__":
    print("Direk bu dosyayı çalıştırmak sana yakışıyor mu?")