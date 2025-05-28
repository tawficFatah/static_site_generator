import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH       = 'paragraph'
    HEADING         = 'heading'
    CODE            = 'code'
    QUOTE           = 'quote'
    UNORDERED_LIST  = 'unordered_list'
    ORDERED_LIST    = 'ordered_list'

'''
    Assumptions:
        Documents is well formated, i.e. each block is on a seperate line.
'''
def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")
    
    blocks = []
    
    for block in markdown_blocks:
        block = block.strip()
        if block == "":
            continue
        blocks.append(block)

    return blocks
'''
    Assumptions:
        All leading and trailing whitespace were already stripped.
        
    Takes a single block of markdown text as input and returns the BlockType representing the type
    of block it is.
'''
def block_to_block_type(markdown_block):
    heading_pattern         = r'^#{1,6} .+'
    code_block_pattern      = r'^```[\s\S]*?```$'
    quote_block_pattern     = r'^(> .*\n?)+$'
    unordered_list_pattern  = r'^(- .*\n?)+$'
    ordered_list_pattern    = r'^(\d+\. .*\n?)+$'
    
    if check_pattern_match(heading_pattern, markdown_block):
        return BlockType.HEADING
    
    if check_pattern_match(code_block_pattern, markdown_block):
        return BlockType.CODE

    if check_pattern_match(quote_block_pattern, markdown_block):
        return BlockType.QUOTE

    if check_pattern_match(unordered_list_pattern, markdown_block):
        return BlockType.UNORDERED_LIST
    
    if check_pattern_match(ordered_list_pattern, markdown_block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
'''
    Convenience function to check if a regex pattern matches the markdown text.
    True    - match is found
    False   - match not found
'''
def check_pattern_match(pattern, markdown_text):
    return bool(re.match(pattern, markdown_text))