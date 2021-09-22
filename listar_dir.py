import os
import pdb


from abc import abstractmethod
from abc import ABCMeta

class I_get_info_archivo(metaclass=ABCMeta):
    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def get_directorio_base(self):
        pass
    
    @abstractmethod
    def get_size_file(self):
        pass

    @abstractmethod
    def get_ultima_fecha_modificacion(self):
        pass

    @abstractmethod
    def get_fecha_creacion(self):
        pass

class get_Info_archivo_os(I_get_info_archivo):
    
    @classmethod
    def get_nombre(cls,path):
        """ devuelve el nombre del archivo o fichero. """
        _,nombre = os.path.split(path)
        return nombre
    
    @classmethod
    def get_directorio_base(cls,path):
        """ devuelve el directorio base del archivo o fichero. """
        directorio_base,_ = os.path.split(path)
        return directorio_base
    
    @classmethod
    def get_size_file(cls,path):
        """ devuelve el tamaño del archivo o fichero. """
        size_file = os.path.getsize(path)
        return size_file
    
    @classmethod
    def get_ultima_fecha_modificacion(cls,path):
        """ devuelve el la última fecha de modificación del archivo"""
        ultima_fecha_modificacion = os.path.getmtime(path)
        return ultima_fecha_modificacion
    
    @classmethod
    def get_fecha_creacion(cls,path):
        """ devuelve la fecha de creación (igual a la última fecha de 
            modificación en Unix como Mac) """
        fecha_creacion = os.path.getctime(path)
        return fecha_creacion

class I_get_info_subdirectorio(metaclass=ABCMeta):
    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def get_directorio_base(self):
        pass
    
    @abstractmethod
    def get_size_subdirectorio(self):
        pass

    @abstractmethod
    def get_ultima_fecha_modificacion(self):
        pass

    @abstractmethod
    def get_fecha_creacion(self):
        pass

class get_Info_subdirectorio_os(I_get_info_archivo):
    
    @classmethod
    def get_nombre(cls,path):
        """ devuelve el nombre del archivo o fichero. """
        _,nombre = os.path.split(path)
        return nombre
    
    @classmethod
    def get_directorio_base(cls,path):
        """ devuelve el directorio base del archivo o fichero. """
        directorio_base,_ = os.path.split(path)
        return directorio_base
    
    @classmethod
    def get_size_subdirectorio(cls,path):
        """ devuelve el tamaño del archivo o fichero. """
        size_file = os.path.getsize(path)
        return size_file
    
    @classmethod
    def get_ultima_fecha_modificacion(cls,path):
        """ devuelve el la última fecha de modificación del archivo"""
        ultima_fecha_modificacion = os.path.getmtime(path)
        return ultima_fecha_modificacion
    
    @classmethod
    def get_fecha_creacion(cls,path):
        """ devuelve la fecha de creación (igual a la última fecha de 
            modificación en Unix como Mac) """
        fecha_creacion = os.path.getctime(path)
        return fecha_creacion

class Iplantilla_inf_directorio(metaclass=ABCMeta):
    @abstractmethod
    def crear_plantilla(self):
        pass

class Info_archivo():
    def __init__(self,path,get_Info_archivo:I_get_info_archivo):
        try:
            # pdb.set_trace()
            self.path = path
            self.nombre = get_Info_archivo.get_nombre(self.path)
            self.directorio_base = get_Info_archivo.get_directorio_base(self.path)
            self.size_file = get_Info_archivo.get_size_file(self.path)
            self.ultima_fecha_modificacion = get_Info_archivo.get_ultima_fecha_modificacion(self.path)
            self.fecha_creacion = get_Info_archivo.get_fecha_creacion(self.path)
        except Exception:
            # pdb.set_trace()
            self.nombre = ""
            self.directorio_base = "" 
            self.size_file = ""
            self.ultima_fecha_modificacion = ""
            self.fecha_creacion = ""

class Info_subdirectorio():
    def __init__(self,path,get_Info_subdirectorio:I_get_info_subdirectorio):
        try:
            pdb.set_trace()
            self.path = path
            self.nombre = get_Info_subdirectorio.get_nombre(self.path)
            self.directorio_base = get_Info_subdirectorio.get_directorio_base(self.path)
            self.size_file = get_Info_subdirectorio.get_size_subdirectorio(self.path)
            self.ultima_fecha_modificacion = get_Info_subdirectorio.get_ultima_fecha_modificacion(self.path)
            self.fecha_creacion = get_Info_subdirectorio.get_fecha_creacion(self.path)
        except Exception:
            # pdb.set_trace()
            self.nombre = ""
            self.directorio_base = "" 
            self.size_file = ""
            self.ultima_fecha_modificacion = ""
            self.fecha_creacion = ""
 
path = "D:\\Mis documentos\\Jorge"
contenido = os.listdir(path)
# print(contenido)

def list_to_text(lista: list):
    texto = ''
    for elemento in lista:
        texto += elemento + '\n'
    return texto

def list_path_to_info_archivo(lista: list,base,get_info_archivo:I_get_info_archivo):
    list_info_archivo = []
    for path in lista:
        path_absoluto = os.path.join(base,path)
        info_archivo_actual = Info_archivo(path_absoluto,get_info_archivo) 
        list_info_archivo.append(info_archivo_actual)
    return list_info_archivo

def list_path_to_info_subdirectorio(lista: list,base,get_info_subdirectorio:I_get_info_subdirectorio):
    list_info_subdirectorio = []
    for path in lista:
        path_absoluto = os.path.join(base,path)
        info_archivo_actual = Info_subdirectorio(path_absoluto,get_info_subdirectorio) 
        list_info_subdirectorio.append(info_archivo_actual)
    return list_info_subdirectorio

def extension(key):
    i = key.rfind('.')
    return key[i:]


numero_de_iterarcion = 0
n_archivos = 0
with open('C:\\todos_los_archivos.txt', 'w', encoding='utf-8') as Archivo:
    for base, dirs, files in os.walk(path):
        files.sort(key = extension)
        # print(dirs)
        # print(base)

        # if numero_de_iterarcion == 0:
        #     base = list_to_text(base)

        Objetos_files = list_path_to_info_archivo(files,base,get_Info_archivo_os)
        
        Objetos_dirs = list_path_to_info_subdirectorio(path,base,get_Info_subdirectorio_os)

        Archivo.write(50*'#'+'\n')

        Archivo.write(base)

        Archivo.write('\n')

        dirs = list_to_text(dirs)
        Archivo.write(dirs)

        n_archivos += len(files)

        files = list_to_text(files)
        Archivo.write(files)

        Archivo.write('Resumen: Numero de archivos {0}'.format(len(files))+'\n')

        numero_de_iterarcion = numero_de_iterarcion + 1

    Archivo.write('\n')

    Archivo.write('Resumen General: Numero total de archivos {0}'.format(n_archivos)+'\n')

    print(n_archivos)

if __name__ == "__main__":
    pass
     