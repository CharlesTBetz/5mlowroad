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
  <p>All the songs currently on video, in show order, one after another. More are on the way.</p>
  {% include youtube-embed.html id="06IxhEzTSMs" title="All videos from Five Minutes on the Low Road" params="playlist=WUdIpjG9AYE" %}
</section>

{% include divider.html %}

<!-- Individual songs -->
<section class="section">
  <h2 class="section-heading">The songs</h2>
  <p>Songs from <em>Five Minutes on the Low Road</em>, in story order. More videos are on the way.</p>

  {% include song-card.html title="Leaderboard" description="The corporate world Tanya rules: driven, competitive, climbing. The life she is about to lose." %}
  {% include song-card.html title="Earth Was the Dream" description="On the other side, in a garden where the flowers sing. More real than real… and almost impossible to leave. Performed by Lia." youtube="06IxhEzTSMs" %}
  {% include song-card.html title="This Was You" description="The life review. A guide shows Tanya the consequences of her choices, replayed through the eyes of everyone she touched." %}
  {% include song-card.html title="This Side of Tomorrow" description="The choice to return, and the promise that follows: a life reclaimed for the here and now." youtube="WUdIpjG9AYE" %}
</section>

{% include divider.html %}

<!-- Concept recording — a future YouTube video weaving the key songs with narrative -->
<section class="section">
  <h2 class="section-heading">The concept recording</h2>
  <p>A longer piece weaving the key songs together with a bit of narrative, the fullest single introduction to the show. Coming soon.</p>
</section>

{% include divider.html %}

<p class="logline">Want updates as new music is released?</p>
<div class="cta-row">
  <a class="btn btn-primary" href="{{ '/subscribe/' | relative_url }}">Stay in Touch</a>
  <a class="btn btn-secondary" href="https://onthelowroad.substack.com/" target="_blank" rel="noopener">Read the Substack</a>
</div>
