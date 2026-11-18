import os
import shutil



# Remove internal directories only during Cloudflare Pages builds.
if os.environ.get("CF_PAGES") or os.environ.get("CF_PAGES_URL"):
    for folder in ['.private', '.github']:
        folder_path = os.path.join(os.getcwd(), folder)
        try:
            shutil.rmtree(folder_path)
            print(f"Deleted {folder} folder: {folder_path}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Failed to delete {folder} folder: {e}")
# Build-only and internal files must never be published. CF_PAGES / CF_PAGES_URL are set by the
# Cloudflare Pages build, so none of this ever touches a local working tree.
if os.environ.get("CF_PAGES") or os.environ.get("CF_PAGES_URL"):
    # (1) internal image-description sidecars (*-description.txt) are auto-generated working notes
    # sitting in the SERVED image directories, not published content.
    removed_sidecars = 0
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('-description.txt'):
                try:
                    os.remove(os.path.join(root, file))
                    removed_sidecars += 1
                except Exception as e:
                    print(f"Failed to delete description sidecar {file}: {e}")
    print(f"Deleted {removed_sidecars} image-description sidecar file(s)")

    # (2) this script is itself a build input living in the output tree.
    try:
        os.remove(os.path.join(os.getcwd(), "remove_html.py"))
        print("Deleted build-only file: remove_html.py")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Failed to delete build-only file remove_html.py: {e}")

filenames = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.htm'):
            filenames.append(os.path.join(root, file))

print(f"Found {len(filenames)} html files in current directory")
print(*filenames, sep="\n")

for filename in filenames:
    try:
        print("Read file", filename)
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        import re
        basename = os.path.basename(filename)
        # Special case: preserve .html in google-site-verification files
        if basename.startswith("google") and basename.endswith(".html"):
            lines = text.strip().splitlines()
            if len(lines) == 1 and re.match(r"^google-site-verification: google.*\.html$", lines[0]):
                print(f"Special case: preserving .html in {filename}")
                # Do not modify text
                continue

        # --- own-origin guard (R1 2026-10-15, tightened by R1.1 2026-10-16) --
        # The strip exists so THIS site's links are served extensionless
        # (Cloudflare Pages 308s a .html path to its extensionless form).
        # Another origin's routing is not ours to rewrite: an external
        # citation keeps its extension or the reader dead-ends on a 404 or a
        # generic hub. Scheme-less values are always ours; an absolute (or
        # protocol-relative) value is ours only when its host is this site's,
        # resolved from this page's own canonical, then the checkout
        # directory name (on Pages the cwd is the repo root and the repo name
        # IS the domain). R1.1: the file rule is REMOVED -- host only.
        def _norm_host(host):
            host = host.strip().lower()
            return host[4:] if host.startswith("www.") else host

        def _url_host(url):
            m = re.match(r"^(?:[a-z][a-z0-9+.-]*:)?//(?:[^@/]*@)?([^/:?#]+)", url, re.I)
            return _norm_host(m.group(1)) if m else None

        def _canonical_hosts(doc):
            hosts = set()
            for tag in re.findall(r"<link\b[^>]*>", doc, re.I):
                if re.search(r"""rel\s*=\s*["']?[^"'>]*canonical""", tag, re.I):
                    m = re.search(r"""href\s*=\s*["']([^"']+)["']""", tag, re.I)
                    h = _url_host(m.group(1)) if m else None
                    if h:
                        hosts.add(h)
            return hosts

        def _own_hosts(doc):
            hosts = _canonical_hosts(doc)
            d = _norm_host(os.path.basename(os.path.abspath(os.getcwd())))
            if d:
                hosts.add(d)
            return hosts

        _OWN_HOSTS = _own_hosts(text)

        def _is_own_origin(url):
            if not re.match(r"^(?:https?:)?//", url, re.I):
                return True                  # relative / scheme-less: this site
            host = _url_host(url)
            return host is not None and host in _OWN_HOSTS   # R1.1: host only

        def remove_html_from_href(match):
            url = match.group(1)
            if not _is_own_origin(url):
                return match.group(0)        # FOREIGN origin: citation intact
            url = re.sub(r"(\.html|\.htm)$", "", url)
            return f'href="{url}"'

        new_text = re.sub(r'href="([^"]*?\.(?:html|htm))"', remove_html_from_href, text)

        with open(filename, "w", encoding="utf-8") as f:
            print("Write file", filename)
            f.write(new_text)
    except:
        print("failed ", filename)

