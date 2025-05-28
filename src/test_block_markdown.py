import unittest
from block_markdown import (
    markdown_to_blocks,
    BlockType,
    block_to_block_type,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_block(self):
        markdown = "# This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_code_block(self):
        markdown = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_quote_block(self):
        markdown = "> This is a quote\n> that spans two lines"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_unordered_list_block(self):
        markdown = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        markdown = "1. First item\n2. Second item"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        markdown = "This is a normal paragraph of text."
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()