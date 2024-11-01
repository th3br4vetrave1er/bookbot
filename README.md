# 📚 Bookbot CLI Companion 🤖

Hello there, brave reader! 👋 Welcome to **Bookbot**, your friendly terminal buddy who digs into .txt books, counts words, and sniffs out the most common letters! All you need is a book path, and you're off to the races.

> **Note:** This is my first project, so it’s a little rough around the edges, but hey, we're all learning here, right? 🎓

---

## 🧐 What Does This Do?

This is a super simple script that:
1. 📥 Takes a book file path as input.
2. 📖 Reads the file.
3. 🔍 Counts all the words in the book.
4. 🔢 Tally up each letter from A to Z.
5. 📊 Reports the most frequent characters!

It’s like having your own librarian who loves numbers. Perfect for those curious about letter frequency or anyone who loves data in text!

---

## 🚀 How to Run It

Just fire up the command line, and type:

```bash
python3 bookbot.py
```

When prompted, enter the path to your .txt file (yes, the full path, we’re picky like that 😅):

```bash
Enter your book path: /path/to/your/book.txt
```

And voila! Your report is ready.

---

## 📜 Example Output

Here's what to expect:

```
--- Begin report of /path/to/your/book.txt ---
2154 words found in the document
The 'e' character was found 1340 times
The 't' character was found 1012 times
...
--- End report ---
```

---

## 🛠 Code Breakdown

A quick tour of the main functions:

- **`file_path(path)`** - Opens and reads the book file.
- **`word_counter(book)`** - Counts the words.
- **`char_dict(source)`** - Tallies up each letter’s frequency.
- **`main()`** - The main flow, where all the magic happens!

---

## 🎯 Goals

This project is just the beginning. Future upgrades might include:
- 🎨 Fancy formatting!
- 📈 Graphs for character distribution!
- 🤔 More file format support (PDF, EPUB, who knows!)

---

## 📚 About the Author

A newbie coder and a *brave traveler* in the world of programming, learning one line at a time.