import mysql.connector
config ={
    "host":"127.0.0.1",
    "user":"root",
    "password":"nova_senha", 
}
try:
    con = mysql.connector.connect(**config)
    if con.is_connected():
        print("Deu certo")
    con.close()
except mysql.connector.Error as erro:
    print(erro)