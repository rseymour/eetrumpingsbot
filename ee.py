from twitter import *

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Update your status
t.statuses.update(
    status="")

#-- # Send images along with your tweets:
#-- # - first just read images from the web or from files the regular way:
#-- with open("example.png", "rb") as imagefile:
#--     imagedata = imagefile.read()
#-- # - then upload medias one by one on Twitter's dedicated server
#-- #   and collect each one's id:
#-- t_upload = Twitter(domain='upload.twitter.com',
#--     auth=OAuth(token, token_secret, consumer_key, consumer_secret))
#-- id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
#-- id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
#-- # - finally send your tweet with the list of media ids:
#-- t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))
#-- 
#-- # Or send a tweet with an image (or set a logo/banner similarily)
#-- # using the old deprecated method that will probably disappear some day
#-- params = {"media[]": imagedata, "status": "PTT ★"}
#-- # Or for an image encoded as base64:
#-- params = {"media[]": base64_image, "status": "PTT ★", "_base64": True}
#-- t.statuses.update_with_media(**params)
#-- 
#-- # Attach text metadata to medias sent, using the upload.twitter.com route
#-- # using the _json workaround to send json arguments as POST body
#-- # (warning: to be done before attaching the media to a tweet)
#-- t_upload.media.metadata.create(_json={
#--   "media_id": id_img1,
#--   "alt_text": { "text": "metadata generated via PTT!" }
#-- })
