import os
import re
import requests
from pathlib import Path
from datetime import datetime, timezone


# ============================================================
# CONFIG
# ============================================================

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

NOTION_VERSION = "2026-03-11"

NOTION_API = "https://api.notion.com/v1"
LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}

LEETCODE_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0",
}


# ============================================================
# LEETCODE METADATA
# ============================================================

def get_leetcode_metadata(slug):

    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            titleSlug
            difficulty
            topicTags {
                name
                slug
            }
        }
    }
    """

    variables = {
        "titleSlug": slug
    }

    response = requests.post(
        LEETCODE_GRAPHQL,
        headers=LEETCODE_HEADERS,
        json={
            "query": query,
            "variables": variables
        },
        timeout=30
    )

    if not response.ok:
        print(
            f"LeetCode API error for {slug}: "
            f"{response.status_code}"
        )
        return None

    data = response.json()

    question = (
        data
        .get("data", {})
        .get("question")
    )

    if not question:
        print(
            f"Could not find LeetCode problem: {slug}"
        )
        return None

    return question


# ============================================================
# NOTION HELPERS
# ============================================================

def notion_request(method, endpoint, **kwargs):

    url = f"{NOTION_API}{endpoint}"

    response = requests.request(
        method,
        url,
        headers=NOTION_HEADERS,
        **kwargs
    )

    if not response.ok:
        print("\nNotion API Error")
        print("Status:", response.status_code)
        print(response.text)
        response.raise_for_status()

    return response.json()


def get_data_source_id():
    """
    Resolve the data source ID from the Notion database ID.
    """

    response = notion_request(
        "GET",
        f"/databases/{NOTION_DATABASE_ID}"
    )

    data_sources = response.get("data_sources", [])

    if not data_sources:
        raise RuntimeError(
            "No data source was found inside the Notion database."
        )

    data_source_id = data_sources[0]["id"]

    print(
        f"Resolved Notion data source ID: {data_source_id}"
    )

    return data_source_id


def get_existing_pages(data_source_id):

    existing = {}

    payload = {
        "page_size": 100
    }

    response = notion_request(
        "POST",
        f"/data_sources/{data_source_id}/query",
        json=payload
    )

    for page in response.get("results", []):

        properties = page.get(
            "properties",
            {}
        )

        url_property = properties.get(
            "LeetCode URL"
        )

        if not url_property:
            continue

        url = url_property.get("url")

        if url:
            existing[
                url.rstrip("/")
            ] = page["id"]

    return existing


# ============================================================
# PROPERTY BUILDERS
# ============================================================

def title_property(value):

    return {
        "title": [
            {
                "text": {
                    "content": value
                }
            }
        ]
    }


def select_property(value):

    return {
        "select": {
            "name": value
        }
    }


def multi_select_property(values):

    return {
        "multi_select": [
            {
                "name": value
            }
            for value in values
        ]
    }


def status_property(value):

    return {
        "status": {
            "name": value
        }
    }


def url_property(value):

    return {
        "url": value
    }


def date_property(value):

    return {
        "date": {
            "start": value
        }
    }


# ============================================================
# LANGUAGE DETECTION
# ============================================================

def detect_language(folder):

    extensions = {
        ".py": "Python",
        ".cpp": "C++",
        ".cc": "C++",
        ".cxx": "C++",
        ".java": "Java",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".c": "C",
        ".cs": "C#",
        ".go": "Go",
        ".rs": "Rust",
        ".php": "PHP",
        ".rb": "Ruby",
        ".kt": "Kotlin",
        ".swift": "Swift",
        ".sql": "SQL",
    }

    for file in folder.iterdir():

        if not file.is_file():
            continue

        extension = file.suffix.lower()

        if extension in extensions:
            return extensions[extension]

    return "Unknown"


# ============================================================
# GITHUB PROBLEM SCANNER
# ============================================================

def scan_repository():

    root = Path(".")

    problems = []

    for folder in root.iterdir():

        if not folder.is_dir():
            continue

        match = re.match(
            r"^(\d+)-(.+)$",
            folder.name
        )

        if not match:
            continue

        number = match.group(1)
        slug = match.group(2)

        print(
            f"\nFound repository problem: "
            f"{number} - {slug}"
        )

        metadata = get_leetcode_metadata(slug)

        if not metadata:

            print(
                "  ⚠ Could not retrieve metadata"
            )

            continue

        tags = [
            tag["name"]
            for tag in metadata.get(
                "topicTags",
                []
            )
        ]

        language = detect_language(folder)

        problem = {
            "number": number,
            "slug": slug,
            "title": metadata["title"],
            "difficulty": metadata["difficulty"],
            "tags": tags,
            "language": language,
            "url":
                f"https://leetcode.com/problems/{slug}/",
            "date":
                datetime.now(
                    timezone.utc
                ).date().isoformat(),
        }

        problems.append(problem)

        print(
            f"  ✓ {metadata['title']}"
        )

        print(
            f"  Difficulty: "
            f"{metadata['difficulty']}"
        )

        print(
            f"  Tags: "
            f"{', '.join(tags)}"
        )

        print(
            f"  Language: {language}"
        )

    return problems


# ============================================================
# CREATE NOTION PAGE
# ============================================================

def create_notion_problem(
    problem,
    data_source_id
):

    properties = {

        "Problem Name":
            title_property(
                problem["title"]
            ),

        "Difficulty":
            select_property(
                problem["difficulty"]
            ),

        "Problem Tag":
            multi_select_property(
                problem["tags"]
            ),

        "Status":
            status_property(
                "Completed"
            ),

        "Submission Date":
            date_property(
                problem["date"]
            ),

        "Language":
            select_property(
                problem["language"]
            ),

        "LeetCode URL":
            url_property(
                problem["url"]
            ),
    }

    payload = {
        "parent": {
            "data_source_id":
                data_source_id
        },

        "properties": properties,
    }

    return notion_request(
        "POST",
        "/pages",
        json=payload
    )


# ============================================================
# MAIN SYNC
# ============================================================

def main():

    print("=" * 60)
    print("LeetCode → Notion Sync")
    print("=" * 60)

    print(
        "\nResolving Notion data source..."
    )

    data_source_id = get_data_source_id()

    print(
        "\nReading existing Notion entries..."
    )

    existing = get_existing_pages(
        data_source_id
    )

    print(
        f"Existing entries: "
        f"{len(existing)}"
    )

    print(
        "\nScanning GitHub repository..."
    )

    problems = scan_repository()

    print(
        f"\nProblems found: "
        f"{len(problems)}"
    )

    created = 0
    skipped = 0

    for problem in problems:

        url = problem["url"].rstrip("/")

        print(
            f"\nProcessing: "
            f"{problem['title']}"
        )

        if url in existing:

            print(
                "  → Already exists"
            )

            skipped += 1

            continue

        create_notion_problem(
            problem,
            data_source_id
        )

        print(
            "  ✓ Added to Notion"
        )

        created += 1

    print("\n" + "=" * 60)
    print("SYNC COMPLETE")
    print("=" * 60)

    print(
        f"Created: {created}"
    )

    print(
        f"Skipped: {skipped}"
    )


if __name__ == "__main__":
    main()