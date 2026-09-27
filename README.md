# Physics-Grounded 4D World Model Resources

Published geometry and selected simulation assets for the
[Physics-Grounded 4D World Model Framework](https://github.com/acse-yl222/physics-grounded-4d-world-model-framework).

[Browse resources](https://acse-yl222.github.io/urban-world-model-models/) ·
[Explore scenes](https://acse-yl222.github.io/physics-grounded-4d-world-model-framework/)

## Layout

```text
resources.json                         # all published resources, provenance and hashes
project/
  south_ken/geometry/models_v1/         # chunked South Kensington GLB
  white_city/geometry/white_city_v2/    # chunked White City GLB
  windfarm/geometry/published_v1/       # published terrain/turbine GLB
  windfarm/runs/published_movie_v1/     # published wind playback and comparison fields
  <scene>/resources.json               # scene resource IDs
core008/manifest.json                  # compatibility manifest
white_city/manifest.json               # compatibility manifest
tools/check_resources.py
```

Resources are grouped by **scene / category / version**. Reusable simulation and viewer
code belongs to the framework repository; this repository holds publishable assets.
`resources.json` is a resource catalogue, **not** the framework's simulation run manifest.
The wind movie retains its original export format and sampling metadata.

Each resource has an ID, scene, category, version, format, assets (relative path, bytes,
SHA-256), provenance, and licensing notes. Treat published versions as immutable: publish
changed data under a new version. Supported categories include geometry, input, runs and
previews. Do not upload local caches, checkpoints, private data, or credentials automatically.

## Compatibility and hosting

The repository address is retained for compatibility. The original model-manifest URLs
`core008/manifest.json` and `white_city/manifest.json` remain available. Their part lists
now point to canonical resource paths; clients must resolve each `file` relative to its
manifest URL. Historical direct `.part-*` URLs have moved. Follow the manifest instead
of constructing part URLs yourself.

GitHub Pages serves the assets cross-origin for the framework viewer. Large GLBs are
split into ordered chunks; the manifest records each chunk's bytes and SHA-256.
Concatenate canonical chunks in manifest order to reconstruct the model. Do not treat
individual chunks as standalone GLBs.

City physics fields, replay data and auxiliary assets already published on the framework's
`pages` branch remain there for compatibility. This catalogue does not claim that all
framework assets have been migrated here. Windfarm assets were copied from an existing
public deployment; no private local simulation output was uploaded.

## Verification and attribution

```sh
python3 tools/check_resources.py
```

Validation checks every registered file, chunk order/length, GLB header and compatibility
manifest. It does not establish scientific accuracy or grant a new blanket licence.
Keep source-specific attribution and original assumptions when reusing data.
