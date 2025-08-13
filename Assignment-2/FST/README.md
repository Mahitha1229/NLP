# Finite State Transducer (FST) for Noun Pluralization

This project simulates a **Finite State Transducer (FST)** that processes nouns from the Brown corpus and generates their **morphological features** in both singular and plural forms.

---

## Objective

- Read nouns from `brown_nouns.txt`
- Apply pluralization rules using FST logic
- Output morphological tags in the format:  
  `root+N+SG` for singular  
  `root+N+PL` for plural
- Reject invalid pluralizations with `"Invalid Word"`

---

## 🔤 Morphological Tags

| Tag | Meaning     |
|-----|-------------|
| `N` | Noun        |
| `SG`| Singular    |
| `PL`| Plural      |

Example:
jury = jury+N+SG  juries+N+PL


---

## Pluralization Rules

| Rule Name       | Description                                           | Example             |
|-----------------|-------------------------------------------------------|---------------------|
| E Insertion     | Add `e` before `s` if word ends in `s`, `z`, `x`, `ch`, `sh` | `fox` → `foxes`     |
| Y Replacement   | Replace `y` with `ie` before adding `s` if preceded by a consonant | `try` → `tries`     |
| S Addition      | Add `s` for regular nouns                             | `bag` → `bags`      |
| Invalid Filter  | Prevent pluralizing words that are already plural     | `thanks` → Invalid  |

---

## Sample Output
investigation = investigation+N+SG | investigations+N+PL 
primary = primary+N+SG | primaries+N+PL 
election = election+N+SG | elections+N+PL 
thanks = thanks+N+SG | Invalid Word 
irregularities = irregularities+N+SG | Invalid Word

## Execution
Execute on Goggle Colab
