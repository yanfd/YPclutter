from atproto import Client
import os


BS_ACCOUNT = {
    "ACCOUNT": os.environ.get("bs_account"),
    "PWD": os.environ.get("bs_pwd"),
}
client = Client()
client.login(BS_ACCOUNT["ACCOUNT"], BS_ACCOUNT["PWD"])
post = client.send_post('testing with hidden.')
post.uri  # at://did:plc:abc123..../app.bsky.feed.post/xyz...
post.cid  # abc...

