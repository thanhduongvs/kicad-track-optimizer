# ![icon](icon.png) KiCad Track Optimizer

<img src="https://img.shields.io/badge/KiCad-v10-brightgreen?style=for-the-badge&logo=KiCad"> <img src="https://img.shields.io/badge/kicad--python-v0.7.1-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/PySide6-Qt-brightgreen?style=for-the-badge">

A powerful Python-based plugin designed to automatically clean up, optimize traces, manipulate geometry, and route high-speed differential pairs in **KiCad PCB designs**.

When modifying dense layouts, it is easy to leave behind microscopic unconnected stubs or accidentally draw overlapping tracks. This tool acts as an advanced geometric sweeper to clean your board instantly. Furthermore, it includes precision alignment tools and a smart breakout generator for differential pairs to ensure perfectly symmetrical and deskewed routing from IC pads.

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <img src="./images/gui1.png" alt="SOM RZ/V2L" width="100%" />
    </td>
    <td width="33%" align="center" valign="top">
      <img src="./images/gui2.png" alt="SOM RZ/V2H" width="100%" />
    </td>
  </tr>
</table>

## 🚀 Key Features

### 🧹 Track Optimization
* **Recursive Stub Removal:** Safely hunts down and deletes dangling track ends, even if they are made of multiple chained segments, without touching valid pads or vias.
* **Collinear & Overlap Merging:** Uses advanced vector projection to find tracks that are parallel and overlapping, merging them into a single continuous trace.
* **Smart Net Awareness:** Fully respects KiCad's electrical rules. It will never merge tracks of different nets or different widths, preventing accidental short circuits.

### 🎯 Precision Alignment & Joining *(New)*
* **Track Joiner:** Select two intersecting tracks, and the tool will automatically calculate their intersection point and snap their endpoints together, creating a perfect geometric corner.
* **Center Track to Pads:** Select exactly 2 pads and 1 (or 2) tracks. The tool calculates the exact midpoint and dynamically translates the tracks to be perfectly centered between the pads, maintaining the differential gap.
* **Align Perpendicular to Pads:** Select exactly 2 pads and 1 (or 2) tracks. The tool automatically rotates and centers the tracks so they are perfectly perpendicular to the imaginary line connecting the two pads.

### ⚡ Differential Pair Breakout
* **Auto-Deskewed Breakout:** Automatically calculates and routes perfectly symmetrical escape tracks from two selected pads, compensating for any initial pad misalignment.
* **Customizable Escapes:** Generates breakouts with customizable track widths, gaps, escape lengths, and routing angles (Perpendicular, 45°, 22.5°, etc.).
* **Flip Direction:** Easily reverse the escape routing direction with a single click to adapt to your surrounding layout.

* **Safe & Reversible:** All operations (both cleaning and routing) are wrapped in native KiCad commits, allowing you to easily `Ctrl+Z` (Undo) the entire process if needed.

## 🖥️ Usage

1. Open **PCB Editor**.
2. Go to **Tools** -> **External Plugins** -> **Track Optimizer** (or click the icon on the top toolbar).
3. **For Track Cleanup:**
   - Go to the **Track Optimizer** tab.
   - Choose to remove stubs, merge collinear tracks, or do both.
   - Click the respective button.
4. **For Track Alignment & Joining:**
   - Select the required items on your PCB (e.g., 2 tracks for joining, or 2 pads + tracks for alignment).
   - Go to the **Track Optimizer** tab.
   - Click **Track Joiner**, **Center Track to Pads**, or **Align Tracks Perpendicular to Pads**.
5. **For Differential Pairs:**
   - Select exactly **2 pads** on your PCB.
   - Go to the **Differential Pair** tab.
   - Set your desired Width, Gap, Escape Length, and Escape Mode (supports both mm and mil).
   - Check "Flip escape direction" if you want the tracks to route to the opposite side.
   - Click **Breakout Diff Pair**.

## 🛠️ Installation

### Via KiCad Plugin and Content Manager (Recommended)
Add our custom repo to **the Plugin and Content Manager**, the URL is:
`https://raw.githubusercontent.com/thanhduongvs/kicad-repository/main/repository.json`

![pcm](images/pcm.png)

### Manual Installation
- Download the plugin source code as **a .zip** file.
- Locate your KiCad plugins folder:
  - **Windows:** `Documents\KiCad\10.0\plugins` (or `9.0\plugins`)
  - **Linux:** `~/.local/share/kicad/10.0/plugins` (or `9.0/plugins`)
  - **macOS:** `~/Documents/KiCad/10.0/plugins` (or `9.0/plugins`)
- Extract the archive to the KiCad plugins directory.
- Restart KiCad / PCB Editor.

## 📦 Libraries Used
This project relies on several powerful open-source libraries:
 - [kicad-python](https://pypi.org/project/kicad-python/): KiCad API Python Bindings.
 - [PySide6](https://pypi.org/project/PySide6/): The official Python module from the Qt for Python project, used for the graphical user interface.

## 📜 License and Credits
Plugin code licensed under MIT, see `LICENSE` for more info.
