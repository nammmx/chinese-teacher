import os
import json

base_path = os.getcwd()
root_dir = os.path.join(base_path, "chinese_lessons")

# Subfolders for lesson sections
lesson_sections = [
    "hook",
    "core_lesson",
    "quick_example",
    "cultural_nugget",
    "call_to_action"
]

# Utility files
utils_files = [
    "base_scene.py",
    "style_loader.py",
    "config_loader.py",
    "animation_helpers.py"
]

# Asset subfolders
assets_subfolders = [
    "shared_fonts", "images", "sounds", "backgrounds", "styles"
]

# Create root folder
os.makedirs(root_dir, exist_ok=True)

# === 01_wo/ Sample Lesson ===
lesson_id = "01_wo"
lesson_path = os.path.join(root_dir, lesson_id)
os.makedirs(lesson_path, exist_ok=True)

# Create section subfolders and scene files
for section in lesson_sections:
    section_path = os.path.join(lesson_path, section)
    os.makedirs(section_path, exist_ok=True)
    scene_file = os.path.join(section_path, f"{section}_scene.py")
    with open(scene_file, "w") as f:
        f.write(f"# {section}_scene.py – scene script for the {section.replace('_', ' ').title()} section\n")

# Create config.json with placeholder content
config_data = {
    "character": "我",
    "pinyin": "wǒ",
    "translation": "I, me",
    "example_sentence": {
        "chinese": "我是学生。",
        "pinyin": "Wǒ shì xuéshēng.",
        "english": "I am a student."
    },
    "colors": {
        "background": "#f9f5f0",
        "text": "#1d3557"
    },
    "style": "ghibli"
}
with open(os.path.join(lesson_path, "config.json"), "w", encoding="utf-8") as f:
    json.dump(config_data, f, ensure_ascii=False, indent=4)

# === Placeholder 02_ai/ folder ===
os.makedirs(os.path.join(root_dir, "02_ai"), exist_ok=True)

# === Assets ===
assets_path = os.path.join(root_dir, "assets")
os.makedirs(assets_path, exist_ok=True)
for sub in assets_subfolders:
    os.makedirs(os.path.join(assets_path, sub), exist_ok=True)

# === Utils ===
utils_path = os.path.join(root_dir, "utils")
os.makedirs(utils_path, exist_ok=True)
for file in utils_files:
    with open(os.path.join(utils_path, file), "w") as f:
        f.write(f"# {file} – utility module\n")

# === Render Script at Project Root ===
render_script = os.path.join(base_path, "render.py")
with open(render_script, "w") as f:
    f.write("# render.py – master script to render scenes for any word\n")

print("✓ Full structure created exactly as shown in your reference image.")