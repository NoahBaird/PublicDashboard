import sys
sys.path.insert(0, 'C:\Python27\Projects\PublicDashboard\Dashboard')
import Hiddens
import dropbox

dbx = dropbox.Dropbox(Hiddens.DropBoxAccessToken)
currentAccount = dbx.users_get_current_account()

for child in dbx.files_list_folder('').entries:
    print(child.name)

# dbx.files_upload("Lorem Ipsum", '/outer folder/inner folder/example.txt')
# dbx.files_delete('/cavs vs warriors')
# print(dbx.files_get_metadata('/Bar_Graph_Example.xlsx'))

# dbx.files_download_to_file('C:\Users\NB029380\Desktop\Downloaded_Bar_Graph_Example.xlsx', '/Bar_Graph_Example.xlsx')
print ("success")