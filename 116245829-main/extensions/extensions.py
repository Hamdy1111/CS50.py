file_check=input('File name: ')
file_check=file_check.lower().strip()

if '.gif' in file_check:
    print("image/gif")
elif '.jpg' in file_check:
    print("image/jpeg")
elif '.jpeg' in file_check:
    print("image/jpeg")
elif '.png' in file_check:
    print("image/png")
elif '.pdf' in file_check:
    print("application/pdf")
elif '.txt' in file_check:
    print("text/plain")
elif '.zip' in file_check:
    print("application/zip")
else:
    print("application/octet-stream")
