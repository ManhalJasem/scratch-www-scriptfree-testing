#!/usr/bin/env bash
set -euo pipefail

VERSION="${VERSION:-113.0.5672.63}"

detect_platform() {
  local os arch
  case "$(uname -s)" in
    Linux*)  os="linux" ;;
    Darwin*) os="mac" ;;
    MINGW*|MSYS*|CYGWIN*) os="win" ;;
    *) echo "Unsupported OS: $(uname -s)" >&2; exit 1 ;;
  esac

  case "$(uname -m)" in
    x86_64|amd64) arch="x64" ;;
    arm64|aarch64) arch="arm64" ;;
    i?86) arch="32" ;;
    *) echo "Unsupported CPU arch: $(uname -m)" >&2; exit 1 ;;
  esac

  case "${os}:${arch}" in
    linux:x64)  CFT_PLATFORM="linux64";   DRIVER_PLATFORM="linux64";   CHROME_BIN_SUBPATH="chrome-linux64/chrome" ;;
    mac:x64)    CFT_PLATFORM="mac-x64";   DRIVER_PLATFORM="mac64";     CHROME_BIN_SUBPATH="chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing" ;;
    mac:arm64)  CFT_PLATFORM="mac-arm64"; DRIVER_PLATFORM="mac_arm64"; CHROME_BIN_SUBPATH="chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing" ;;
    win:x64)    CFT_PLATFORM="win64";     DRIVER_PLATFORM="win32";     CHROME_BIN_SUBPATH="chrome-win64/chrome.exe" ;;
    win:32)     CFT_PLATFORM="win32";     DRIVER_PLATFORM="win32";     CHROME_BIN_SUBPATH="chrome-win32/chrome.exe" ;;
    linux:arm64) echo "No official Chrome-for-Testing build for Linux arm64 in 113." >&2; exit 1 ;;
    *) echo "Unsupported platform combo: ${os}:${arch}" >&2; exit 1 ;;
  esac
  export CFT_PLATFORM DRIVER_PLATFORM CHROME_BIN_SUBPATH
}

download_and_unzip() {
  local url="$1"
  local dest="$2"
  local zipfile
  zipfile=$(basename "$url")

  echo "[download] $url"
  mkdir -p "$dest"
  rm -rf "${dest:?}"/*

  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$url" -o "$zipfile"
  else
    wget -q "$url" -O "$zipfile"
  fi

  if command -v unzip >/dev/null 2>&1; then
    unzip -q -o "$zipfile" -d "$dest"
  else
    if [[ "$DRIVER_PLATFORM" == win32 ]]; then
      powershell -NoProfile -Command "Expand-Archive -LiteralPath '${zipfile}' -DestinationPath '${dest}' -Force"
    else
      echo "unzip not found; please install unzip." >&2
      exit 3
    fi
  fi

  rm -f "$zipfile"
}

detect_platform

# 1) Install Chrome 113 (Chrome for Testing bucket)
CHROME_DEST="chrome_deps/chrome/${CFT_PLATFORM}-${VERSION}"
CHROME_URL="https://storage.googleapis.com/chrome-for-testing-public/${VERSION}/${CFT_PLATFORM}/chrome-${CFT_PLATFORM}.zip"
download_and_unzip "$CHROME_URL" "$CHROME_DEST"
CHROME_BIN="${CHROME_DEST}/${CHROME_BIN_SUBPATH}"
[ -x "$CHROME_BIN" ] || { echo "Chrome binary not found at ${CHROME_BIN}"; exit 4; }
"$CHROME_BIN" --version || true

# 2) Install matching ChromeDriver 113 (old storage bucket)
DRIVER_DEST="chrome_deps/chromedriver113"
DRIVER_URL="https://chromedriver.storage.googleapis.com/${VERSION}/chromedriver_${DRIVER_PLATFORM}.zip"
download_and_unzip "$DRIVER_URL" "$DRIVER_DEST"
CHROMEDRIVER_BIN=$(find "$DRIVER_DEST" -type f -name "chromedriver*" | head -n1)
[ -x "$CHROMEDRIVER_BIN" ] || { echo "Chromedriver binary not found in ${DRIVER_DEST}"; exit 5; }
"$CHROMEDRIVER_BIN" --version || true

echo "[install] Done."
echo "Chrome:       $CHROME_BIN"
echo "ChromeDriver: $CHROMEDRIVER_BIN"

mkdir -p "./chrome_deps/bin"
BIN_DIR="$(realpath ./chrome_deps/bin)"

ln -sf "$(realpath "$CHROME_BIN")" "$BIN_DIR/chrome113"
ln -sf "$(realpath "$CHROMEDRIVER_BIN")" "$BIN_DIR/chromedriver113"
echo "[install] Symlinks created in $BIN_DIR:"
