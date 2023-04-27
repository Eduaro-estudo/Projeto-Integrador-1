#https://www.youtube.com/watch?v=mWdBpNy0BAM&t=0s
import sqlite3 as sql

con = sql.connect('cliente.db') # conector com banco de dados
cur =con.cursor()
cur.execute('DROP TABLE IF EXISTS users') # substitui tabela, caso exista

sql = ''' CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "SERVICO" VARCHAR(10) NOT NULL,
    "EQUIPAMENTO" VARCHAR(30) NOT NULL,
    "NOME" VARCHAR(30) NOT NULL,
    "ENDERECO" VARCHAR(50) NOT NULL,
    "FONE" INTEGER(12) NOT NULL
          
)''' # aspas triplas por se multiplas linhas

cur.execute(sql) # colocar os campos na tabela
con.commit()     # registra dados
con.close()      # fecha banco

# ao final da execução criará o arquivo de BD