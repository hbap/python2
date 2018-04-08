import html
import os

from twython import Twython
from twython import TwythonAuthError, TwythonError, TwythonRateLimitError


def get_user_timeline(screen_name, count=200):
    """Return list of most recent tweets posted by screen_name."""

    # Ensure count is valid
    if count < 1 or count > 200:
        raise RuntimeError("invalid count")

    # Ensure environment variables are set
    if not os.environ.get("API_KEY"):
        raise RuntimeError("API_KEY not set")
    if not os.environ.get("API_SECRET"):
        raise RuntimeError("API_SECRET not set")

    # Get screen_name's (or @screen_name's) most recent tweets
    # https://dev.twitter.com/rest/reference/get/users/lookup
    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline
    # https://github.com/ryanmcgrath/twython/blob/master/twython/endpoints.py
    try:
        twitter = Twython(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
        user = twitter.lookup_user(screen_name=screen_name.lstrip("@"))
        if user[0]["protected"]:
            return None
        tweets = twitter.get_user_timeline(screen_name=screen_name, count=count, tweet_mode="extended")
        return [html.unescape(tweet["full_text"].replace("\n", " ")) for tweet in tweets]
    except TwythonAuthError as e:
        raise RuntimeError("invalid API_KEY and/or API_SECRET") from None
    except TwythonRateLimitError:
        raise RuntimeError("you've hit a rate limit") from None
    except TwythonError:
        return None
