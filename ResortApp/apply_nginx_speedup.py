import subprocess

nginx_config = """# Nginx configuration for Pomma Holidays
limit_req_zone $binary_remote_addr zone=api:10m rate=100r/s;
limit_req_zone $binary_remote_addr zone=general:10m rate=50r/s;

upstream resort_backend {
    server 127.0.0.1:8000;
    keepalive 64;
}

server {
    server_name pommaholidays.com www.pommaholidays.com;

    gzip on;
    gzip_vary on;
    gzip_min_length 256;
    gzip_comp_level 5;
    gzip_proxied any;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/javascript
        application/x-javascript
        application/json
        application/xml
        application/xml+rss
        image/svg+xml
        font/woff2;

    client_max_body_size 50M;
    client_body_timeout 12;
    client_header_timeout 12;
    keepalive_timeout 65;
    keepalive_requests 1000;
    send_timeout 10;
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;

    # Admin Dashboard Static Asset Caching
    location /admin/static/ {
        alias /opt/pomma/dasboard-build/static/;
        expires 1y;
        add_header Cache-Control "public, max-age=31536000, immutable";
        access_log off;
    }

    # Admin Dashboard - /admin
    location /admin/ {
        alias /opt/pomma/dasboard-build/;
        index index.html;
        try_files $uri $uri/ /admin/index.html;
        include /etc/nginx/mime.types;
        add_header Cache-Control "no-cache, must-revalidate";
    }

    # Legacy Admin Dashboard - /pommaadmin
    location /pommaadmin/ {
        alias /opt/pomma/dasboard-build/;
        index index.html;
        try_files $uri $uri/ /pommaadmin/index.html;
        include /etc/nginx/mime.types;
    }

    location = /admin { return 301 /admin/; }
    location = /pommaadmin { return 301 /pommaadmin/; }

    # User App (Userend)
    location / {
        root /opt/pomma/userend-build/;
        index index.html;
        try_files $uri $uri/ /index.html;
        include /etc/nginx/mime.types;
    }

    # User App Assets
    location /pomma/ {
        alias /opt/pomma/userend-build/;
        index index.html;
        try_files $uri $uri/ /index.html;
        include /etc/nginx/mime.types;
    }

    # API routes
    location /api/ {
        limit_req zone=api burst=200 nodelay;
        proxy_pass http://resort_backend/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_buffering off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }

    # Health check endpoint
    location /health {
        proxy_pass http://127.0.0.1:8000/health;
        proxy_set_header Host $host;
        access_log off;
    }

    # Uploads directory with caching & compression
    location /uploads/ {
        alias /opt/pomma/ResortApp/uploads/;
        expires 30d;
        add_header Cache-Control "public, max-age=2592000, immutable";
        access_log off;
    }

    # Static files
    location /backend-static/ {
        alias /opt/pomma/ResortApp/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }

    listen 443 ssl http2;
    ssl_certificate /etc/letsencrypt/live/pommaholidays.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/pommaholidays.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}

server {
    if ($host = www.pommaholidays.com) {
        return 301 https://$host$request_uri;
    }
    if ($host = pommaholidays.com) {
        return 301 https://$host$request_uri;
    }
    listen 80;
    server_name pommaholidays.com www.pommaholidays.com;
    return 404;
}
"""

def update_nginx():
    path = "/etc/nginx/sites-available/pommaholidays"
    with open(path, "w") as f:
        f.write(nginx_config)
    print("Nginx config updated successfully.")

if __name__ == "__main__":
    update_nginx()
