from flask import Flask, request, render_template

app = Flask(__name__)

checkbox_options = {
    'option1': '選択肢1のメッセージ',
    'option2': '選択肢2のメッセージ',
    'option3': '選択肢3のメッセージ'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 開始日時と終了日時を取得
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        message = f"開始日: {start_date}, 終了日: {end_date}"

        selected_options = request.form.getlist('option')  # 選択されたチェックボックスの値をリストで取得
        message = message + '\n' + ', '.join([checkbox_options.get(option, '選択肢が無効です') for option in selected_options])
        images = []
        print(selected_options)

        for option in selected_options:
            # 選択されたオプションに対応する画像を取得し、リストに追加
            image_path = f'static/{option}.png'
            images.append(image_path)

        return render_template('index.html', message=message, images=images)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
