---
layout: listen
title: Listen
subtitle: Songs and video from the show.
permalink: /listen/
description: Watch and listen to songs from Five Minutes on the Low Road, a new musical about near-death experience.
---

<!-- Play all: one auto-advancing YouTube playlist of the available videos -->
<section class="section">
  <h2 class="section-heading">Watch the set</h2>
  <p>Play the videos back-to-back, in show order. More are on the way.</p>
  {% include youtube-embed.html id="videoseries" thumb="UOYqIwcR6HE" title="All videos from Five Minutes on the Low Road" params="list=PLK-uEjJBX11g" %}
</section>

{% include divider.html %}

<!-- Individual songs -->
<section class="section">
  <h2 class="section-heading">The songs</h2>
  <p>Songs from <em>Five Minutes on the Low Road</em>, in story order. More videos are on the way.</p>

  {% include song-card.html title="Overture &amp; Leaderboard" description="The corporate world Tanya rules: driven, competitive, climbing. The life she is about to lose." youtube="UOYqIwcR6HE" %}
  {% include song-card.html title="Earth Was the Dream" description="On the other side, in a garden where the flowers sing. More real than real… and almost impossible to leave. Performed by Lia." youtube="06IxhEzTSMs" %}
  {% include song-card.html title="This Was You" description="The life review. A guide shows Tanya the consequences of her choices, replayed through the eyes of everyone she touched." %}
  {% include song-card.html title="This Side of Tomorrow" description="The choice to return, and the promise that follows: a life reclaimed for the here and now." youtube="WUdIpjG9AYE" %}
</section>

{% include divider.html %}

<p class="logline">Want updates as new music is released?</p>
<div class="cta-row">
  <a class="btn btn-primary" href="{{ '/subscribe/' | relative_url }}">Stay in Touch</a>
  <a class="btn btn-secondary" href="https://onthelowroad.substack.com/" target="_blank" rel="noopener">Read the Substack</a>
</div>
