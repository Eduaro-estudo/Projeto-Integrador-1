# Eduardo A. A. Garcia -  Gabrielle de Souza
# Projeto Integrador 1 - 21/05/23 - deploy funcionando
# Este é o primeiro arquivo a ser executado, onde ficam as rotas para os outros templates
# projeto executou com sucesso no servidor pythonanywhere.com

from flask import Flask, render_template,request,redirect,url_for,flash
import sqlite3 as sql
from flask_login import logout_user

app=Flask(__name__)
app.secret_key="projeto.integrador.engenharia" # se não for colocado dá erro no servidor quando fizer deploy

@app.route("/")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/processar_login.py', methods=['POST'])
def processar_login():
    username = request.form['username']
    password = request.form['password']
    
    # Verifique as credenciais (lógica de autenticação)
    if username == 'piunivesp' and password == '123456':
        return render_template("home.html")
    else:
      
       return render_template("errologin.html")
    
@app.route('/logout')
def logout():
    response = redirect(url_for('login'))
    response.delete_cookie('session_id')
    return response

   


      

 

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/index")
def index():
    con = sql.connect("cliente.db")
    con.row_factory=sql.Row # vai percorre as linhas do BD
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall() # variável data recebe todo conteúdo da tabela
    return render_template("index.html", datas=data) # datas vai receber conteudo da var data

@app.route("/add_user", methods=["POST","GET"])
def add_user(): # aqui a informação enviada do formulário pelo método POST é associado a cada variável, de cada campo da tabela
    if request.method == "POST":
       servico=request.form["servico"]
       dentrada=request.form["dentrada"]
       dsaida=request.form["dsaida"]
       equipamento=request.form["equipamento"]
       nome=request.form["nome"]
       endereco=request.form["endereco"]
       fone=request.form["fone"]
       orcamento=request.form["orcamento"]

       con=sql.connect("cliente.db") # começa a conexão co o banco de dados
       cur=con.cursor()
       cur.execute("insert into users(SERVICO,DENTRADA,DSAIDA,EQUIPAMENTO,NOME,ENDERECO,FONE,ORCAMENTO) values(?,?,?,?,?,?,?,?)",(servico,dentrada,dsaida,equipamento,nome,endereco,fone,orcamento))
       # esta sequência de interrogações serve para evitar sql injection
       con.commit()
       flash("Dados cadastrados","success") # mensagem para usuário, "success" será usado pelo bootstrap
       return redirect(url_for("index")) # terminado cadastro volta para a página inicial
    return render_template("add_user.html")

        

@app.route('/edit_user/<string:id>', methods=["POST","GET"]) # reconhecerá o usuário quando passar o id
def edit_user(id):
    if request.method=="POST":
       servico=request.form["servico"]
       dentrada=request.form["dentrada"]
       dsaida=request.form["dsaida"]
       equipamento=request.form["equipamento"]
       nome=request.form["nome"]
       endereco=request.form["endereco"]
       fone=request.form["fone"]
       orcamento=request.form["orcamento"]

       con=sql.connect("cliente.db")
       cur=con.cursor()
       cur.execute("update users set SERVICO=?,DENTRADA=?,DSAIDA=?,EQUIPAMENTO=?,NOME=?,ENDERECO=?,FONE=? ,ORCAMENTO=? where ID=?",(servico,dentrada,dsaida,equipamento,nome,endereco,fone,orcamento,id))
       con.commit()
       flash("Dados atualizados", "success")
       return redirect(url_for("index")) # atualizou, volta para página inicial
    
    con=sql.connect("cliente.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where ID=?",(id,))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
    con=sql.connect("cliente.db")
    cur=con.cursor()
    cur.execute("delete from users where ID=?",(id,))
    con.commit()
    flash("Dados apagados", "warning")
    return redirect(url_for("index"))


if __name__=="__main__":
  
    app.run(debug=True)








