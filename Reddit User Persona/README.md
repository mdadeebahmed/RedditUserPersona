# Reddit User Persona Extractor

This project takes a Reddit user's profile URL, scrapes their recent public posts and comments, and uses an LLM (like GPT-3.5 or GPT-4) to generate a detailed qualitative **user persona** — including citations to specific posts or comments that contributed to each trait.

## Example Output

Sample persona files are included for the following Reddit users:
- [`kojied_persona.txt`](users/kojied_persona.txt)
- [`Hungry-Move-6603_persona.txt`](users/Hungry-Move-6603_persona.txt)

Each output describes:
- Estimated age, location, personality traits
- Hobbies, interests, pain points
- Reddit usage style
- Representative quotes with post links

---

## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/mdadeebahmed/RedditUserPersona.git
cd reddit-user-persona
