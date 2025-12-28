#!/usr/bin/env python3
"""
Commit Message AI Bullshitter - Because 'fixed stuff' wasn't vague enough.
"""

import random
import sys
import subprocess
from datetime import datetime

# Corporate buzzword bingo cards
BUZZWORDS = [
    "synergize", "leverage", "paradigm", "disrupt", "innovate",
    "streamline", "optimize", "scale", "robust", "agile",
    "cloud-native", "microservices", "blockchain", "AI-driven", "quantum"
]

# Pretentious technical terms
TECH_TERMS = [
    "refactor", "technical debt", "edge case", "regression", "hotfix",
    "technical spike", "proof of concept", "minimum viable product"
]

# Vague action verbs that sound important
ACTIONS = [
    "enhance", "revolutionize", "reimagine", "transform", "modernize",
    "future-proof", "hardening", "productionalize"
]

# Classic excuses
EXCUSES = [
    "due to legacy constraints", "for backward compatibility",
    "addressing technical debt", "improving developer experience",
    "following industry best practices"
]


def generate_bullshit() -> str:
    """Generate a commit message that sounds smart but says nothing."""
    
    # Pick random components
    action = random.choice(ACTIONS)
    buzzword = random.choice(BUZZWORDS)
    tech_term = random.choice(TECH_TERMS)
    excuse = random.choice(EXCUSES)
    
    # Random template selection
    templates = [
        f"{action} {buzzword} {tech_term} {excuse}",
        f"{action}: {buzzword} implementation for {tech_term}",
        f"{tech_term}: {action} {buzzword} capabilities",
        f"{action} {tech_term} to improve {buzzword} {excuse}"
    ]
    
    return random.choice(templates).title()


def main():
    """Main function - because every script needs one."""
    print("\n🤖 AI Bullshitter 9000 Activated 🤖\n")
    print("Your profound commit message:")
    print("-" * 40)
    
    for _ in range(3):  # Give them options, they love options
        print(f"• {generate_bullshit()}")
    
    print("\nPro tip: Pick the one that sounds most expensive.")
    print("\n(Actual tip: Write meaningful commit messages, you animal)")


if __name__ == "__main__":
    main()