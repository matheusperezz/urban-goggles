def count_valid_elements(n, tags):
    valid_tags = {"html", "head", "title", "body", "h1"}
    stack = []
    valid_element_count = 0
    
    for tag in tags:
        if tag.startswith("<") and not tag.startswith("</"):
            element = tag[1:-1]
            if element in valid_tags:
                stack.append(element)
        elif tag.startswith("</"):
            element = tag[2:-1]
            if stack and stack[-1] == element:
                stack.pop()
                valid_element_count += 1
            else:
                return "Em construcao"
    
    if stack:
        return "Em construcao"
    
    return valid_element_count

n = int(input())
tags = [input().strip() for _ in range(n)]
result = count_valid_elements(n, tags)
print(result)
