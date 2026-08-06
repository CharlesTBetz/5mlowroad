---
layout: page
title: Contact
description: For industry inquiries, press, and collaboration.
permalink: /contact/
---

For industry inquiries, press, and collaboration.

Direct email: [hello@5minlowroad.com](mailto:hello@5minlowroad.com)

<!-- Formspree contact form. Submissions are delivered to the address configured in
     Formspree (currently char@charlestbetz.com) — changing the mailto above does not
     reroute the form. Update the destination in the Formspree dashboard if wanted. -->

<form class="contact-form" action="https://formspree.io/f/mbdnoall" method="POST">
  <div class="form-field">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" required>
  </div>
  <div class="form-field">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>
  </div>
  <div class="form-field">
    <label for="message">Message</label>
    <textarea id="message" name="message" required></textarea>
  </div>
  <button class="btn btn-primary" type="submit">Send</button>
</form>
