import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = REPO_ROOT / "scripts" / "icb_skill_source.json"
GEMINI_SKILL_PATH = REPO_ROOT / ".agent" / "skills" / "icb_page_generator" / "SKILL.md"
COPILOT_SKILL_PATH = REPO_ROOT / ".agents" / "skills" / "icb_page_generator" / "SKILL.md"
OPENCODE_CONFIG_PATH = REPO_ROOT / "opencode.json"
CLAUDE_COMMANDS_DIR = REPO_ROOT / ".claude" / "commands"


def load_source() -> dict:
    with SOURCE_PATH.open("r", encoding="utf-8") as source_file:
        return json.load(source_file)


def render_skill(source: dict) -> str:
    repo_posix = "."
    resources_root = f"{repo_posix}/.agent/skills/icb_page_generator/resources/"

    def format_lines(values: list[str]) -> list[str]:
        return [value.format(repo_posix=repo_posix) for value in values]

    read_order = format_lines(source["read_order"])

    lines = [
        "---",
        f"name: {source['skill_name']}",
        f"description: {source['description']}",
        "---",
        "",
        f"# {source['title']}",
        "",
        "此檔由 scripts/sync_icb_skill.py 自動產生，請優先修改 scripts/icb_skill_source.json。",
        "",
        "> [!NOTE]",
        "> `.agent/skills/icb_page_generator/SKILL.md`、`.agents/skills/icb_page_generator/SKILL.md` 與 OpenCode instructions 應維持語意一致。",
        f"> 核心知識來源固定為 `{resources_root}` 與 `{repo_posix}/AGENTS.md`。",
        "",
        "## 統一讀取順序",
        ""
    ]

    for index, item in enumerate(read_order, start=1):
        lines.append(f"{index}. {item}")

    lines.extend(["", "## 核心規則", ""])
    for index, item in enumerate(source["core_rules"], start=1):
        lines.append(f"{index}. **{item.split('：', 1)[0]}：** {item.split('：', 1)[1]}")

    lines.extend([
        "",
        "## 依需求讀取的知識庫",
        "",
        f"核心知識資源位於 `{resources_root}`",
        "",
        "| 任務 | 讀取文件 |",
        "|------|---------|"
    ])
    for task, file_name in source["knowledge_map"]:
        lines.append(f"| {task} | `{file_name}` |")

    lines.extend(["", "## 尚未補齊但必須遵守的規則", "", "以下知識文件仍在 `TODO.md` 的待完成項目內；在文件建立前，直接遵守這些限制：", ""])
    for index, item in enumerate(source["pending_rules"], start=1):
        title, body = item.split("：", 1)
        lines.append(f"{index}. **{title}：** {body}")

    lines.extend(["", "## 可用指令", "", "| 指令 | 說明 |", "|------|------|"])
    for command_name, description in source["commands"]:
        lines.append(f"| `{command_name}` | {description} |")

    lines.extend(["", "## 輸出原則", ""])
    for index, item in enumerate(source["output_principles"], start=1):
        lines.append(f"{index}. {item}")

    lines.extend(["", "## Resources 目錄", "", "```", resources_root])
    for file_name in source["resource_files"]:
        lines.append(f"├── {file_name}" if file_name != source["resource_files"][-1] else f"└── {file_name}")
    lines.extend(["```", ""])
    return "\n".join(lines)


def update_opencode(source: dict) -> None:
    with OPENCODE_CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    config["instructions"] = source["opencode_instructions"]

    with OPENCODE_CONFIG_PATH.open("w", encoding="utf-8", newline="\n") as config_file:
        json.dump(config, config_file, ensure_ascii=False, indent=2)
        config_file.write("\n")


def update_claude_commands(source: dict) -> None:
    commands = source.get("claude_commands")
    if not commands:
        return

    CLAUDE_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
    for command in commands:
        file_name = command["file"]
        content = command["content"].rstrip("\n") + "\n"
        (CLAUDE_COMMANDS_DIR / file_name).write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    source = load_source()
    rendered_skill = render_skill(source)

    for output_path in (GEMINI_SKILL_PATH, COPILOT_SKILL_PATH):
        output_path.write_text(rendered_skill, encoding="utf-8", newline="\n")

    update_opencode(source)
    update_claude_commands(source)
    print("Synchronized ICB skill entry points.")


if __name__ == "__main__":
    main()
