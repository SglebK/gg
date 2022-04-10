import zipfile

divtionary = "dictionary.txt"
archive = "archive.zip"
archive_zip = zipfile.ZipFile(archive)

f = open(divtionary)
for line in f.readlines():
    password = line.strip("\n")
    try:
        archive_zip.extractall(pwd=bytes(password, "utf-8"))
    except:
        print(password + " Неверный пароль")
    else:
        print(password + " Верный пароль")
        break
    finally:
        print(" ")