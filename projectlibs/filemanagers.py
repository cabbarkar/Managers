from abc import ABC, abstractmethod
import os
import datetime as dt

class FileManager():
    """
    Alt sınıflar için soyut sınıf tanımı
    """
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def open_file(self, filepath:str, mode:str):
        """_summary_

        Args:
            filepath (str): açılacak olan dosya yolu
            mode (str): dosya açma metodu
        """
        pass
    
    @abstractmethod
    def close_file(self):
        """
        açılan dosyayı kapatmak amacıyla kullanılacak fonksiyon
        """
        pass
    
    @abstractmethod
    def read_entire_file(self, file_path:str)-> str:
        """_summary_

        Args:
            file_path (str): açılacak olan dosyanın yolu

        Returns:
            str: dosya içeriğini döndürür
        """
        pass
    
    @abstractmethod
    def read_line_from_file(self, file_path:str)->str:
        """_summary_

        Args:
            file_path (str): açılacak olan dosyanın yolu


        Returns:
            str: Dosyadan okunan tek bir satır döndürür.
        """
        
    @abstractmethod
    def write_to_file(self, file_path:str, data:str)->str:
        """_summary_

        Args:
            file_path (_type_): Açılacak dosyanın yolu
            data (str): dosyaya yazılacak olan bilgi
        Returns:
        """
        pass
    
    @abstractmethod
    def append_to_file(self, file_path:str, data:str)->str:
        """_summary_

        Args:
            file_path (str): Açılacak dosyanın yolu
            data (str): Yazılacak olan bilgi
        """
        pass
    
    def delete_file(self,file_path:str):
        """Dosyayı tamamı ile siler

        Args:
            filepath (str): silinecek olan dosyanın yolu
        """
        try:
            os.remove(file_path)
        except Exception as e:
            print(str(e), "dosya silme hatası")
            
    def get_file_size(self, file_path:str)->int:
        """Dosya boyutu okuma

        Args:
            file_path (str): Dosya boyutu alınacak olan eleman

        Returns:
            int: Dosy boyutu
        """
        
        return os.path.getsize(file_path)

    def get_file_creation_time(self, file_path)-> dt:
        """Dosyanın oluşturma zamanını döner

        Args:
            file_path (_type_): dosya yolunu belirtir

        Returns:
            datetime: Dosyanın oluşturulduğu tarih ve saati döner.
        """
        return dt.datetime.fromtimestamp(os.path.getctime(file_path))

            
    
        
        
        
        