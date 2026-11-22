"""Obstacle detector for the Kestrel-1 camera."""
import os

THRESHOLD_CM = 30


def detect_obstacle(distance_cm, threshold_cm=THRESHOLD_CM):
    """Return True when something is closer than threshold_cm."""
    return distance_cm < threshold_cm


def closest(distances):
    """Return the smallest distance in the list, or None when it is empty."""
    return min(distances) if distances else None
