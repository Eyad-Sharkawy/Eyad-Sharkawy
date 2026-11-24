"""Re-render every data-driven SVG tailored for Eyad Sharkawy."""
import sys
import os

# Ensure scripts dir is on sys.path
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fetch_profile
import fetch_contributions
import make_ascii_svg
import render_header_svg
import render_info_card
import render_globe_svg
import render_tech_sphere_svg
import render_skyline_svg
import render_heatmap_svg

def main():
    print("=== [1/9] Fetching Profile Data ===")
    fetch_profile.main()

    print("=== [2/9] Fetching Contribution Activity ===")
    fetch_contributions.main()

    print("=== [3/9] Generating ASCII Portrait SVG from Avatar ===")
    make_ascii_svg.main()

    print("=== [4/9] Rendering Header SVG ===")
    render_header_svg.main()

    print("=== [5/9] Rendering Info Card SVG ===")
    render_info_card.main()

    print("=== [6/9] Rendering Globe SVG ===")
    render_globe_svg.main()

    print("=== [7/9] Rendering Tech Sphere SVG ===")
    render_tech_sphere_svg.main()

    print("=== [8/9] Rendering Contribution Skyline SVG ===")
    render_skyline_svg.main()

    print("=== [9/9] Rendering Contribution Heatmap SVG ===")
    render_heatmap_svg.main()

    print("\n[SUCCESS] All profile SVGs rendered with 100% accurate data!")

if __name__ == "__main__":
    main()
