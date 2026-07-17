---
layout: listen
title: Listen
subtitle: A narrated story with original songs.
permalink: /listen/
description: Listen to Five Minutes on the Low Road — a narrated story with original songs. About twenty minutes.
---

<!-- Podcast player -->
<section class="section">
  <h2 class="section-heading">The Full Audio Experience</h2>
  <p>Narrated story with original songs. About twenty minutes.</p>
  <div class="podcast-embed">
    <!-- PODCAST_PLAYER_EMBED_HERE: paste iframe from Buzzsprout/Transistor/etc -->
    <p class="podcast-placeholder">Podcast player coming soon.</p>
  </div>
</section>

{% include divider.html %}

<!-- Individual songs -->
<section class="section">
  <h2 class="section-heading">Individual Songs</h2>

  {% include song-card.html title="Leaderboard" src="/assets/audio/leaderboard.mp3" description="The corporate world Tanya rules — driven, competitive, climbing. The life she is about to lose." %}
  {% include song-card.html title="This Was You" src="/assets/audio/this-was-you.mp3" description="The life review. A guide shows Tanya the consequences of her choices, replayed through the eyes of everyone she touched." %}
  {% include song-card.html title="Earth Was the Dream" src="/assets/audio/earth-was-the-dream.mp3" description="On the other side, in a garden where the flowers sing. More real than real — and almost impossible to leave." %}
  {% include song-card.html title="This Side of Tomorrow" src="/assets/audio/this-side-of-tomorrow.mp3" description="The choice to return, and the promise that follows: a life reclaimed for the here and now." %}
</section>

{% include divider.html %}

<p class="logline">Want updates as new music is released?</p>
<div class="cta-row">
  <a class="btn btn-primary" href="{{ '/subscribe/' | relative_url }}">Stay in Touch</a>
</div>
