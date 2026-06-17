# Setup & Build Recipes

All recipes run in **n8n** (free self-host or cloud). The client pays their own
Twilio / email usage. Import `01-missed-call-textback.json` directly; build the
rest from the node recipes below (kept as recipes to stay tool-agnostic — works
in n8n or Make).

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

## 2. Speed-to-Lead Router
Webhook (website form) → Set (name/phone/email/service) →
(a) HTTP Request → Twilio SMS: "Thanks {{name}}, book a time: {{bookingLink}}";
(b) Send Email node → owner alert;
(c) Google Sheets → append lead row.
Trigger goal: first touch in < 60 seconds.

## 3. Auto Review Requests
Trigger: job marked done (Webhook from CRM, or Schedule reading a "completed"
Google Sheet) → Wait 2h → HTTP Request → Twilio SMS with the Google review
short-link → Google Sheets: mark "review_requested".

## 4. Appointment Reminders
Schedule trigger (hourly) → Google Calendar "get events" (next 25h) →
IF event ~24h away → SMS reminder; IF ~1h away → SMS reminder with
"reply R to reschedule" → log to Sheet. Cuts no-shows.

## 5. Lead-Nurture Sequence
Webhook (new lead, or Sheet trigger) → Wait/branch 5 touches over 10 days:
Day0 text, Day1 email (social proof), Day3 text (offer), Day6 email (case
study), Day10 text (last call). Stop branch if lead replies/books.

---
**Selling note:** if the buyer would rather have it installed, that's the
$300–$1,500 done-for-you service. This pack is the top of that funnel.
