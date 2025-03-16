import pygame

def limit_vector(vector, max_length):
    """Limits the length of a vector."""
    if vector.length() > max_length:
        vector.scale_to_length(max_length)
    return vector
