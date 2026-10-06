# Make it yours (10 minutes)

1. **Create the repo.** On GitHub, create a *public* repo named exactly your username (e.g. `yourname/yourname`) and copy these files in, or click **Use this template**.
2. **Find & replace `USERNAME`** with your GitHub username in `README.md` (stats cards, snake, project links). Also swap `YOUR_EMAIL`, `YOUR_LINKEDIN` and the Instagram handle.
3. **Rewrite the text.** Edit the WHOAMI block, portfolio table, roadmap and tech-stack icons (icon names: <https://skillicons.dev>).
4. **Regenerate the visuals** (optional but recommended, makes the ASCII banner *your* name):
   ```bash
   pip install pyfiglet
   # edit the CONFIG block at the top of tools/build_assets.py
   python tools/build_assets.py
   ```
   Try other `FONT` values: `ansi_shadow`, `slant`, `big`, `doom`, `block`.
5. **Turn on the snake.** Repo → Settings → Actions → General → Workflow permissions → *Read and write*. Then Actions tab → *Generate Snake* → *Run workflow*. It refreshes every 12 hours.
6. **ASCII portrait (optional).**
   ```bash
   pip install pillow
   python tools/img2ascii.py me.jpg --width 60 > portrait.txt
   ```
   Paste it into a code block in the README.

## Notes
- The ticker, divider and chart are decoration. Nothing in them is live data, and the README labels the chart "art, not data".
- Stats cards come from a free public host that is sometimes rate-limited. If one shows an error, refresh later or self-host `github-readme-stats`.
- Colors live in `tools/build_assets.py` (`CYAN`, `VIOLET`, `GREEN`, `AMBER`, `BG`) and as hex codes in the stats URLs.
