#!/usr/bin/env python3
"""
Mermaid Diagram Preview Script

Renders Mermaid diagrams to SVG/PNG and opens preview in browser.

Usage:
    python preview.py <diagram.mmd>
    python preview.py <diagram.mmd> --format png
    python preview.py <diagram.mmd> --output output.svg

Requirements:
    - Node.js (for mermaid-cli)
    - npm install -g @mermaid-js/mermaid-cli
    
    Or use the online renderer (default fallback).
"""

import argparse
import base64
import os
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path


def check_mmdc_installed() -> bool:
    """Check if mermaid-cli (mmdc) is installed."""
    try:
        result = subprocess.run(
            ["mmdc", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def render_with_mmdc(input_file: Path, output_file: Path, format: str = "svg") -> bool:
    """Render diagram using mermaid-cli."""
    try:
        result = subprocess.run(
            ["mmdc", "-i", str(input_file), "-o", str(output_file), "-f", format],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"mmdc error: {result.stderr}", file=sys.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error running mmdc: {e}", file=sys.stderr)
        return False


def create_html_preview(mermaid_code: str, output_path: Path) -> None:
    """Create an HTML file with embedded Mermaid renderer."""
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mermaid Preview</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }}
        h1 {{
            color: #333;
            margin-bottom: 20px;
        }}
        .container {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 20px;
            max-width: 100%;
            overflow-x: auto;
        }}
        .mermaid {{
            display: flex;
            justify-content: center;
        }}
        .controls {{
            margin-top: 20px;
            display: flex;
            gap: 10px;
        }}
        button {{
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }}
        .btn-primary {{
            background: #4CAF50;
            color: white;
        }}
        .btn-secondary {{
            background: #2196F3;
            color: white;
        }}
        pre {{
            background: #263238;
            color: #aed581;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            max-width: 800px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <h1>Mermaid Diagram Preview</h1>
    
    <div class="container">
        <div class="mermaid">
{mermaid_code}
        </div>
    </div>
    
    <div class="controls">
        <button class="btn-primary" onclick="downloadSVG()">Download SVG</button>
        <button class="btn-secondary" onclick="toggleCode()">Show/Hide Code</button>
    </div>
    
    <pre id="code" style="display: none;">{mermaid_code}</pre>
    
    <script>
        mermaid.initialize({{ 
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose'
        }});
        
        function downloadSVG() {{
            const svg = document.querySelector('.mermaid svg');
            if (svg) {{
                const svgData = new XMLSerializer().serializeToString(svg);
                const blob = new Blob([svgData], {{type: 'image/svg+xml'}});
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'diagram.svg';
                a.click();
                URL.revokeObjectURL(url);
            }}
        }}
        
        function toggleCode() {{
            const code = document.getElementById('code');
            code.style.display = code.style.display === 'none' ? 'block' : 'none';
        }}
    </script>
</body>
</html>
"""
    output_path.write_text(html_template)


def main():
    parser = argparse.ArgumentParser(
        description="Render and preview Mermaid diagrams",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input Mermaid file (.mmd or .md)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["svg", "png", "pdf"],
        default="svg",
        help="Output format (default: svg)"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file path"
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Don't open in browser"
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Create HTML preview instead of using mmdc"
    )
    
    args = parser.parse_args()
    
    if not args.input.exists():
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Read input file
    mermaid_code = args.input.read_text()
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_path = args.input.with_suffix(f".{args.format}" if not args.html else ".html")
    
    # Use HTML preview if requested or if mmdc is not installed
    if args.html or not check_mmdc_installed():
        if not args.html and not check_mmdc_installed():
            print("mermaid-cli (mmdc) not found. Using HTML preview.")
            print("Install with: npm install -g @mermaid-js/mermaid-cli")
        
        html_output = output_path.with_suffix(".html")
        create_html_preview(mermaid_code, html_output)
        print(f"Created: {html_output}")
        
        if not args.no_open:
            webbrowser.open(f"file://{html_output.absolute()}")
    else:
        # Use mmdc for rendering
        if render_with_mmdc(args.input, output_path, args.format):
            print(f"Created: {output_path}")
            
            if not args.no_open and args.format == "svg":
                # Create HTML wrapper for SVG
                svg_content = output_path.read_text()
                html_wrapper = output_path.with_suffix(".html")
                html_wrapper.write_text(f"""<!DOCTYPE html>
<html>
<head><title>Mermaid Preview</title></head>
<body style="display:flex;justify-content:center;padding:20px;">
{svg_content}
</body>
</html>""")
                webbrowser.open(f"file://{html_wrapper.absolute()}")
        else:
            print("Failed to render with mmdc. Falling back to HTML preview.")
            html_output = output_path.with_suffix(".html")
            create_html_preview(mermaid_code, html_output)
            if not args.no_open:
                webbrowser.open(f"file://{html_output.absolute()}")


if __name__ == "__main__":
    main()
