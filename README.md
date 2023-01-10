# Posthog Deploy

## Setup
- Clone the repo
- Create `.env` file (copied from `sample.env`) and configure all the variables.
- Hit `docker-compose up -d`
- `DOMAIN` must be configured on HTTPS. You can use the below http NGINX config for the same:
```
server {
    server_name {{DOMAIN-HERE}};

    location / {
        proxy_pass http://localhost:{{PORT-HERE}};
    }
    listen 80;
}
```

It'll take a few minutes & service should be available at https://`DOMAIN`.COM