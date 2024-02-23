from zhipuai import ZhipuAI

class ChatBot():
    def __init__(self):
        self.model = "glm-4"
        self.api_key="xxx"

        self.init_prompt = "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"

        self.message = [
            {"role": "system", "content": self.init_prompt},

        ]

    def get_user(self, input):
        self.message.append({"role": "user", "content": input})

    def get_response(self):
        client = ZhipuAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model,  # 填写需要调用的模型名称
            messages=self.message,
        )
        res = str(response.choices[0].message).split('role')[0][9:-2]
        self.message.append({"role": "assistant", "content": res})
        return res

    def chat(self, input):
        self.get_user(input)
        res = self.get_response()
        return res

bot = ChatBot()

for i in range(10):
    x = input()
    result = bot.chat(x)
    print(result)