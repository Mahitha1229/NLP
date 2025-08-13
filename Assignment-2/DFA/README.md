# Simplified English Word Validator using DFA

A Python-based implementation of a **Deterministic Finite Automaton (DFA)** designed to validate simplified English words. This validator accepts non-empty strings composed exclusively of lowercase English letters (`a–z`). It includes:

-  Interactive command-line validation  
-  Batch testing for datasets  
-  DFA visualization using `networkx` and `matplotlib`  
-  Educational insights into automata theory  

---
## Objective
Design and implement a **Deterministic Finite Automaton (DFA)** that recognizes simplified English words according to the following rules:
- The word must start with a lowercase English letter (`a`–`z`).
- The rest of the word may contain only lowercase English letters (`a`–`z`).
- Any uppercase letters, digits, spaces, or special characters make the word invalid.

  ---
  
## Goals

- Demonstrate DFA principles in a practical Python application  
- Provide a reusable validator for string preprocessing tasks  
- Visualize state transitions for educational and debugging purposes  

---

## What is a DFA?

A **Deterministic Finite Automaton (DFA)** is a mathematical model of computation used to recognize patterns within input strings. It consists of:

- A finite set of states  
- An input alphabet  
- A transition function  
- A start state  
- One or more accepting states  

This project uses a DFA to recognize strings that match the regular expression:   
[a–z]+

which is, one or more lowercase English letters.

---

## DFA Transition Table

| Current State | Input Character | Next State |
|---------------|-----------------|------------|
| `start`       | `[a–z]`          | `valid`    |
| `start`       | `other`         | `dead`     |
| `valid`       | `[a–z]`          | `valid`    |
| `valid`       | `other`         | `dead`     |
| `dead`        | `any`           | `dead`     |

---

## Execution
Execute on Google Colab
