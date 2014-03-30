import cherrypy
from cherrypy import tools
import simplejson as json
import requests

'''
    author: @plamere
    date: 3/30/14

    This is an example token swap service written in python / cherrypy
    This is required by the Spotify iOS SDK to authenticate a user.

    The service relies on the cherrypy and requests libaries to be installed:

    % pip install cherrypy
    % pip install requests

    To run the service, enter your client ID, secret and callback URL
    below and run the program with:

    % python spotify_token_swap.py

    IMPORTANT: You will get authorization failures if you don't insert
    your own client credentials below.

    Once the service is running, pass the public URI to it (such as
    http://localhost:9020/swap) to the token swap method in the
    Spotify iOS SDK:

     NSURL *swapServiceURL = 
        [NSURL # urlWithString:@"http://localhost:9020/swap"];
    
        -[SPAuth handleAuthCallbackWithTriggeredAuthURL:url
               tokenSwapServiceEndpointAtURL:swapServiceURL callback:callback];

Note: For this beta 1 release of the iOS SDK Spotify provides the
above beta values you can use in your Token Exchange Service code; later,
these values will be invalidated and will need to be replaced by your
own unique values.

'''

# CHANGE these values to your own 
k_client_id = "spotify-ios-sdk-beta"
k_client_secret = "ba95c775e4b39b8d60b27bcfced57ba473c10046"
k_client_callback_url = "spotify-ios-sdk-beta://callback"

verbose = True

class SpotifyTokenSwap(object):
    @cherrypy.expose
    @tools.json_out()
    def swap(self, code=None):
        params = {
            'grant_type': 'authorization_code',
            'client_id': k_client_id,
            'client_secret': k_client_secret,
            'redirect_uri': k_client_callback_url,
            'code' : code
        }
        r = requests.post('https://ws.spotify.com/oauth/token', params)
        cherrypy.response.status = r.status_code
        if verbose:
            print
            print code
            print r.status_code
            print r.text
            print
        return r.json()

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*" 


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    root = SpotifyTokenSwap()

    config = {
        'global' : {
            'server.socket_host' : '0.0.0.0',
            'server.socket_port' : 9020,
            'server.thread_pool' : 10,
            # 'environment' : 'production',
        },
        '/' : {
            'tools.CORS.on' : True,
        }
    }
    cherrypy.quickstart(root, '/', config=config)
