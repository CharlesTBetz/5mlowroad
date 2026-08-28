---
layout: listen
title: Listen
subtitle: Songs and video from the show.
permalink: /listen/
description: Watch and listen to songs from Five Minutes on the Low Road, a new musical about near-death experience.
---

<p class="page-note">Seeing a security warning or a "sign in to confirm you're not a bot" message in the video players? That's a YouTube restriction, common on shared or public Wi-Fi, not a problem with the site. You can <a href="https://www.youtube.com/playlist?list=PLK-uEjJBX11g">watch the full set directly on YouTube</a> instead.</p>

<!-- Play all: one auto-advancing YouTube playlist of the available videos -->
<section class="section">
  <h2 class="section-heading">Watch the set</h2>
  <p>Play the videos back-to-back, in show order. More are on the way.</p>
  {% include youtube-embed.html id="videoseries" thumb="Y9EvnAL71E4" title="All videos from Five Minutes on the Low Road" params="list=PLK-uEjJBX11g" %}
</section>

{% include divider.html %}

<!-- Individual songs -->
<section class="section">
  <h2 class="section-heading">The songs</h2>
  <p>Songs from <em>Five Minutes on the Low Road</em>, in story order. More videos are on the way.</p>

  {% include song-card.html title="Overture &amp; Leaderboard" description="Tanya the Tiger in all her competitive glory. Executive vice president at PharmaSpan, gunning for the Chief Marketing Officer position. Steve used to be a friend." youtube="Y9EvnAL71E4" id="leaderboard" lyrics="leaderboard" %}
  {% include song-card.html title="Earth Was the Dream" description="On the other side, in a garden where the flowers sing. More real than real… and almost impossible to leave." youtube="QcUStJWsifw" id="earth-was-the-dream" lyrics="earth-was-the-dream" %}
  {% include song-card.html title="This Was You" description="The life review. A guide shows Tanya the consequences of her choices, replayed through the eyes and hearts of everyone she touched. And then, a decision." youtube="3r_wGI2sdbQ" id="this-was-you" lyrics="this-was-you" %}
  {% include song-card.html title="This Side of Tomorrow" description="Tanya's final reflection on her journey and return, and the fundamental transformation wrought on her life in the here and now." youtube="lYIsLwYX9TA" id="this-side-of-tomorrow" lyrics="this-side-of-tomorrow" %}
</section>

{% include divider.html %}

<p class="logline">Want updates as new music is released?</p>
<div class="cta-row">
  <a class="btn btn-primary" href="{{ '/subscribe/' | relative_url }}">Stay in Touch</a>
  <a class="btn btn-secondary" href="https://onthelowroad.substack.com/" target="_blank" rel="noopener">Read the Substack</a>
</div>
