# Missed-Call Text-Back — Free Setup Guide

The automation that texts back every missed call in seconds, so the caller stays
your customer instead of dialing the next business. ~10 minutes to set up.

## What you get
- `01-missed-call-textback.json` — importable n8n workflow.
- This guide.

## What it does
Missed call → your phone system fires a webhook → the workflow instantly texts
the caller: *"Sorry we missed you — how can we help?"* The lead stays with you.

## Setup (10 min)
1. **Get n8n.** Free if you self-host (Docker), or skip the server with
   **n8n Cloud** (2-minute setup): 👉 **[run it on n8n Cloud](AFF_N8N)**.
2. **Import** `01-missed-call-textback.json` (n8n → Import from File).
3. **Twilio:** add your Twilio Account SID, Auth Token, and SMS-enabled number
   in the HTTP Request node. (You only ever pay your own texting — pennies/text.)
4. **Webhook:** point your phone provider's "missed call / no-answer" callback at
   the workflow's webhook URL. (Twilio: set the number's no-answer webhook.)
5. **Test:** call your number, don't answer → you should get the text back.

## Want the other 4 leaks fixed too?
This is 1 of 5. Speed-to-lead, no-show reminders, auto review requests, and a
5-touch nurture sequence are in **The Local Business Automation Pack** — import,
plug in keys, done. Intro **$29** with code `LAUNCH`: 👉 **[PRODUCT_PACK]**

## Rather have it installed for you?
Reply to the email this came with, or book a free 10-min automation audit:
👉 **[BOOK_AUDIT]** — I'll show you the 3 spots you're leaking leads, no pitch.

— The Ops Engine
