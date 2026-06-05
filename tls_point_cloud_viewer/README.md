# TLS Point Cloud Viewer

This folder contains the browser-ready PACE TLS point cloud viewer and the compact local data assets it needs.

## Run

Do not double-click the HTML file; browser security rules block local binary asset loading from `file://` URLs.

Recommended:

- macOS: double-click `start_viewer.command`, or run `python3 start_viewer.py`
- Windows: double-click `start_viewer.bat`, or run `python start_viewer.py`

Manual option:

From this folder, start a local web server:

```bash
python3 -m http.server 8791
```

Then open:

```text
http://localhost:8791/tls_point_cloud_viewer.html
```

## Included

- `tls_point_cloud_viewer.html`
- `start_viewer.py`, `start_viewer.command`, and `start_viewer.bat`
- local Three.js files in `vendor/three/`
- compact point-cloud LOD files and TREE labels in `data/tls/PACE/viewer/`

The original LAS file is not required for viewing and is not included.
