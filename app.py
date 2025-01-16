from flask import (
    Flask, #библиотека фласк
    render_template, #компонент который переносит перемен в html
    redirect, #перенос данных
    request #запрос на шаблон или сайт
)
app = Flask(__name__) #инициализация

@app.route('/base', methods=['GET', 'POST'])
def get_base():
  

    return render_template('base.html')

@app.route('/log', methods=['GET', 'POST'])
def get_log():
  

    return render_template('loger.html')

@app.route('/reg', methods=['GET', 'POST'])
def get_reg():


    return render_template('register.html')







if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )