# Funnel Setup — connecting Instagram · Kit · Gumroad · n8n affiliate

Goal: a working money funnel using only the accounts you have. No Carrd needed —
a **Kit landing page** is the bio hub + email capture in one.

```
Instagram (content)
   └─ bio link ─► Kit landing page (opt-in: "Free Missed-Call Text-Back")
                     └─ email captured in Kit  ──► Kit nurture sequence (5 emails)
                            ├─ delivers free workflow (hosted as a $0 Gumroad product)
                            ├─ sells the $49 Pack (Gumroad)        [stream 2]
                            ├─ drops n8n affiliate link            [stream 1]
                            └─ offers done-for-you build $300–1,500 [stream 3]

Gumroad (free + $49 products) ──(native Kit integration)──► tags buyers back into Kit
```

Two capture points (the Kit landing page **and** Gumroad checkout) both feed Kit,
so no lead is lost.

---

## A. Gumroad — create the two products (15 min)

### 1. Free lead magnet (the list-builder)
- New product → **"Missed-Call Text-Back Automation (Free)"** → price **$0** (or
  "pay what you want", min $0).
- Upload file: `content/product/templates/01-missed-call-textback.json` +
  a 1-page setup PDF (export `content/product/free-magnet/README.md`).
- Description: paste **Block 1** below.
- Turn ON "Send customers a receipt" so they get the file link by email.

### 2. The paid pack (the product)
- New product → **"The Local Business Automation Pack"** → price **$49**,
  set a discount code `LAUNCH` for the **$29 intro**.
- Upload: a zip of `content/product/` (templates + `SETUP.md` + `README.md`).
- Description: paste **Block 2** below.
- Thank-you / receipt note: add the bio-hub link + the **done-for-you** upsell
  ("Want it installed for you? Reply for a $300–1,500 build").

---

## B. Kit — capture + nurture (30 min)

### 1. Landing page (this becomes your Instagram bio link)
- Kit → **Grow → Landing Pages & Forms → Create → Landing Page**.
- Headline: *"Steal the automation that texts back every missed call — free."*
- Sub: *"Plug-and-play workflow. Stop losing jobs to whoever the customer calls
  next."* Button: **"Send me the free automation."**
- Publish → copy the URL → this is `BIO_HUB` (goes in your IG bio).

### 2. Tag + incentive
- Create tags: `free-magnet` and `customer`.
- On the form, set the **Incentive email** to deliver the free Gumroad link
  (paste **Block 3**), and auto-apply tag `free-magnet`.

### 3. Nurture sequence
- Kit → **Automate → Sequences → New** → name it "Magnet Nurture".
- Add the 5 emails from **Block 4** (set days: 0 is the incentive, then 1/3/6/9).
- Kit → **Automate → Visual Automations → New**:
  trigger = *joins form* → action = subscribe to "Magnet Nurture".
- Second automation: trigger = *tag `customer` added* → a 2-email customer
  sequence that pitches the done-for-you build.

---

## C. Connect Gumroad → Kit (the key wiring, 5 min)

So everyone who buys/downloads on Gumroad also lands in Kit.

1. Kit → **Settings → Advanced → API** → copy your **API Key**.
2. Gumroad → open each product → **Settings / Integrations** tab → find
   **Kit** (may still read **"ConvertKit"**) → paste API key → choose:
   - free product → subscribe to form, tag `free-magnet`
   - $49 product → subscribe + tag `customer`.
3. Save. (If the native option ever disappears, the fallback is a free Zapier
   zap: *Gumroad new sale → Kit add subscriber + tag*.)

---

## D. n8n affiliate (once approved)

Your affiliate link earns 30% recurring for 12 months when someone signs up for
**n8n Cloud** (the paid, no-server option). Honest placement — three spots:
1. Inside the free workflow's setup page: *"Don't want to self-host? Run it on
   n8n Cloud in 2 minutes → [your link]."*
2. Kit nurture **Email 3** (already slotted in Block 4).
3. A pinned Instagram post / Stories highlight "Tools I use".

Paste the real link into `content/links.md` → `AFF_N8N` when it arrives.

---

## E. Instagram (5 min)
- Bio: one line of value + **the Kit landing-page URL** as the link.
  e.g. *"Automations that run service businesses in the background. Free
  missed-call automation 👇"*
- Add a Stories Highlight: "Free Automation" pointing to the same link.
- Every Reel caption CTA = *"Free template — link in bio."* (matches the scripts).

---

# Paste-ready copy

## Block 1 — Gumroad FREE product description
> **The missed-call text-back every local business needs — free.**
> When you're on a job and miss a call, that caller dials your competitor. This
> automation texts them back in seconds ("Sorry we missed you — how can we
> help?") so the lead stays yours.
> ✅ Importable workflow (n8n) ✅ 1-page setup ✅ You only pay your own texting (pennies)
> Grab it free, plug in your number, stop losing jobs. Want all 5 automations?
> See **The Local Business Automation Pack**.

## Block 2 — Gumroad $49 PACK description
> **The Local Business Automation Pack — 5 systems that stop the leaks.**
> Missed calls, slow lead follow-up, no-shows, missing reviews — every one is
> lost money. This pack hands you 5 plug-and-play automations that fix them:
> 1. Missed-Call Text-Back 2. Speed-to-Lead Router 3. Auto Review Requests
> 4. Appointment Reminders 5. Lead-Nurture Sequence
> Import, plug in your keys, done. Build recipes + step-by-step setup included.
> Built in **n8n (free to self-host)** — the client pays only their own SMS.
> **$49** (intro **$29** with code `LAUNCH`). Rather have it installed? A
> done-for-you build is one email away.

## Block 3 — Kit incentive email (instant)
> **Subject:** Your free missed-call automation 👇
> Here it is — the automation that texts back every missed call:
> **→ [Free Gumroad link]**
> Import it, plug in your number, and you'll stop losing jobs to whoever the
> customer calls next. I'll send a couple more in the next few days that plug the
> other leaks (slow follow-up, no-shows, missing reviews). — The Ops Engine

## Block 4 — Kit nurture sequence (5 emails)

**Email 1 · Day 1 — the real cost**
> **Subject:** the $X most local businesses lose every month
> Most service businesses miss 30%+ of calls when they're on a job. Each missed
> call is a customer who just dialed the next company. Reply in 5 minutes and
> you're ~21x more likely to win the job — that's the whole game. The automation
> I sent makes that reply instant, 24/7. Set it up yet? Hit reply if you got
> stuck — I read every one.

**Email 2 · Day 3 — the bigger system**
> **Subject:** the missed-call fix is 1 of 5 leaks
> Missed calls are the obvious leak. The quiet ones: leads that sit unanswered,
> no-shows, and customers you never asked for a review. I packaged all 5 fixes
> into one plug-and-play set — **The Local Business Automation Pack**. Import,
> plug in keys, done. Intro price $29 with code `LAUNCH` → [pack link].

**Email 3 · Day 6 — the tool that runs it (affiliate)**
> **Subject:** how to run these without a server
> People ask what runs these automations. It's **n8n** — free if you self-host,
> or 2-minute setup on **n8n Cloud** if you'd rather skip the server:
> [your n8n affiliate link]. Either way the automations are the same; Cloud just
> saves you the setup. (The Pack includes the importable workflow + recipes.)

**Email 4 · Day 9 — proof + last call**
> **Subject:** 2 saved jobs pays for the whole thing
> The math is stupid simple: the Pack is $29 right now, and recovering *two*
> missed jobs a month covers it many times over — every month after is profit.
> Code `LAUNCH` expires soon → [pack link]. Prefer it installed for you? Reply
> "install" and I'll send options (done-for-you builds run $300–$1,500).

**Email 5 · Day 12 — the service offer**
> **Subject:** want me to just build it for you?
> If you'd rather not touch any of this: I install the whole system for you —
> missed-call text-back, speed-to-lead, reminders, reviews — flat fee, done in
> about a day. Reply "audit" and I'll show you the 3 spots your business is
> leaking leads first, free. — The Ops Engine

---

## Test checklist (do once, end-to-end)
- [ ] Open the Kit landing page → submit a test email → incentive email arrives with the free link.
- [ ] Free Gumroad link downloads the workflow JSON.
- [ ] Buy the $49 pack with code `LAUNCH` (use a test) → tag `customer` appears in Kit → customer sequence fires.
- [ ] Affiliate link resolves to your n8n dashboard credit.
- [ ] IG bio link opens the Kit landing page on mobile.
