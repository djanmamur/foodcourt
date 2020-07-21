# Posts

### Model
    name - Name of the post (max 255 characters)
    description - Description of Post (models.TextField)
    price - Post price (integer)
    owner - User who owns/created this Post

**Create a new Post**:

`POST` `/api/v1/posts/`

Owner of the Post must be specified

`Request Body`
```

{
    "name": "Amazon Alexa",
    "description": "Amazon voice helper",
    "price": 12000,
    "owner": "dcffd1f8-964e-469c-84b6-c394a25b4b0e"
}
```

**Delete existing Post**:

`DELETE` `/api/v1/posts/64fca7af-bb84-4868-a2ae-0b0f4f86fcbf`

`Headers`
```
Authorization: Token 684193fee0760acf69a75bb8a5764b391295bf78
```



