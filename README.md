What it does
- Presents a realistic-looking calculator UI using Tkinter (desktop) and a simple web version using Flask.
- In both versions pressing `=` shows the embedded ASCII-art cat (the UI does not evaluate expressions).

How to run (desktop)
- Run `python calculator.py` in this folder.

How to run (web)
- Install Flask: `pip install flask`
- Run `python app.py` from the repository root and open http://127.0.0.1:5000/ in your browser.

How to deploy to GitHub Pages (static)
1. Commit the `docs/` folder to your repository root.
2. In your repository Settings → Pages, set Source to the `main` branch and `docs/` folder (or `gh-pages` branch if you prefer).
3. Wait a minute and open the page at `https://<your-username>.github.io/<repo-name>/`.

If your GitHub Pages site still shows the repository README instead of the site, either:
- Set the Pages source to the `docs/` folder in repo Settings → Pages, or
- Keep the Pages source as the repository root and use the provided `index.html` (at the repo root) to redirect visitors automatically to `/docs/`.

Notes
- All previous files were deleted as you requested.
- The ASCII cat is embedded in the source (no external images).
