import argparse
import os
import webbrowser
from weblite.builder import build

def view_site():
    import http.server
    import socketserver

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "output")
    port = 8000

    # Determine default page (index.html or home.html)
    entry_file = "index.html" if os.path.exists(os.path.join(output_dir, "index.html")) \
                 else "home.html" if os.path.exists(os.path.join(output_dir, "home.html")) \
                 else None

    if entry_file is None:
        print("❌ No index.html or home.html found in output/. Please run `weblite build <file>` first.")
        return

    url = f"http://localhost:{port}/{entry_file}"

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=output_dir, **kwargs)

    try:
        with socketserver.TCPServer(("localhost", port), CustomHandler) as httpd:
            print(f"🌐 Serving site at {url} (press Ctrl+C to stop)")
            webbrowser.open(url)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
    except OSError as e:
        print(f"❌ Could not start server: {e}")


def main():
    parser = argparse.ArgumentParser(description="WebLite - Build static websites from YAML.")
    parser.add_argument("command", help="The command to execute", choices=["build", "view"])
    parser.add_argument("input", nargs="?", help="The .wl file to build from (required for build)")

    args = parser.parse_args()

    if args.command == "build":
        if not args.input:
            print("❌ Please provide a .wl input file.")
            return
        build(args.input)
        print(f"✅ Site built successfully from {args.input}. Check the output/ folder!")

    elif args.command == "view":
        view_site()

if __name__ == "__main__":
    main()
