#!/usr/bin/env python3
"""Task 1: Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class representing a geometric shape"""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass

class Circle(Shape):
    """Circle implementation of Shape"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate circle area: πr²"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle perimeter: 2πr"""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle implementation of Shape"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area: width × height"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter: 2(width + height)"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print area and perimeter of any shape-like object
    
    Args:
        shape: An object implementing area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
