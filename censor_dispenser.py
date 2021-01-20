# Read emails
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Censor a word or phrase from the first email
def censor_words(word, text):
    term = ""
    for w in word:
      if w.isalpha():
        term += '#'
      else:
        term += w
    return text.replace(word, term)   
  

# print(censor_words('learning algorithms', email_one))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
# Censor the second email for a list of proprietary terms
def censor_list(text, censored_terms):
  
  for term in censored_terms:
      censored_word = ""
      for t in term:
          if t.isalpha():
            censored_word += '#'  
          else:
            censored_word += t
      text = text.replace(term, censored_word) 

  # Repeating code to handle capitalized terms
  for term in censored_terms:
      term = term.capitalize()
      censored_word = ""
      for t in term:
        if t.isalpha():
          censored_word += '#'  
        else:
          censored_word += t
      text = text.replace(term, censored_word) 

  return text
  
  
# print(censor_list(email_two, proprietary_terms))


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
# Censor the occurance of negative words after any of them has occurred twice, plus the list of proprietary terms. 
def censor_lists(neg_words, censored_terms, text):
    count = 0
    text_list = text.split()
    for term in text_list:
      if any(word == term for word in neg_words):
        count += 1
        censored_word = ""
        if count > 2:
            for t in term:
              if t.isalpha():
                censored_word += '#'
              else:
                censored_word += t
            text = text.replace(term, censored_word)

    # Handling phrases from the negative_words list
    for word in neg_words:
      if " " in word:
        censored_word = ""
        for w in word:
          if w.isalpha():
            censored_word += "#"
          else:
            censored_word += w  
        text = text.replace(word, censored_word)   

    # Handling capitalized terms
    for word in neg_words:
      word = word.capitalize()
      censored_word = ""
      for w in word:
          if w.isalpha():
            censored_word += '#'  
          else:
            censored_word += w
      text = text.replace(word, censored_word) 

    # Censor proprietary terms
    for term in censored_terms:
        censored_term = ""
        for t in term:
            if t.isalpha():
              censored_term += '#'
            else:
              censored_term += t
        text = text.replace(term, censored_term)
            
    return text
      
# print(censor_lists(negative_words, proprietary_terms, email_three))

# Censor the list of negative words, the list of proprietaty terms, plus any word that comes before and after a term from these lists
def heavy_censoring(text):

  censor_list = negative_words + proprietary_terms

  text = text.split("\n")

  for paragraph in text:
    word_list = paragraph.split(' ')
    
    # Censor the phrases from the censor_list
    for term in censor_list:
      if " " in term:
        phrase = term
        if phrase in paragraph:
          phrase = phrase.split(" ")
          for word in phrase:
            if word in word_list:
              target = word
              for i in range(len(word_list)):
                word_in_text = word_list[i].lower().split('.')[0].split('!')[0]
                if word_in_text == target:
                  word_in_text = word_list[i]
                  censored_word = ''
                  for ele in word_list[i]:
                      if ele.isalpha():
                        censored_word += '#'
                      else:
                        censored_word += ele

                  word_list[i] = word_list[i].replace(word_list[i], censored_word)
                  
                  # Censor the previous word
                  before_phrase = word_list[i-1]
                  censored_word = ''
                  for ele in before_phrase:
                    if ele.isalpha():
                      censored_word += '#'
                    else:
                      censored_word += ele

                  word_list[i-1] = word_list[i-1].replace(before_phrase, censored_word)  
    
                  # Censor the following word
                  after_phrase = word_list[i+1]
                  censored_word = ''
                  for ele in after_phrase:
                    if ele.isalpha():
                      censored_word += '#'
                    else:
                      censored_word += ele
                  
                  word_list[i+1] = word_list[i+1].replace(after_phrase, censored_word)

    # Censor the words from the censor_list
    for i in range(len(word_list)):
      word_in_text = word_list[i].lower().split('.')[0].split('!')[0]
      if word_in_text in censor_list:
        target = word_list[i]
        censored_word = ''
        for ele in target:
            if ele.isalpha():
              censored_word += '#'
            else:
              censored_word += ele

        word_list[i] = word_list[i].replace(target, censored_word)

        # Censor the previous word       
        before_target = word_list[i-1]
        censored_word = ''
        for ele in before_target:
          if ele.isalpha():
            censored_word += '#'
          else:
            censored_word += ele

        word_list[i-1] = word_list[i-1].replace(before_target, censored_word)  

        # Censor the following word
        try:
          after_target = word_list[i+1]
          censored_word = ''
          for ele in after_target:
            if ele.isalpha():
              censored_word += '#'
            else:
              censored_word += ele
          
          word_list[i+1] = word_list[i+1].replace(after_target, censored_word)

        except:
          pass  

    new_text = ' '.join(word_list)
      
    print(new_text)
  
heavy_censoring(email_four)
