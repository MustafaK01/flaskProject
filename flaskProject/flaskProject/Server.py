from Routes import *

app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="hastane"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

if __name__=="__main__":
    app.run(debug=True)
