# Setup & Build Recipes

All five workflows ship as **importable n8n JSON** (`01`–`05`) — free self-host or
cloud. Import a workflow, fill its **Config** node, add the Twilio HTTP Basic Auth
credential (Account SID : Auth Token), point your trigger at the webhook, activate.
The client pays their own Twilio usage (~$0.0079/SMS). The recipes below explain each
flow (handy for customizing, or rebuilding in Make).

## 0. Prereqs
- n8n (self-hosted Docker = $0, or n8n Cloud).
- Twilio account + number (client's) for SMS recipes.
- A Google account (Sheets for logging; Calendar for bookings).

## 1. Missed-Call Text-Back  ✅ included JSON (client-deploy ready)
Webhook → **Config** (edit once: SID, From number, message) → **Only Missed Calls**
(filters DialCallStatus/CallStatus = no-answer/busy/failed so answered calls are
skipped) → HTTP Request (Twilio Send Message). Import the JSON, fill the Config node,
add the HTTP Basic Auth credential (SID:AuthToken), point Twilio's call action/status
callback at the webhook, activate. Full steps are in the sticky note inside the JSON.

## 2. Speed-to-Lead Router  ✅ `02-speed-to-lead.json`
Webhook (website form: `name`/`phone`/`email`/`service`) → Config → Extract →
Text the Lead (Twilio: "Hi {{name}}, grab a time: {{bookingLink}}") → Alert the Owner
(Twilio SMS to owner's mobile). First touch in < 60s. Optional add-on: a Google Sheets
→ Append node after *Extract Lead* to log every lead.

## 3. Auto Review Requests  ✅ `03-review-requests.json`
Webhook (job done: `name`/`phone`) → Config → Extract → **Wait 2h** → Twilio SMS with
your Google review short-link. Optional: a Google Sheets node to mark "review_requested".

## 4. Appointment Reminders  ✅ `04-appointment-reminders.json`
Webhook (booking: `name`/`phone`/`appointmentTime` ISO) → Config → Extract (computes
`remindAt = appointmentTime − 24h`) → **Wait Until** that time → Twilio SMS reminder
with "reply R to reschedule". Cuts no-shows. Needs n8n always-on (Cloud or self-host).

## 5. Lead-Nurture Sequence  ✅ `05-lead-nurture.json`
Webhook (new lead: `name`/`phone`) → Config → 5 Twilio touches with Wait nodes between:
Day 0 welcome → Day 1 proof → Day 3 offer → Day 6 case study → Day 10 last call.
Upgrades (notes inside): swap any touch for an Email node; add an IF after each Wait to
stop once the lead books.

---
**Selling note:** if the buyer would rather have it installed, that's the
$300–$1,500 done-for-you service. This pack is the top of that funnel.
