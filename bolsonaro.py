import twint

c = twint.Config()

c.Username = "jairbolsonaro"
c.Store_csv = True
# details
c.Custom["id"] = ["id"]
c.Custom["conversation_id"] = ["conversation_id"]
c.Custom["created_at"] = ["created_at"]
c.Custom["date"] = ["date"]
c.Custom["time"] = ["time"]
c.Custom["timezone"] = ["timezone"]
c.Custom["user_id"] = ["user_id"]
c.Custom["username"] = ["username"]
c.Custom["name"] = ["name"]
c.Custom["place"] = ["place"]
c.Custom["tweet"] = ["tweet"]
c.Custom["mentions"] = ["mentions"]
c.Custom["urls"] = ["urls"]
c.Custom["photos"] = ["photos"]
c.Custom["replies_count"] = ["replies_count"]
c.Custom["retweets_count"] = ["retweets_count"]
c.Custom["likes_count"] = ["likes_count"]
c.Custom["location"] = ["location"]
c.Custom["hashtags"] = ["hashtags"]
c.Custom["link"] = ["link"]
c.Custom["retweet"] = ["retweet"]
c.Custom["quote_url"] = ["quote_url"]
c.Custom["video"] = ["video"]

c.Output = "twitter"

twint.run.Search(c)