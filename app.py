from flask import Flask
from views import index, create, edit, delete

app = Flask(__name__)
app.template_folder = 'templates'

app.route('/')(index)
app.route('/create', methods=['GET', 'POST'])(create)
app.route('/edit/<int:user_id>', methods=['GET', 'POST'])(edit)
app.route('/delete/<int:user_id>')(delete)

if __name__ == '__main__':
    app.run()
