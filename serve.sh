rm -rf build
python build.py
python -m http.server --directory build