# Fake Tweet Data

The data json in this repo includes three different data structures:

- Users
- Hashtags
- Tweets

This data is intentionally only partially normalized. The structures look like this:

```
"data": [
    "tweets": [
        {
            "id": 1,                         # The tweet id
            "user": 1,                       # Posting user's id
            "text": "Remesh is very cool",   # Text of the tweet
            "hashtags": [1, 2],              # ids of associated hashtags
            "retweet_id": null,              # id reference to the parent tweet if this is a retweet or null
            "likes": [1]                     # ids of users who liked this tweet
        }
    ],
    "hashtags": [
        {
            "id": 1,
            "name": "coffeelife"
        },
        { "id": 2, "name": "engineering" }
    ],
    "users": [
        {
            "id": 1,
            "username": "dangineer",
        }
    ]
]
```

While the content of these tweets are randomly generated, the data itself is not fully randomized. There _are_ trends and relationships to find!

Good luck!
