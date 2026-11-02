# Imperial Corridor native-resolution assets

Versioned public assets for the existing framework viewer. This dedicated data branch is served through raw GitHub URLs; it does not replace the resource repository main branch or its Pages site.

All files are catalogued with SHA-256. Run `python3 tools/check_resources.py`. Detailed buildings stay in the existing immutable geometry resource. Source grids are preserved: 4 m wind final / solar / tracer / flood; 8 m saved wind time series; 32 m temperature. Ground is a flat projection. Traffic is a selected recorded SUMO subset, with an independent clock and no invented frames.
