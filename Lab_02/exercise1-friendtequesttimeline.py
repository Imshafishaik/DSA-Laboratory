def friend_request_timeline(message): 
    uppercase = 0 
    alphabetic = 0 
    punctuation = 0 
    repeated = False 

    prev_char = '' 
    repeat_count = 1 

    for c in message: 
        if c.isalpha(): 
            alphabetic += 1 
            if c.isupper(): 
                uppercase += 1 

        if c in ('!', '?'): 
            punctuation += 1 
        if c == prev_char: 
            repeat_count += 1 
            if repeat_count > 3: 
                repeated = True 
        else: 
            repeat_count = 1 
            prev_char = c 

    caps_ratio = (uppercase / alphabetic) if alphabetic > 0 else 0 

    if caps_ratio >= 0.6 or punctuation >= 5: 
        classification = "AGGRESSIVE" 
    elif caps_ratio >= 0.3 or punctuation >= 3: 
        classification = "URGENT" 
    else: 
        classification = "CALM" 

    return { 
        "uppercase_count": uppercase, 
        "punctuation_count": punctuation, 
        "caps_ratio": round(caps_ratio, 2), 
        "classification": classification, 
        "repeated_chars": repeated 
    } 

messages = [ 
    "Hey, want to connect?", 
    "PLEASE ACCEPT MY REQUEST!!!", 
    "Are you free? I need to talk!!!", 
    "heyyyyy, let's meet up!" 
] 

for msg in messages: 
    result = friend_request_timeline(msg) 
    print(f"Message: {msg}") 
    print(result) 
    print("-" * 50) 