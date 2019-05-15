# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

initial_data = [
    {
        "pk": 1,
        "regex": "https?://\\S*?flickr.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://www.flickr.com/services/oembed/",
        "name": "Flickr",
        "format": 1
    },
    {
        "pk": 2,
        "regex": "https?://\\S*?viddler.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://lab.viddler.com/services/oembed/",
        "name": "Viddler",
        "format": 1
    },
    {
        "pk": 3,
        "regex": "https?://qik.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://qik.com/api/oembed.json",
        "name": "Qik",
        "format": 1
    },
    {
        "pk": 4,
        "regex": "https?://\\S*?pownce.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://api.pownce.com/2.1/oembed.json",
        "name": "Pownce",
        "format": 1
    },
    {
        "pk": 5,
        "regex": "https?://\\S*?revision3.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://revision3.com/api/oembed/",
        "name": "Revision3",
        "format": 1
    },
    {
        "pk": 6,
        "regex": "https?://\\S*.collegehumor.com/video:[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://oohembed.com/oohembed/",
        "name": "CollegeHumor Video (OohEmbed)",
        "format": 1
    },
    {
        "pk": 7,
        "regex": "https?://\\S*.funnyordie.com/videos/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://oohembed.com/oohembed/",
        "name": "Funny or Die Video (OohEmbed)",
        "format": 1
    },
    {
        "pk": 8,
        "regex": "https?://video.google.com/videoplay?[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://oohembed.com/oohembed/",
        "name": "Google Video (OohEmbed)",
        "format": 1
    },
    {
        "pk": 9,
        "regex": "https?://www.hulu.com/watch/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://oohembed.com/oohembed/",
        "name": "Hulu (OohEmbed)",
        "format": 1
    },
    {
        "pk": 10,
        "regex": "https?://\\S*.metacafe.com/watch/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://oohembed.com/oohembed/",
        "name": "Metacafe (OohEmbed)",
        "format": 1
    },
    {
        "pk": 11,
        "regex": "https?://twitter.com/\\S*/status(es)?/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.twitter.com/1/statuses/oembed.json",
        "name": "Twitter Status",
        "format": 1
    },
    {
        "pk": 12,
        "regex": "https?://\\S*.wikipedia.org/wiki/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://oohembed.com/oohembed/",
        "name": "Wikipedia (OohEmbed)",
        "format": 1
    },
    {
        "pk": 13,
        "regex": "(https?://\\S*.?youtube.com/watch[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://youtu.be/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://www.youtube.com/oembed?scheme=https",
        "name": "YouTube",
        "format": 1
    },
    {
        "pk": 14,
        "regex": "https?://vimeo.com/.*\\d+",
        "endpoint": "https://vimeo.com/api/oembed.json",
        "name": "Vimeo",
        "format": 1
    },
    {
        "pk": 15,
        "regex": "https?://www.slideshare.net/\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "SlideShare (Embedly)",
        "format": 1
    },
    {
        "pk": 16,
        "regex": "https?://\\S*.scribd.com/doc/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Scribd (Embedly)",
        "format": 1
    },
    {
        "pk": 17,
        "regex": "https?://screenr.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Screenr (Embedly)",
        "format": 1
    },
    {
        "pk": 18,
        "regex": "https?://www.5min.com/Video/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "5min (Embedly)",
        "format": 1
    },
    {
        "pk": 19,
        "regex": "https?://www.howcast.com/videos/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Howcast (Embedly)",
        "format": 1
    },
    {
        "pk": 20,
        "regex": "(https?://\\S*?screencast.com/\\S*/media/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*?screencast.com/t/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Screencast (Embedly)",
        "format": 1
    },
    {
        "pk": 21,
        "regex": "https?://www.clearspring.com/widgets/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Clearspring (Embedly)",
        "format": 1
    },
    {
        "pk": 22,
        "regex": "(https?://my.opera.com/\\S*/albums/show.dml\\?id=[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://my.opera.com/\\S*/albums/showpic.dml\\?album=\\S*&picture=[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "My Opera (Embedly)",
        "format": 1
    },
    {
        "pk": 23,
        "regex": "https?://\\S*yfrog.\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Yfrog (Embedly)",
        "format": 1
    },
    {
        "pk": 24,
        "regex": "https?://tweetphoto.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "TweetPhoto (Embedly)",
        "format": 1
    },
    {
        "pk": 25,
        "regex": "https?://\\S*twitpic.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "TwitPic (Embedly)",
        "format": 1
    },
    {
        "pk": 26,
        "regex": "https?://\\S*imgur.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Imgur (Embedly)",
        "format": 1
    },
    {
        "pk": 27,
        "regex": "https?://twitgoo.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "TwitGoo (Embedly)",
        "format": 1
    },
    {
        "pk": 28,
        "regex": "(https?://i\\S*.photobucket.com/albums/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://gi\\S*.photobucket.com/groups/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Photobucket (Embedly)",
        "format": 1
    },
    {
        "pk": 29,
        "regex": "https?://phodroid.com/\\S*/\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Phodroid (Embedly)",
        "format": 1
    },
    {
        "pk": 30,
        "regex": "https?://xkcd.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "xkcd (Embedly)",
        "format": 1
    },
    {
        "pk": 31,
        "regex": "https?://\\S*?23hq.com/\\S*/photo/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "23 HQ (Embedly)",
        "format": 1
    },
    {
        "pk": 32,
        "regex": "(https?://\\S*amazon.\\S*/gp/product/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*amazon.\\S*/\\S*/dp/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*amazon.\\S*/dp/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*amazon.\\S*/o/ASIN/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*amazon.\\S*/gp/offer-listing/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*amazon.\\S*/\\S*/ASIN/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*amazon.\\S*/gp/product/images/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Amazon (Embedly)",
        "format": 1
    },
    {
        "pk": 33,
        "regex": "https?://www.veoh.com/\\S*/watch/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Veoh (Embedly)",
        "format": 1
    },
    {
        "pk": 34,
        "regex": "https?://\\S*justin.tv/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Justin.tv (Embedly)",
        "format": 1
    },
    {
        "pk": 35,
        "regex": "https?://www.ustream.tv/(recorded|channel)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "UStream (Embedly)",
        "format": 1
    },
    {
        "pk": 36,
        "regex": "(https?://\\S*.dailymotion.com/video/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://\\S*.dailymotion.com/\\S*/video/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Daily Motion (Embedly)",
        "format": 1
    },
    {
        "pk": 37,
        "regex": "https?://www.twitvid.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "TwitVid (Embedly)",
        "format": 1
    },
    {
        "pk": 38,
        "regex": "https?://www.break.com/\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Break.com (Embedly)",
        "format": 1
    },
    {
        "pk": 39,
        "regex": "https?://(www|vids).myspace.com/index.cfm\\?fuseaction=\\S*&videoid[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Myspace Videos (Embedly)",
        "format": 1
    },
    {
        "pk": 40,
        "regex": "https?://\\S*blip.tv/file/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://blip.tv/oembed",
        "name": "Blip.tv",
        "format": 1
    },
    {
        "pk": 41,
        "regex": "https?://\\S*revver.com/video/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Revver (Embedly)",
        "format": 1
    },
    {
        "pk": 42,
        "regex": "(https?://video.yahoo.com/watch/\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://video.yahoo.com/network/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Yahoo! Video (Embedly)",
        "format": 1
    },
    {
        "pk": 43,
        "regex": "https?://\\S*?liveleak.com/view?[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "LiveLeak (Embedly)",
        "format": 1
    },
    {
        "pk": 44,
        "regex": "https?://animoto.com/(play|s)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Animoto (Embedly)",
        "format": 1
    },
    {
        "pk": 45,
        "regex": "https?://dotsub.com/view/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "dotSUB (Embedly)",
        "format": 1
    },
    {
        "pk": 46,
        "regex": "https?://soundcloud.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "SoundCloud (Embedly)",
        "format": 1
    },
    {
        "pk": 47,
        "regex": "https?://www.lala.com/#*(album|song)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Lala (Embedly)",
        "format": 1
    },
    {
        "pk": 48,
        "regex": "(https?://movieclips.com/watch/\\S*/\\S*/|https?://movieclips.com/watch/\\S*/\\S*/\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Movie Clips (Embedly)",
        "format": 1
    },
    {
        "pk": 49,
        "regex": "https?://\\S*crackle.com/c/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Crackle (Embedly)",
        "format": 1
    },
    {
        "pk": 50,
        "regex": "https?://www.fancast.com/\\S*/videos",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Fancast (Embedly)",
        "format": 1
    },
    {
        "pk": 51,
        "regex": "https?://www.ted.com/talks/\\S*.html",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "TED (Embedly)",
        "format": 1
    },
    {
        "pk": 52,
        "regex": "https?://\\S*omnisio.com/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Omnisio (Embedly)",
        "format": 1
    },
    {
        "pk": 53,
        "regex": "https?://\\S*nfb.ca/film/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "NFB (Embedly)",
        "format": 1
    },
    {
        "pk": 54,
        "regex": "(https?://www.thedailyshow.com/(watch|full-episodes)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*|https?://www.thedailyshow.com/collection/\\S*/\\S*/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*)",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "The Daily Show (Embedly)",
        "format": 1
    },
    {
        "pk": 55,
        "regex": "https?://movies.yahoo.com/movie/\\S*/(video|info|trailer)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Yahoo! Movies",
        "format": 1
    },
    {
        "pk": 56,
        "regex": "https?://www.colbertnation.com/(the-colbert-report-collections|full-episodes|the-colbert-report-videos)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Colbert Nation (Embedly)",
        "format": 1
    },
    {
        "pk": 57,
        "regex": "https?://www.comedycentral.com/videos/index.jhtml?[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Comedy Central (Embedly)",
        "format": 1
    },
    {
        "pk": 58,
        "regex": "https?://\\S*theonion.com/video/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "The Onion (Embedly)",
        "format": 1
    },
    {
        "pk": 59,
        "regex": "https?://wordpress.tv/\\S*/\\S*/\\S*/\\S*/",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "WordPress TV (Embedly)",
        "format": 1
    },
    {
        "pk": 60,
        "regex": "https?://www.traileraddict.com/(trailer|clip|poster)/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "Trailer Addict (Embedly)",
        "format": 1
    },
    {
        "pk": 61,
        "regex": "https?://www.escapistmagazine.com/videos/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "https://api.embed.ly/v1/api/oembed",
        "name": "The Escapist (Embedly)",
        "format": 1
    },
    {
        "pk": 62,
        "regex": "https?://official\\.fm/[\\w\\-\\.~%/\\?#@!$&'\\(\\)\\*\\+,;=]*",
        "endpoint": "http://official.fm/services/oembed",
        "name": "official.fm",
        "format": 1
    },
    {
        "pk": 63,
        "regex": "https?://www\\.facebook\\.com/\\S*/videos/\\d+/?",
        "endpoint": "https://www.facebook.com/plugins/video/oembed.json",
        "name": "Facebook Video",
        "format": 1
    }
]

def create_fixtures(apps, schema_editor):
    ProviderRule = apps.get_model('oembed', 'ProviderRule')
    for rule_data in initial_data:
        ProviderRule.objects.get_or_create(
            pk=rule_data['pk'],
            defaults=rule_data,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('oembed', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_fixtures)
    ]
