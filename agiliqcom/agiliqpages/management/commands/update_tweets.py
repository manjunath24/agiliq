
from django.conf import settings
from django.core.management.base import NoArgsCommand

from bettertwitter import Twitter
from agiliqpages.models import Tweet

class Command(NoArgsCommand):
    help = 'Update the tweets of user'

    def handle_noargs(self, **options):
        twitter = Twitter(email=settings.TWITTER_API_USER, password=settings.TWITTER_API_PASSW)
        
        for scr_name in settings.TWITTER_FOLLOW:
            user_tweets = twitter.statuses.user_timeline(screen_name=scr_name)
            for tweet in user_tweets:
                Tweet.objects.create(screen_name = tweet['user']['screen_name']
                                     text=tweet['text'])
            
