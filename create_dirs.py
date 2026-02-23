import os

base = r"H:\Github\Project\PET"
dirs = [
    os.path.join(base, "\u5361\u7247", "\u5de5\u5177"),
    os.path.join(base, "\u5361\u7247", "\u6846\u67b6"),
    os.path.join(base, "\u5361\u7247", "\u7406\u8bba"),
    os.path.join(base, "\u5361\u7247", "\u539f\u5219"),
    os.path.join(base, "\u5361\u7247", "\u6848\u4f8b"),
    os.path.join(base, "\u5361\u7247", "\u7ec3\u4e60"),
    os.path.join(base, "\u5361\u7247", "\u53cd\u6a21\u5f0f"),
    os.path.join(base, "MOC"),
]
for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created: {d}")
print("All directories created.")
