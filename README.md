# cloudflare-dyndns

Simple script to automatically update Cloudflare DNS entry for a home server

## How to use:

1. Install dependencies from `requirements.txt`

2. Create the A record on Cloudflare that you want to keep updated.

3. Find your `zone_id` by going to the cloudflare website, clicking on your
   domain, and scrolling down to the the API section. You'll also need your
   [global API key](https://support.cloudflare.com/hc/en-us/articles/200167836-Where-do-I-find-my-Cloudflare-API-key-).

4. Copy the `template.config.py` to `config.py` and modify the fields.

5. Setup cron to run the script at the desired frequency.

