# jsonry
python program to give a json object based on input string


jsonry
----
### About
Console application to transform a message string into a JSON string of it's special contents.  In particular we are searching for 3 elements:

#### Mentions
These are substrings of the format `@handle` where `handle` represents some username.  In the JSON response the format will look like:

```json
{"mentions": ["username"]}
```

#### Emoticons
These are substrings of the format `(emoticon)` where `emoticon` represents the actual emoticon to be displayed.  In the JSON response the format will look like:

```json
{"emoticons": ["emoticon"]}
```

#### Links
These substrings are any properly formatted URL.  In the JSON response we want to capture not only the URL, but also the title of the page that URL represents, the response object will look like:

```json
{"links": [{"url": "url", "title": "title"}]}
```

### Example
A full example of a parsed string would be the following:

Input: `@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016`

Output (as a string): 

```json
{
  "mentions": [
    "bob",
    "john"
  ],
  "emoticons": [
    "success"
  ],
  "links": [
    {
      "url": "http://www.twitter.com/jdorfman/status/430511497475670016",
      "title": "Justin Dorfman on Twitter: \"nice @littlebigdetail from @HipChat (shows hex colors when pasted in chat). http://t.co/7cI6Gjy5pq\""
    }
  ]
}
```