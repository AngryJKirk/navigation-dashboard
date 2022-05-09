# Navigation

This project follows a goal to have simple and lightweight dashboard with different links.
I use it to have my own self-hosted service dashboard.

Most of the dashboards are heavy and have many features many people don't need.

Here is mine:

![](https://storozhenko.dev/images/navigation.gif)

### Pros:

1) static html, 0 lines of JS
2) minimalistic look
3) easy to set up

### Cons:

1) No customization

## Setup

Create navigation.yml following this example:

```yaml
sorted: true
titles:
  - title:
      name: "database tools"
      items:
        - name: "metabase"
          logo: 📊
          url: "https://metabase.example.com"
        - name: "pg"
          logo: "💾"
          url: "https://pg.example.com"
  - title:
      name: "tools"
      items:
        - name: "notes"
          logo: "📓"
          url: "https://md.example.com"
        - name: "torrent"
          logo: "🏴‍☠️"
          url: "https://torrent.example.com"
        - name: "passwords"
          logo: "🔐"
          url: "https://password.example.com"
        - name: "terminal"
          logo: "💻"
          url: "https://hacker.example.com"
  - title:
      name: "misc"
      items:
        - name: "cat or dog"
          logo: "🙀"
          url: "https://play.example.com"
        - name: "memory game"
          logo: "🧠"
          url: "https://example.com/memorygame"
```

Amount of titles could be anything, but 4 is probably the max amount of titles, there might be issues if more.

`sorted: true` is used to sort items in their length order. Set it to `false` if you want to keep order as is.

`logo` can accept any text, but you should use emojis. Emojis are the best icons due to high availability (almost every
browser font supports it).

That's pretty much it. CSS is adapted to mobile view.

Before running make sure you have PyYML installed.

If not, just run `pip3 install pyyaml`.

Then run `python3 main.py > index.html` and put the `index.html` in your favorite web server. If you don't have one, I
recommend [caddy](https://caddyserver.com/). You also may just store the `index.html` locally and open it everytime you need to navigate.

### Docker install with nginx webserver:

1. Edit the yml file with your necessaries 
2. `docker build -t victim/navigation-dashboard .`
3. `docker run --name=navigationdashboard -d -p 8080:80 victim/navigation-dashboard`
4. Go to http://yourip:8080 or http://localhost:8080 to see the results

If you want to change your listed websites you'll need to destroy the container and rebuild with any changes.
