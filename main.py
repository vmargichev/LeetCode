def filter_messages(messages):
    msg_filtered = []
    msg_part_filter = []
    words_filtered = []
    msg_filtering = []

    for sentance in messages:
        count = 0
        msg_filtering = sentance.split()
        for word in msg_filtering:
            if word == "dang":
                count += 1
            else:
                msg_part_filter.append(word)
        new_sentance = " ".join(msg_part_filter)
        msg_filtered.append(new_sentance)
        words_filtered.append(count)
        del msg_part_filter[:]
    return msg_filtered,

    
            
                
                
        
