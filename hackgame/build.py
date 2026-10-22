#!/usr/bin/env python3
"""
  build.py — Compile hackgame.py into a standalone .exe
  Works on Windows, macOS, and Linux.
  Run:  python build.py
"""

import subprocess, sys, os, shutil

def run(cmd):
    print(f"  → {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode != 0:
        print(f"\n  ✗ Command failed with exit code {result.returncode}")
        sys.exit(1)

def main():
    print("\n  ╔══════════════════════════════════╗")
    print("  ║   HACKGAME — EXE Builder         ║")
    print("  ╚══════════════════════════════════╝\n")

    # ── 1. Install PyInstaller ────────────────────────────────────────────
    print("  [1/3] Installing PyInstaller...")
    run([sys.executable, "-m", "pip", "install", "--quiet", "pyinstaller"])

    # ── 2. Run PyInstaller ───────────────────────────────────────────────
    print("\n  [2/3] Compiling hackgame.py...")
    run([
        sys.executable, "-m", "PyInstaller",
        "--onefile",          # single .exe, no folder mess
        "--console",          # keep the terminal window (it's a terminal game!)
        "--name", "hackgame", # output name
        "hackgame.py"
    ])

    # ── 3. Move .exe to project root ──────────────────────────────────────
    print("\n  [3/3] Moving output...")
    dist_dir = os.path.join(os.path.dirname(__file__), "dist")
    exe_name = "hackgame.exe" if sys.platform == "win32" else "hackgame"
    src = os.path.join(dist_dir, exe_name)
    dst = os.path.join(os.path.dirname(__file__), exe_name)

    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"\n  ✓ Done! Your executable is ready:\n")
        print(f"      {os.path.abspath(dst)}\n")
        print("  Run it with:")
        if sys.platform == "win32":
            print("      hackgame.exe\n")
        else:
            print("      ./hackgame\n")
    else:
        print(f"  ✗ Could not find output at {src}")
        print("    Check the 'dist/' folder manually.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
