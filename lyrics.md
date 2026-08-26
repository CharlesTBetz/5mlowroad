---
layout: page
title: Lyrics
description: Read the lyrics to the songs of Five Minutes on the Low Road.
permalink: /lyrics/
---

<p class="lead">Read the words. The songs, in show order.</p>

<ul class="lyric-index">
{% assign songs = site.lyrics | sort: "order" %}
{% for song in songs %}
  <li><a href="{{ song.url | relative_url }}">{{ song.title }}</a>{% if song.scene %} <span class="lyric-index-scene">{{ song.scene }}</span>{% endif %}</li>
{% endfor %}
</ul>
