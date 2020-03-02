
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')


with conn:
    cur = conn.cursor()
    
    fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for fileName in fileList:
        if fileName.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)", \
                (fileName,))
            print(fileName)
    conn.commit()
conn.close()
