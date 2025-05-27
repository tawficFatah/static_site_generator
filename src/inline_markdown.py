from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    #print(f"in split_nodes_delimeter. delimeter:{delimeter}, text_type:{text_type}")
    new_nodes = []
    for old_node in old_nodes:
        # If an "old node" is not a TextType.TEXT type, just add it to the new
        # list as-is,
        # we only attempt to split "text" type objects (not bold, italic, etc).
        #print(f"Before if: node: {old_node}")
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # first, we need to chek if the delimeters match.
        # check if the splitters match
        indexes = [delimeter_index for delimeter_index in range(len(old_node.text)) if old_node.text.startswith(delimeter, delimeter_index)]
        #print(f"indexes: {indexes}")
        
        if not check_dlimeter_match(indexes):
            raise ValueError("invalid open/closing {delimeter} pair")

        none_text_parts = []
        for index in range(0, len(indexes), 2):
            open_index  = indexes[index]
            close_index = indexes[index + 1]
            
            # skip the delimiter
            str_start_index = open_index + len(delimeter)
            none_text_parts.append(old_node.text[str_start_index:close_index])

        # Now, get the new nodes for that node
        node_parts = old_node.text.split(delimeter)
        generated_nodes = create_nodes_from_node(node_parts, none_text_parts, text_type)

        # extend the current nodes list
        new_nodes.extend(generated_nodes)      
    return new_nodes
'''
Check if the delimeters match. If we have an even number, they do, otherwise, they don't.
'''
def check_dlimeter_match(indexes):
    if len(indexes) % 2 == 0:
        return True
    
    return False

def create_nodes_from_node(node_parts, none_text_parts, text_type):
    nodes = []
    
    for node_part in node_parts:
        if node_part in none_text_parts:
            nodes.append(TextNode(node_part, text_type))
        elif node_part.strip() == "":
            continue
        else:
            nodes.append(TextNode(node_part, TextType.TEXT))
            
    return nodes

def split_text(text_str, splitter):
    # check if the splitters match
    indexes = [splitter_index for splitter_index in range(len(text_str)) if text_str.startswith(splitter, splitter_index)]
    print(f"indexes: {indexes}")
    
    if len(indexes) % 2 == 0:
        print("Valid formatting")
        # Debug. List the string(s)
        for index in range(0, len(indexes), 2):
            open_index  = indexes[index]
            close_index = indexes[index + 1]
            
            # skip the delimiter
            str_start_index = open_index + len(splitter)
            print(f"string at [{str_start_index}:{close_index}]: {text_str[str_start_index:close_index]}")

        print("Text")
        print(text_str)    
        print("parts")
        parts = text_str.split(splitter)
        print(parts)
    else:
        print("Invalid formatting")