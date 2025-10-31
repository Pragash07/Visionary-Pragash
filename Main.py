import shutil
import os


def get_folder():
    path = input("Enter the Folder : ")
    if os.path.exists(path):
        files = os.listdir(path)
        print(files)
        return path, files
    else:
        print("No Folder Found")
        exit()


def create_folders(path):
    Imgfol = path + "/Images"
    docfol = path + "/Documents"
    Vidfol = path + "/Videos"
    audfol = path + "/Audio"
    exefol = path + "/Executables"
    Arcfol = path + "/Archives"
    Othfol = path + "/Others"

    for fol in [Imgfol, docfol, Vidfol, audfol, exefol, Arcfol, Othfol]:
        os.makedirs(fol, exist_ok=False)

    return Imgfol, docfol, Vidfol, audfol, exefol, Arcfol, Othfol


def get_extensions():
    Images = [".png", ".jpeg", ".jpg", ".gif", ".webp", ".bmp"]
    Documents = [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".xls", ".xlsb", ".xlsm"]
    Videos = [".mp4", ".mkv", ".avi"]
    Audio = [".mp3", ".wav", ".flv"]
    Executables = [".exe", ".msi", ".bat"]
    Archives = [".zip", ".rar", ".7z"]
    
    return Images, Documents, Videos, Audio, Executables, Archives


def move_files(path, files, folders, exts):
    Imgfol, docfol, Vidfol, audfol, exefol, Arcfol, Othfol = folders
    Images, Documents, Videos, Audio, Executables, Archives = exts

    Imgcount = doccount = Vidcount = audcount = execount = Arccount = Othcount = 0

    for file in files:
        source = path + "/" + file
        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        if extension in Images:
            dest = Imgfol; Imgcount += 1
        elif extension in Documents:
            dest = docfol; doccount += 1
        elif extension in Videos:
            dest = Vidfol; Vidcount += 1
        elif extension in Audio:
            dest = audfol; audcount += 1
        elif extension in Executables:
            dest = exefol; execount += 1
        elif extension in Archives:
            dest = Arcfol; Arccount += 1
        else:
            dest = Othfol; Othcount += 1

        shutil.move(source, dest + "/" + file)

    print("Image File Count : " + str(Imgcount))
    print("Documents File Count : " + str(doccount))
    print("Videos File Count : " + str(Vidcount))
    print("Audio File Count : " + str(audcount))
    print("Executables File Count : " + str(execount))
    print("Archives File Count : " + str(Arccount))
    print("Others File Count : " + str(Othcount))


def final():
    path, files = get_folder()
    folders = create_folders(path)
    exts = get_extensions()
    move_files(path, files, folders, exts)


final()
