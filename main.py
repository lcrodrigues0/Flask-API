from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

vide_post_args = reqparse.RequestParser()
vide_post_args.add_argument("name", type=str, help="Name of the video is required", required=True)
vide_post_args.add_argument("views", type=int, help="Views of the video")
vide_post_args.add_argument("likes", type=int, help="Likes in the video")

videos = {}

def check_video_id(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video.")

    
class Video(Resource):
    def get(self, video_id):
        check_video_id(video_id)
        return videos[video_id]
    
    def post(self, video_id):
        args = vide_post_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>") 

if __name__ == "__main__":
    app.run(debug=True)