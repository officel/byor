#!/usr/bin/env python3

import json
import os

import frontmatter

# 固定ディレクトリのリスト
directories = [
    "./radar/techniques",
    "./radar/tools",
    "./radar/platforms",
    "./radar/languages_frameworks",
]


# ディレクトリ内のすべてのマークダウンファイルを検索
def find_markdown_files(directories):
    markdown_files = []
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".md"):
                    markdown_files.append(os.path.join(root, file))
    return markdown_files


# Frontmatterを抽出して変数化
def extract_frontmatter(files):
    frontmatter_list = []
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            post = frontmatter.load(file)
            if "byor" in post.metadata:
                frontmatter_list.append(post.metadata["byor"])
    return frontmatter_list


# JSONとして出力
def output_json(frontmatter_data):
    with open("Office_L.json", "w", encoding="utf-8") as json_file:
        json.dump(frontmatter_data, json_file, ensure_ascii=False, indent=4)
        json_file.write("\n")


# メイン関数
def main():
    markdown_files = find_markdown_files(directories)
    frontmatter_data = extract_frontmatter(markdown_files)
    output_json(frontmatter_data)


if __name__ == "__main__":
    main()
