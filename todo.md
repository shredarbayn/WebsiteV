# TODO List for WebsiteV

- [x] Obtain IMDb poster URLs for selected works
- [x] Embed IMDb posters in `index.html`
- [x] Update CSS for poster layout and responsiveness
- [ ] Add new project entries as needed
- [ ] Optimize images for faster load times
- [ ] Write documentation for future content updates
- [ ] Conduct cross-browser testing
- [ ] Deploy updates to production

## Technical Learnings
- **IMDb Scraping**: Directly scraping IMDb for poster URLs is unreliable due to aggressive bot protection (returning 403 Forbidden). 
- **Poster Hotlinking**: Using direct Amazon S3 URLs (`https://m.media-amazon.com/images/M/...`) is the most stable way to embed IMDb posters without local hosting.
- **CSS Layout**: Using `display: grid` with `aspect-ratio: 2/3` and `object-fit: cover` provides a robust container for variable-sized film posters.
- **Verification**: When browser tools are restricted from accessing `file://` URLs, serving the site via `python -m http.server` allows for a consistent testing environment.
