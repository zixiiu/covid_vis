import tweepy
from API_KEY import *

def send(text, imageFlag , replyId = None):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    # Upload image
    if imageFlag == 'confirmed':
        media = api.media_upload("./Graph/confirmed.png")
    if imageFlag == 'deaths':
        media = api.media_upload("./Graph/deaths.png")
    else:
        raise ValueError('wrong keyword!')

    # Post tweet with image
    if not replyId:
        post_result = api.update_status(status=text, media_ids=[media.media_id])
    else:
        post_result = api.update_status(status=text, media_ids=[media.media_id], in_reply_to_status_id = replyId)





