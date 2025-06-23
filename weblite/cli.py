import argparse
import os
import webbrowser
import http.server
import socketserver
from threading import Thread
from weblite.builder import build

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("❌ Missing dependency: watchdog. Install with `pip install watchdog`")
    exit(1)


def view_site(port=8000):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "output")

    entry_file = next((f for f in ("index.html", "home.html")
                       if os.path.exists(os.path.join(output_dir, f))), None)
    if not entry_file:
        print("❌ No index.html or home.html found. Please run `weblite build <file>` first.")
        return

    url = f"http://localhost:{port}/{entry_file}"

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=output_dir, **kwargs)

    def serve():
        with socketserver.TCPServer(("localhost", port), CustomHandler) as httpd:
            print(f"🌐 Serving site at {url} (press Ctrl+C to stop)")
            webbrowser.open(url)
            httpd.serve_forever()

    Thread(target=serve, daemon=True).start()


def watch_file(filepath, on_change):
    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.src_path.endswith(filepath):
                print(f"🔄 Change detected in {filepath}. Rebuilding...")
                on_change()

    observer = Observer()
    observer.schedule(Handler(), path=os.path.dirname(filepath) or ".", recursive=False)
    observer.start()
    return observer



def main():
    parser = argparse.ArgumentParser(
        prog="weblite",
        description="WebLite - Instantly build and preview static websites from YAML.",
        epilog="Examples:\n  weblite build site.wl\n  weblite dev site.wl",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "command",
        choices=["build", "dev"],
        help="Choose a command: 'build' to generate HTML, 'dev' to build + watch"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="The .wl file to build from (required for 'build' and 'dev')"
    )

    args = parser.parse_args()

    if args.command == "build":
        if not args.input:
            print("❌ Please provide a .wl input file.")
            return
        build(args.input)
        print(f"✅ Site built from {args.input}. Check output/ folder.")

    elif args.command == "dev":
        if not args.input:
            print("❌ Please provide a .wl input file.")
            return
    
        def rebuild():
            try:
                build(args.input)
                print("✅ Rebuilt site.")
            except Exception as e:
                print(f"❌ Build failed: {e}")

        rebuild()
        view_site()

        print(f"👀 Watching {args.input} for changes... (Press Ctrl+C to stop)")
        observer = watch_file(args.input, rebuild)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
            print("\n🛑 Stopped watching.")
        observer.join()


if __name__ == "__main__":
    main()
