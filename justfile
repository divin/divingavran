# divingavran.com – task runner (https://github.com/casey/just)
# Usage: just <recipe>   (or just --list to see all recipes)

default:
    @just --list

# Start the dev server with live reload, reachable from devices on the LAN
serve:
    zola serve --interface 0.0.0.0

# Build the production site into public/
build:
    zola build

# Build and run a quick sanity check on the output
check: build
    @echo "Checking output..."
    @test -f public/index.html || (echo "FAIL: index.html missing" && exit 1)
    @test -f public/about/index.html || (echo "FAIL: about missing" && exit 1)
    @test -f public/games/index.html || (echo "FAIL: games missing" && exit 1)
    @test -f public/apps/index.html || (echo "FAIL: apps missing" && exit 1)
    @test -f public/music/index.html || (echo "FAIL: music missing" && exit 1)
    @test -f public/journey/index.html || (echo "FAIL: journey missing" && exit 1)
    @test -f public/404.html || (echo "FAIL: 404 page missing" && exit 1)
    @test -f public/robots.txt || (echo "FAIL: robots.txt missing" && exit 1)
    @test -f public/sitemap.xml || (echo "FAIL: sitemap.xml missing" && exit 1)
    @echo "All required pages present ✓"

# Serve the built site (after `just build`); reachable from devices on the LAN
preview:
    zola serve --interface 0.0.0.0

# Remove build artifacts
clean:
    rm -rf public

# Rebuild from scratch
rebuild: clean build
