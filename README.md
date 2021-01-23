# houston_covid19_vaccine_monitor

As someone with elderly parents, I would like to know when https://houstonemergency.org/covid-19-vaccines/ is updated so that I can tell my parents to go sign up for a vaccine.

# Notes

- build vs. buy: Googling website monitoring pages results in only services that only monitor at intervals on the order of tens of minutes or hours. **Build** because it's easy, simple and I want monitoring on the order of 1 minute.
- We can interpolate epoch date to save versions of the page. eg. `echo "haha" >> `date +%s`.txt`
- The page is ~14k according to `curl -so /dev/null https://houstonemergency.org/covid-19-vaccines/ -w '%{size_download}'`

# BVP

- Run on VM or in container. This should cost just a few dollars/month since it's such a lightweight process.
- Don't use persistent datastore b/c #bvp
- Save html contents of https://houstonemergency.org/covid-19-vaccines/ to memory.
- Wait 60s
- wget https://houstonemergency.org/covid-19-vaccines/ again and compare to previous version
- Save latest version to memory and repeat

# MVP

- Wild guess is that this is cheaper than BVP b/c we're using a lambda function, but having a persistent datastore could add cost.
- Save https://houstonemergency.org/covid-19-vaccines/ as `date +%s_index.html` and as `previous_index.html`
- Each time we scrape the page, we diff the latest results with `previous_index.html` and then overwrite `previous_index.html` with the latest
- If there's a diff, send notification to as defined by config file or environment variable. Email is easy.
- Set this up as a cron running during normal waking hours 05:00 - 01:00 (b/c we're talking about a covid vaccine)

# MVP+

- Detect if an anchor tag has been added and send the URL in the notification
