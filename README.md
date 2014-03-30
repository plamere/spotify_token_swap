# spotify_token_swap.py

    author: @plamere
    date: 3/30/14

This is an example token swap service written in python / cherrypy
This is required by the Spotify iOS SDK to authenticate a user.

See the [Spotify iOS SDK](https://developer.spotify.com/technologies/spotify-ios-sdk/) for details about the Spotify iOS SDK and the role of the token swap service has in your iOS app.

## Dependencies

The service relies on the cherrypy and requests libaries to be installed:

    % pip install cherrypy
    % pip install requests

## Configuration
IMPORTANT: You will get authorization failures if you don't insert
your own client credentials. To configure your server, edit
spotify_token_swap.py and change the following config variables 
to match the values for your app:

    k_client_id = "spotify-ios-sdk-beta"
    k_client_secret = "ba95c775e4b39b8d60b27bcfced57ba473c10046"
    k_client_callback_url = "spotify-ios-sdk-beta://callback"

Note: For this beta 1 release of the iOS SDK Spotify provides the following
beta values you can use in your Token Exchange Service code; later,
these values will be invalidated and will need to be replaced by your
own unique values.

## Running 
To run the service, enter your client ID, secret and callback URL
below and run the program with:

    % python spotify_token_swap.py

## Using the swap service in your iOS code
Once the service is running, pass the public URI to it (such as
http://localhost:9020/swap) to the token swap method in the
Spotify iOS SDK:

    NSURL *swapServiceURL =
       [NSURL # urlWithString:@"http://localhost:9020/swap"];

    -[SPAuth handleAuthCallbackWithTriggeredAuthURL:url
           tokenSwapServiceEndpointAtURL:swapServiceURL callback:callback];
