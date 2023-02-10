from flask import Flask
from flask import render_template, request
import jinja2
import config  # 配置文件
from response_api import answer

app = Flask(__name__)
app.config.from_object(config)


def get_response(question, img_size, img_number):

    ans = answer(question,  img_size, img_number)
    img = ans.img_gen()
    idea = ans.idea_gen()
    #mood_color = ans.mood_color_gen()
    return img, idea,  # mood_color


@app.route("/form", methods=['GET', 'POST'])
def post():

    if request.method == 'POST':

        get_ques = request.form['questions']
        #get_img_num = request.form['img_num']
        get_img_size = request.form['img_size']
        answer_img, answer_idea = get_response(
            get_ques, get_img_size, 1)

        context = {
            'img_url': answer_img,
            'ideas': answer_idea,
            # 'mood': answer_mood
        }

        return render_template('form.html', **context)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=True)
