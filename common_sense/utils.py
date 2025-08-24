"""General utilities that are just common sense."""
def flatten(lst):
    """Flatten a list of lists into a single list.
    >>> flatten([[1,2],[3,4]])
    [1, 2, 3, 4]
    """
    return [item for sublist in lst for item in sublist]

def unique(lst):
    """Return a list of unique elements, preserving order.
    >>> unique([1,2,2,3])
    [1, 2, 3]
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def chunk(lst, size):
    """Split lst into chunks of given size.
    >>> chunk([1,2,3,4,5], 2)
    [[1,2],[3,4],[5]]
    """
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def first(lst, default=None):
    """Return the first element or default if empty."""
    return lst[0] if lst else default

def last(lst, default=None):
    """Return the last element or default if empty."""
    return lst[-1] if lst else default

def is_sorted(lst):
    """Return True if the list is sorted."""
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def flatten_dict(d, parent_key='', sep='.'): 
    """Flatten a nested dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def deep_get(d, keys, default=None):
    """Get a value from nested dicts by a list of keys."""
    for k in keys:
        if isinstance(d, dict) and k in d:
            d = d[k]
        else:
            return default
    return d

def safe_get(lst, idx, default=None):
    """Safely get an index from a list."""
    try:
        return lst[idx]
    except Exception:
        return default

def safe_pop(lst, idx, default=None):
    """Safely pop an index from a list."""
    try:
        return lst.pop(idx)
    except Exception:
        return default

def safe_dict_get(d, key, default=None):
    """Safely get a key from a dict."""
    return d.get(key, default)

def safe_dict_pop(d, key, default=None):
    """Safely pop a key from a dict."""
    return d.pop(key, default)
