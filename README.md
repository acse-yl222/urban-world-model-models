# urban-world-model · models

Large binary models for https://github.com/acse-yl222/urban-world-model, served by GitHub Pages (which adds
`Access-Control-Allow-Origin: *`, unlike release assets) so the viewer at acse-yl222.github.io/urban-world-model can fetch
them cross-origin. Files above GitHub's 100 MB limit are split into parts; each folder has a `manifest.json` with the part
list and SHA-256 sums. Reassemble with `cat name.glb.part-* > name.glb`.

- `core008/` — the South Kensington core008 city model (254 MB, 3 parts).
- `white_city/` — the White City 9 km² city model (191 MB, 3 parts).
