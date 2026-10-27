# -*- coding: utf-8 -*-
"""Generates the NewsBreak FE test pages /final-expense/today/ and /final-expense/now/.
Run: python build_fe_pages.py (from this folder)."""
import io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

TEL = 'tel:+18336314698'
PHONE = '(833) 631-4698'

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="/images/NBIP.png">
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ background:#f4f1ea; color:#222; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; padding-bottom:84px; }}
  .label {{ background:#e9e5da; color:#555; font:600 .72rem/1 inherit; letter-spacing:.08em; text-transform:uppercase; text-align:center; padding:.45rem; }}
  .top {{ background:#fff; border-bottom:1px solid #e2ddd0; text-align:center; padding:.6rem; }}
  .top img {{ height:44px; width:auto; }}
  .hero {{ max-width:640px; margin:0 auto; background:#fff; padding:1.5rem 1.25rem 1.25rem; text-align:center; }}
  .who {{ display:inline-block; background:#e8f7f4; color:#1d6b5f; font-weight:700; font-size:.95rem; padding:.35rem .8rem; border-radius:99px; margin-bottom:.75rem; }}
  h1 {{ font-size:2rem; line-height:1.15; color:#111; margin-bottom:.6rem; }}
  .dek {{ font-size:1.2rem; line-height:1.45; color:#333; margin-bottom:1.1rem; }}
  .checks {{ list-style:none; text-align:left; display:inline-block; font-size:1.12rem; line-height:1.9; margin-bottom:1rem; }}
  .checks li {{ display:flex; align-items:baseline; }}
  .checks li::before {{ content:"\\2713"; color:#2fbdaa; font-weight:900; margin-right:.55rem; flex:none; }}
  .cta {{ display:block; background:#2fbdaa; color:#fff; text-decoration:none; font-weight:800; font-size:1.35rem; line-height:1.2; padding:1.15rem 1rem; border-radius:12px; box-shadow:0 6px 16px rgba(47,189,170,.4); text-align:center; margin:1rem 0 .4rem; }}
  .cta small {{ display:block; font-weight:600; font-size:.9rem; opacity:.95; margin-top:.25rem; }}
  .note {{ font-size:.85rem; color:#666; text-align:center; }}
  .body {{ max-width:640px; margin:0 auto; background:#fff; padding:.5rem 1.25rem 2rem; font-size:1.12rem; line-height:1.6; }}
  h2 {{ font-size:1.35rem; color:#1d3d6b; margin:1.75rem 0 .6rem; }}
  p {{ margin-bottom:1rem; }}
  .big {{ background:#fff7e6; border-left:5px solid #e0a100; padding:1rem; font-size:1.15rem; margin:1rem 0; }}
  .steps {{ padding-left:1.4rem; margin-bottom:1.25rem; }}
  .steps li {{ margin-bottom:.5rem; }}
  .foot {{ max-width:640px; margin:0 auto; padding:1.25rem; font-size:.78rem; line-height:1.5; color:#666; text-align:center; }}
  .foot a {{ color:#666; }}
  .bar {{ position:fixed; left:0; right:0; bottom:0; background:#1d3d6b; color:#fff; text-decoration:none; text-align:center; font-weight:800; font-size:1.2rem; line-height:1; padding:1.15rem 1rem calc(1.15rem + env(safe-area-inset-bottom)); box-shadow:0 -4px 12px rgba(0,0,0,.2); }}
  @media (max-width:600px) {{ h1 {{ font-size:1.7rem; }} }}
</style>
<script>
  // CallGrid dynamic number insertion (campaign "NBIP FE NewsBreak", source "NBIP NewsBreak").
  // URL parameters (utm_*, nb_cid, callback) are captured automatically; landing_page is passed as a tag.
  (function () {{
    var s = document.createElement('script');
    s.src = 'https://cdn.callgrid.com/callgrid.js';
    s.async = true;
    s.dataset.organizationId = 'cmqa4hp8c003x06k5iu7c2c0r';
    s.dataset.campaignSourceId = 'cmvpmb7u403fm06ibc50q4my2';
    s.dataset.targetPhoneNumber = '8336314698';
    s.dataset.tags = JSON.stringify({{ landing_page: '{page}' }});
    document.head.appendChild(s);
  }})();
  // A tap before the pool number arrives would dial the untracked backup number.
  // Hold that tap for up to 1.5s until CallGrid assigns a number, then dial.
  document.addEventListener('callgrid:numberAssigned', function (e) {{ window.__cgNum = e.detail && e.detail.phoneNumber; }});
  document.addEventListener('click', function (ev) {{
    var a = ev.target.closest && ev.target.closest('a[href^="tel:"]');
    if (!a || window.__cgNum || /8336314698/.test(a.getAttribute('href')) === false) return;
    ev.preventDefault();
    var done = false, go = function () {{ if (done) return; done = true; location.href = 'tel:' + (window.__cgNum || '+18336314698'); }};
    document.addEventListener('callgrid:numberAssigned', function () {{ setTimeout(go, 50); }});
    setTimeout(go, 1500);
  }});
</script>
<script>
!(function (e, n, t, i, p, a, s) {{
  e[i] ||
    (((p = e[i] =
      function () {{
        p.process ? p.process.apply(p, arguments) : p.queue.push(arguments);
      }}).queue = []),
    (p.t = +new Date()),
    ((a = n.createElement(t)).async = 1),
    (a.src = 'https://static.newsbreak.com/business/tracking/nbpixel.js?t=' + 864e5 * Math.ceil(new Date() / 864e5)),
    (s = n.getElementsByTagName(t)[0]).parentNode.insertBefore(a, s));
}})(window, document, 'script', 'nbpix'),
  nbpix('init', 'ID-2107135447630544897'),
  nbpix('event', 'pageload');
</script>
</head>
<body>
  <div class="label">Advertisement</div>
  <div class="top"><img src="/images/NBIP.png" alt="National Burial Insurance Policies"></div>
"""

FOOT = """
  <div class="foot">
    <p>Advertisement. National Burial Insurance Policies connects you with licensed agents and is not an insurance company. Not affiliated with any government agency.</p>
    <p><a href="/privacy-policy.html">Privacy Policy</a> &middot; <a href="/terms-conditions.html">Terms &amp; Conditions</a></p>
  </div>

  <a href="{tel}" class="bar">&#128222; Tap to Call and See Your Rate</a>

  <script>
  (function () {{
    var q = new URLSearchParams(location.search);
    var c = (q.get('utm_campaign') || '') + '_' + (q.get('utm_content') || '');
    function send(e) {{
      var u = 'https://seniorhomewarranties.com/api/t?e=' + e + '&p={page}&c=' + encodeURIComponent(c);
      try {{ if (!navigator.sendBeacon(u)) throw 0; }} catch (x) {{ fetch(u, {{ mode: 'no-cors', keepalive: true }}); }}
    }}
    send('view');
    var marks = [25, 50, 75, 90], hit = {{}};
    addEventListener('scroll', function () {{
      var p = (scrollY + innerHeight) / document.documentElement.scrollHeight * 100;
      marks.forEach(function (m) {{ if (p >= m && !hit[m]) {{ hit[m] = 1; send('scroll' + m); }} }});
    }}, {{ passive: true }});
    document.addEventListener('click', function (ev) {{
      var a = ev.target.closest && ev.target.closest('a[href^="tel:"]'); if (!a) return;
      var label = a.classList.contains('bar') ? 'bar' : 'btn' + [].indexOf.call(document.querySelectorAll('a.cta'), a);
      if (!window.__tapped) {{ window.__tapped = {{}}; send('tap'); if (window.nbpix) nbpix('event', 'contact'); }}
      if (!window.__tapped[label]) {{ window.__tapped[label] = 1; send('tap_' + label); }}
    }}, true);
  }})();
  </script>
</body>
</html>
"""

CTA = f'<a href="{TEL}" class="cta">Tap to Call and See Your Rate<small>A licensed agent answers. Free, no obligation.</small></a>'

TODAY = """
  <section class="hero">
    <div class="who">Ages 50–85 &middot; U.S. Residents</div>
    <h1>Still Got It? Then Your Rate Will Never Be Lower Than Today.</h1>
    <p class="dek">Burial insurance is priced on your age and health right now. Once you're approved, most plans lock that rate for life. Every birthday you wait, it goes up.</p>
    <ul class="checks">
      <li>No medical exam, just a few questions</li>
      <li>As little as $0.89 a day</li>
      <li>Rate locked for life on most plans</li>
      <li>Cash paid straight to your family</li>
    </ul>
    """ + CTA + """
    <p class="note">Mon–Fri, 9am–6pm ET &middot; Takes a few minutes</p>
  </section>

  <section class="body">
    <h2>Why waiting costs you money</h2>
    <p>Most people only think about this after something goes wrong. That's the most expensive moment to start. Apply while you're healthy and more plans are open to you, at the rate for the age you are today. Wait for a diagnosis and the same coverage costs more, or the best plans aren't available at all.</p>

    <div class="big"><strong>Social Security pays a one-time death benefit of just $255.</strong> A funeral costs $8,000 to $10,000. Somebody pays the difference. The only question is whether it's you, ahead of time, or your family, the week after.</div>

    <h2>What happens when you call</h2>
    <ol class="steps">
      <li>A licensed agent answers. Not a recording.</li>
      <li>They ask your age, state, tobacco use and a few health questions. About two minutes.</li>
      <li>They tell you which plans you qualify for and what each costs per month.</li>
      <li>You decide. Nothing is bought unless you say yes.</li>
    </ol>
    """ + CTA + """

    <h2>Who this is for</h2>
    <p>U.S. residents 50 to 85 who are in decent shape today and want this settled while that's still true. Not for you if you're under 50 or already have enough coverage to pay for your funeral.</p>
    """ + CTA + """
  </section>
"""

NOW = """
  <section class="hero">
    <div class="who">Ages 50–85</div>
    <h1>They Took the First Step. Now It's Your Turn.</h1>
    <p class="dek">Over a million seniors bought final expense coverage last year so their families won't get stuck with the funeral bill. See what you qualify for in one quick call.</p>
    <ul class="checks">
      <li>No medical exam</li>
      <li>As little as $0.89 a day</li>
      <li>Coverage up to $25,000</li>
    </ul>
    """ + CTA + """
    <p class="note">Mon–Fri, 9am–6pm ET &middot; No obligation</p>
  </section>
"""

QUIZ = """
  <style>
    .bar { display:none; }
    .bar.show { display:block; }
    .quiz { max-width:640px; margin:0 auto; background:#fff; padding:1.25rem 1.25rem 2rem; text-align:center; }
    .prog { height:8px; background:#e9e5da; border-radius:99px; overflow:hidden; margin:0 0 1.25rem; }
    .prog i { display:block; height:100%; width:0; background:#2fbdaa; transition:width .4s ease; }
    .step { display:none; animation:fadeIn .35s ease; }
    .step.on { display:block; }
    @keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:none; } }
    .q { font-size:1.55rem; font-weight:800; color:#111; line-height:1.2; margin:.25rem 0 1.1rem; }
    .qs { color:#666; font-size:.95rem; margin-bottom:.4rem; font-weight:600; letter-spacing:.04em; text-transform:uppercase; }
    .opt { display:block; width:100%; background:#fff; border:2px solid #2fbdaa; color:#1d3d6b; font:800 1.3rem/1.2 inherit; padding:1.05rem; border-radius:12px; margin:0 0 .75rem; cursor:pointer; }
    .opt:active, .opt.pick { background:#2fbdaa; color:#fff; }
    .checking { padding:1rem 0; }
    .spin { width:64px; height:64px; border:6px solid #e8f7f4; border-top-color:#2fbdaa; border-radius:50%; margin:0 auto 1.25rem; animation:spin 1s linear infinite; }
    @keyframes spin { to { transform:rotate(360deg); } }
    .checks2 { list-style:none; text-align:left; display:inline-block; font-size:1.1rem; line-height:2.1; }
    .checks2 li { opacity:.35; transition:opacity .3s; }
    .checks2 li.done { opacity:1; }
    .checks2 li.done::before { content:"\\2713  "; color:#2fbdaa; font-weight:900; }
    .checks2 li:not(.done)::before { content:"\\25CB  "; color:#bbb; }
    .win { font-size:3rem; line-height:1; margin-bottom:.4rem; }
    .good { display:inline-block; background:#e8f7f4; color:#1d6b5f; font-weight:800; padding:.4rem .9rem; border-radius:99px; margin-bottom:.75rem; }
    .rh { font-size:1.7rem; font-weight:800; color:#111; line-height:1.2; margin-bottom:.6rem; }
    .rp { font-size:1.15rem; color:#333; line-height:1.5; margin-bottom:.5rem; }
    .hold { color:#b42318; font-weight:700; font-size:1rem; margin:.6rem 0 0; }
    .pulse { animation:pulse 1.6s ease-in-out infinite; }
    @keyframes pulse { 0%,100% { transform:scale(1); } 50% { transform:scale(1.03); } }
    .trust { color:#666; font-size:.9rem; margin-top:1rem; }
  </style>

  <section class="quiz">
    <div class="prog"><i id="bar"></i></div>

    <div class="step on" data-s="1">
      <div class="qs">Step 1 of 2 &middot; Takes 30 seconds</div>
      <div class="q">See if you qualify for final expense coverage with no medical exam. How old are you?</div>
      <button class="opt" data-k="age" data-v="50-59">50 &ndash; 59</button>
      <button class="opt" data-k="age" data-v="60-69">60 &ndash; 69</button>
      <button class="opt" data-k="age" data-v="70-79">70 &ndash; 79</button>
      <button class="opt" data-k="age" data-v="80-85">80 &ndash; 85</button>
    </div>

    <div class="step" data-s="2">
      <div class="qs">Step 2 of 2</div>
      <div class="q">Are you male or female?</div>
      <button class="opt" data-k="gender" data-v="male">Male</button>
      <button class="opt" data-k="gender" data-v="female">Female</button>
    </div>

    <div class="step checking" data-s="3">
      <div class="spin"></div>
      <div class="q">Checking your eligibility&hellip;</div>
      <ul class="checks2">
        <li>Confirming age eligibility</li>
        <li>Finding plans available in <span class="st">your state</span></li>
        <li>Checking no-exam options</li>
        <li>Locating a licensed agent</li>
      </ul>
    </div>

    <div class="step" data-s="4">
      <div class="win">&#127881;</div>
      <div class="good">Good news!</div>
      <div class="rh">You may qualify for coverage starting at $0.89 a day.</div>
      <p class="rp">No medical exam. Rates locked for life on most plans. A licensed agent is standing by to show you your exact rate.</p>
      """ + CTA.replace('class="cta"', 'class="cta pulse"') + """
      <p class="hold">Your spot is reserved for the next 10 minutes.</p>
      <p class="trust">A licensed agent answers right away. Free, no obligation.</p>
    </div>
  </section>

  <script>
  (function () {
    var s = 1, bar = document.getElementById('bar');
    function track(e) {
      var q = new URLSearchParams(location.search), c = (q.get('utm_campaign') || '') + '_' + (q.get('utm_content') || '');
      var u = 'https://seniorhomewarranties.com/api/t?e=' + e + '&p=fe-quiz&c=' + encodeURIComponent(c);
      try { if (!navigator.sendBeacon(u)) throw 0; } catch (x) { fetch(u, { mode: 'no-cors', keepalive: true }); }
    }
    function show(n) {
      s = n;
      document.querySelectorAll('.step').forEach(function (el) { el.classList.toggle('on', +el.dataset.s === n); });
      bar.style.width = ({1: 15, 2: 50, 3: 80, 4: 100})[n] + '%';
      scrollTo(0, 0);
    }
    try {
      fetch('https://ipapi.co/json/').then(function (r) { return r.json(); }).then(function (g) {
        if (g && g.region) document.querySelectorAll('.st').forEach(function (el) { el.textContent = g.region; });
      }).catch(function () {});
    } catch (x) {}
    document.querySelectorAll('.opt').forEach(function (b) {
      b.addEventListener('click', function () {
        b.classList.add('pick');
        track('q_' + b.dataset.k);
        setTimeout(function () {
          if (s === 1) return show(2);
          show(3);
          var items = document.querySelectorAll('.checks2 li');
          items.forEach(function (li, i) { setTimeout(function () { li.classList.add('done'); }, 700 * (i + 1)); });
          setTimeout(function () { show(4); track('result'); document.querySelector('.bar').classList.add('show'); }, 700 * items.length + 600);
        }, 250);
      });
    });
  })();
  </script>
"""

for slug, page, title, body in [
    ("today", "fe-today", "Still Got It at 50+? Your Rate Will Never Be Lower Than Today", TODAY),
    ("now", "fe-now", "Final Expense Coverage for Ages 50–85 | See Your Rate", NOW),
    ("quiz", "fe-quiz", "See If You Qualify | Final Expense Coverage for Ages 50–85", QUIZ),
]:
    os.makedirs(f"final-expense/{slug}", exist_ok=True)
    html = HEAD.format(title=title, page=page) + body + FOOT.format(tel=TEL, page=page)
    io.open(f"final-expense/{slug}/index.html", "w", encoding="utf-8", newline="\n").write(html)
    print("built", slug)
