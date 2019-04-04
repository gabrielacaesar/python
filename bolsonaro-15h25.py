import twint

c = twint.Config()

c.Username = "jairbolsonaro"

c.Format = "Tweet_id: {id} | date: {date} | join_date: {join_date} | join_time: {join_time} | time: {time} | timezone: {timezone} | Username: {username} | tweet: {tweet} | hashtag: {hashtags} | url: {url} | replies: {replies} | retweet: {retweets} | likes: {likes} | link: {link} | is_retweet: {is_retweet} | user_rt: {user_rt} | mentions: {mentions} | media: {media} | private: {private} | verified: {verified} | avatar: {avatar}"

twint.run.Search(c)


