from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_post_args.add_argument("views", type=int, help="Views of the video")
video_post_args.add_argument("likes", type=int, help="Likes in the video")

videos = {}

def abort_if_video_id_doesnt_exists(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video.")

def abort_if_video_id_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already existis with that ID.")

    
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exists(video_id)
        return videos[video_id]
    
    def post(self, video_id):
        abort_if_video_id_exists(video_id)

        args = video_post_args.parse_args()
        
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exists(video_id)

        del videos[video_id]
        return '', 204

api.add_resource(Video, "/video/<int:video_id>") 

if __name__ == "__main__":
    app.run(debug=True)