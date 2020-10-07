import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
        
    def uploadfile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
         dbx.files_upload(f.read(),file_to)

def main():
    access_token='-CB8MH7Ukx3QAAAAAAAAAAaE4FZPG329aGODXC528ZTVB6UZ0am3WF9Q_x0_kMQtU'
    transferData = TransferData(access_token)
    
    file_from=input("enter the file path to transfer to dropbox")
    file_to=input("enter the full path to upload to dropbox")

    #apiv2
    transferData.uploadfile(file_from, file_to)
    print("file is moved succsesfuly")

 
main()

