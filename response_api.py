import openai


class answer:

    def __init__(self, question: str, img_size: str, img_num: int):

        self.question = question
        self.img_size = img_size
        self.img_num = img_num

    def img_gen(self):

        openai.api_key = "api key"
        response_img = openai.Image.create(
            prompt=self.question,
            n=self.img_num,
            size=self.img_size
        )
        return response_img['data'][0]['url']

    def idea_gen(self):

        openai.api_key = "api key"
        response_idea = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.question+"and explain the idea of the design",
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response_idea['choices'][0]['text']

    def mood_color_gen(self):

        openai.api_key = "api key"
        response_color = openai.Completion.create(
            model="text-davinci-003",
            prompt="The CSS code for a color like "+self.question,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response_color['choices'][0]['text'][5:12]
