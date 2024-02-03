import requests

def wikisearch(query: str):
    """Searches wikipedia for a given query and returns the first paragraph of the article.

    Args:
        query (str): The query to search for.

    Returns:
        str: The first paragraph of the article if article exists, else a message saying that we need more information.
    """
    # HTTP request to Urban Dictionary API
    url = f"https://api.urbandictionary.com/v0/define?term={query.lower()}"
    response = requests.get(url)
    data: dict = response.json()

    # Exctracting the interesting data
    try:
        text: str = data[list(data.keys())[0]][0]['definition']
        permalink: str = data[list(data.keys())[0]][0]['permalink']
    except IndexError:
        return "I'm not sure what you're looking for. Try to be more specific."
    if text is None: # Checking if the article exists
        return "I'm not sure what you're looking for. Try to be more specific."
    text= text.translate({ord(i): None for i in '[](){}'}) # Removing brackets
    return f'__{query} is:__\n' + text + f"\n\n*[Source](<{permalink}>)*"

def which_function(func_to_call: str, query: str):
    """Returns the function that the user is trying to use.

    Args:
        func_to_call (str): The user's query.

    Returns:
        Any: The returns of the called function.
    """
    done: bool = False
    query = query.translate({ord(i): None for i in '!.?:;,'})

    if func_to_call == 'wikisearch':
        i = 1
        while not done:
            lastXWords: str = ' '.join(query.split(" ")[-i:])
            if i >= 10:
                break
            try:
                done = True
                i+=1
                return wikisearch(lastXWords)
            except KeyError:
                i+=1
                done = False
        return "Didn't found anything about your query, try to be more specific."

    raise ModuleNotFoundError("Function not found") # If the function doesn't exist