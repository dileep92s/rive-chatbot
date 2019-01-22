from flask import Flask
from flask_restful import Resource, Api, reqparse
from rivescript import RiveScript

app = Flask(__name__)
api = Api(app)

class RestBot(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        req = args["query"]
        res = bot.reply("localuser", req)
        res = {"res":res, "req":req}
        return res

api.add_resource(RestBot, '/req')

if __name__ == '__main__':
    
    bot = RiveScript()
    bot.load_file("brain.rive")
    bot.sort_replies()

    parser = reqparse.RequestParser()
    parser.add_argument('query', type=str)

    app.run(port=7878, debug=True)
    