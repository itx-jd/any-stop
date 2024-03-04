from flask import Flask, jsonify
import yt_dlp

app = Flask(__name__)

# YouTube functions

def get_video_info(url):
    ydl_opts = {
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get('url')
           
            return {'success': True,'video_url': video_url}

        except yt_dlp.utils.DownloadError as e:
            return {'success': False, 'error_message': str(e)}

# Flask routes

@app.route('/<path:video_url>', methods=['GET'])
def get_video_info_endpoint(video_url):
    
    if video_url.lower() == 'favicon.ico':
        # Handle favicon.ico request (return an empty response or your favicon)
        return ''

    result = get_video_info(video_url)

    if 'error_message' in result:
        response_data = {
            'success': False,
            'error_message': result['error_message']
        }
    else:
        response_data = {
            'success': True,
            'video_url': result['video_url']
        }
    
    return jsonify(response_data)

# Run the Flask app

if __name__ == '__main__':
    app.run(debug=True)
