def textEditor(input):
    ordered = sorted(input) # sorts in chrnological order
    ret_val = ''
    stack = [] # needed for undo/redo
    selected_data = []
    queue = []
    for order in ordered:
        command = order[1]
        if command == 'APPEND':
            queue = []
            data = order[2]
            if selected_data:
                ret_val = ret_val[:selected_data[0]] + data + ret_val[selected_data[1]:]
                selected_data = []
            else:    
                ret_val += data
            stack.append(ret_val)
        elif command == 'BACKSPACE':
            queue = []
            if not selected_data:
                ret_val = ret_val[:-1]
            else:
                ret_val = ret_val[0:selected_data[0]] + ret_val[selected_data[1]:]
                selected_data = []
            stack.append(ret_val)
        elif command == 'REDO':
            if queue:
                ret_val = queue.pop(0)
        elif command == 'UNDO':
            if stack:
                last = stack.pop()
                queue = [last] + queue
                if stack:
                    ret_val = stack[-1]
                else:
                    ret_val = ''
            
        elif command == 'SELECT':
            queue = []
            selected_data = [int(order[2]), int(order[3])]
        elif command == 'BOLD':
            queue = []
            ret_val = ret_val[:selected_data[0]] + '*' + ret_val[selected_data[0]:selected_data[1]] + '*' + ret_val[selected_data[1]:]
            stack.append(ret_val)
    return ret_val        