---
template: home.html
title: ZugBot — Guild operations for Discord
description: Your World of Warcraft guild's extra pair of hands. Plan events, link characters, build Mythic+ groups, and manage your guild inside Discord.
hide:
  - navigation
  - toc
---

<section class="zb-hero" aria-labelledby="hero-title">
  <img class="zb-hero-art" src="assets/zugbot-fortress.webp" width="1536" height="1024" fetchpriority="high" alt="ZugBot, a heavily armored mechanical orc with glowing eyes, cables, and red cloth, holding an operations tablet in a burning fortress.">
  <div class="zb-shell zb-hero-inner">
    <div class="zb-hero-copy">
      <p class="zb-eyebrow">World of Warcraft · Discord</p>
      <h1 id="hero-title">Less admin.<br><span>More Warcraft.</span></h1>
      <p class="zb-lead">Your guild's extra pair of hands.</p>
      <p class="zb-hero-description">Raid night. Key groups. A whole warband of alts. ZugBot handles the busywork so your guild can get back to playing.</p>
      <div class="zb-actions">
        <a class="zb-button zb-button-primary" href="getting-started/">Get started with ZugBot</a>
        <a class="zb-button" href="#features">Explore features</a>
      </div>
      <p class="zb-hero-note">Built for guilds. Runs inside Discord.</p>
    </div>
  </div>
</section>

<nav class="zb-capabilities" aria-label="Feature guides">
  <div class="zb-shell">
    <a href="planner/">Guild Planner</a>
    <a href="member-guide/">Characters &amp; Warbands</a>
    <a href="member-guide/">Mythic+ Groups</a>
    <a href="member-guide/">Smart LFG</a>
    <a href="admin-guide/">Guild Administration</a>
  </div>
</nav>

<section class="zb-section zb-planner" id="features" aria-labelledby="planner-title">
  <div class="zb-shell zb-split">
    <div class="zb-section-copy">
      <p class="zb-eyebrow">01 / Get the guild together</p>
      <h2 id="planner-title">A raid night.<br>A plan.<br><em>Everyone in the loop.</em></h2>
      <p>Create your event, let members choose their roles, and see your roster take shape. ZugBot keeps the Planner card and Discord Scheduled Event together.</p>
      <ul class="zb-detail-list">
        <li>Tank, Healer, DPS, and Bench signups</li>
        <li>Event times in each member's local timezone</li>
        <li>Persistent cards that work after a bot restart</li>
      </ul>
      <a class="zb-text-link" href="planner/">Explore Guild Planner</a>
    </div>
    <figure class="zb-planner-preview">
      <figcaption>Example Planner card</figcaption>
      <div class="zb-discord-channel"># raid-and-events</div>
      <div class="zb-message-header">
        <img src="assets/zugbot-logo-v2.svg" alt="" width="40" height="40" loading="lazy">
        <strong>ZugBot</strong><span class="zb-app-tag">APP</span>
      </div>
      <div class="zb-event-embed">
        <p class="zb-event-type">Guild Planner · Raid</p>
        <h3>Friday Raid Night</h3>
        <p>Bring your flasks. We've got bosses to pull.</p>
        <div class="zb-event-meta"><div><span>Starts</span><strong>Friday · 8:00 PM</strong></div><div><span>Composition</span><strong>2 Tank · 4 Healer · 11 DPS</strong></div></div>
        <div class="zb-event-roster"><p><strong>Tanks</strong><span>@GuildMember · @GuildMember</span></p><p><strong>Healers</strong><span>@GuildMember · +3 more</span></p><p><strong>DPS</strong><span>@GuildMember · +10 more</span></p></div>
      </div>
      <div class="zb-rsvp-examples" aria-label="Example RSVP options"><span>Tank</span><span>Healer</span><span>DPS</span><span>Bench</span><span>Maybe</span><span>Can't Attend</span></div>
      <p class="zb-preview-note">Illustrative example. Actual events run in your Discord server.</p>
    </figure>
  </div>
</section>

<section class="zb-section zb-tools" aria-labelledby="tools-title">
  <div class="zb-shell">
    <div class="zb-section-heading"><p class="zb-eyebrow">The rest of the guild comes with it</p><h2 id="tools-title">One bot. A lot less busywork.</h2></div>
    <div class="zb-tool-grid">
      <article class="zb-tool"><span class="zb-tool-number">02</span><div><h3>Characters &amp; Warbands</h3><p>Your main, your alts, your identity. Link your characters once and keep them together across ZugBot's member workflows.</p><a class="zb-text-link" href="member-guide/">Meet your warband</a></div></article>
      <article class="zb-tool"><span class="zb-tool-number">03</span><div><h3>Mythic+ Groups</h3><p>Build a group with role slots, linked characters, and PUG controls. Keep organizing the next key right where your guild already talks.</p><a class="zb-text-link" href="commands/">See group commands</a></div></article>
      <article class="zb-tool"><span class="zb-tool-number">04</span><div><h3>Smart LFG</h3><p>Reach members interested in the roles and key ranges you're running. Members choose their notifications, so every group doesn't need an everyone ping.</p><a class="zb-text-link" href="member-guide/">Find your next group</a></div></article>
      <article class="zb-tool"><span class="zb-tool-number">05</span><div><h3>Guild Administration</h3><p>Set up your channels, map your guild's authority roles, and welcome newcomers with a persistent rules agreement. Your server, your structure.</p><a class="zb-text-link" href="admin-guide/">Open the admin guide</a></div></article>
    </div>
  </div>
</section>

<section class="zb-section zb-start" aria-labelledby="start-title">
  <div class="zb-shell zb-start-inner">
    <div><p class="zb-eyebrow">Put ZugBot to work</p><h2 id="start-title">Your guild has enough<br>bosses to deal with.</h2><p>Start with setup. Link your characters. Plan the next run.</p><div class="zb-actions"><a class="zb-button zb-button-primary" href="getting-started/">Read the setup guide</a><a class="zb-button" href="commands/">Browse commands</a></div></div>
    <div class="zb-operating-notes"><p><strong>Discord is the interface.</strong><span>Buttons, selectors, and event cards. No extra dashboard for members to check.</span></p><p><strong>Your guild stays your guild.</strong><span>Server-specific configuration, authority roles, and operational data.</span></p><p><strong>Built for the next login.</strong><span>Persistent groups and event cards recover after restarts.</span></p></div>
  </div>
</section>

<section class="zb-support" id="support" aria-labelledby="support-title">
  <div class="zb-shell zb-support-inner"><div><p class="zb-eyebrow">Independent development</p><h2 id="support-title">Help keep ZugBot moving.</h2><p>Support covers infrastructure, development tools, and the next round of guild features.</p></div><div class="zb-actions"><a class="zb-button" href="https://buymeacoffee.com/ZugBot" target="_blank" rel="noopener noreferrer">One-time support</a><a class="zb-text-link" href="https://patreon.com/ZugBot" target="_blank" rel="noopener noreferrer">Monthly support</a></div></div>
</section>

<footer class="zb-footer"><div class="zb-shell"><a class="zb-footer-brand" href="./"><img src="assets/zugbot-logo-v2.svg" alt="" width="32" height="32" loading="lazy"><strong>ZugBot</strong></a><p>Guild operations for Discord.</p><nav aria-label="Footer"><a href="roadmap/">Roadmap</a><a href="changelog/">Changelog</a><a href="troubleshooting/">Get help</a></nav></div></footer>
