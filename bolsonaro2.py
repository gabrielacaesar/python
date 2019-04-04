import twint

c = twint.Config()

c.Username = "jairbolsonaro"

c.Format = "Tweet id: {id} | Username: {username} | url: {url} | join_date: {join_date} | join_time: {join_time} | tweets: {tweets} | likes: {likes} | media: {media} | private: {private} | verified: {verified} | avatar: {avatar}"

twint.run.Search(c)