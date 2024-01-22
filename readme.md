# Flashcard Learning App🗃️

## Overviewℹ️

This is a simple flashcard learning app designed to help users practice and learn new Korean words efficiently. The app sources its initial set of words from the 1000 most frequent Korean words provided by the National Institute of the Korean Language. The app allows users to interact with flashcards, testing their knowledge of Korean words and removing familiar words from the practice list.

## Features✨

- **Flashcards:** The app uses a flashcard-style interface to present users with Korean words on one side and prompts them to recall the corresponding English translation.

- **Filtering:** Once a user correctly identifies a word, it is removed from the current study list. This way, users can focus on practicing unfamiliar words rather than repeatedly going through words they already know.

- **Persistence:** The app stores the current study list in a CSV file (`data/new_word.csv`). This file allows users to continue their learning progress even if they close and reopen the application.

## Dependencies🔎

- **Python:** The app is written in Python and requires a Python interpreter to run.

- **Tkinter:** The app uses the Tkinter library for the graphical user interface.

- **Pandas:** The Pandas library is used for reading and manipulating the CSV data.

## How to Use❓

1. Upon launching the app, the initial set of Korean words is loaded from `data/korean_vocab_1000.csv` 

2. Click on the "Right" button if you know the English translation of the displayed Korean word.

3. The app will remove the correctly identified word from the current study list and display a new flashcard.

4. Click on the "Wrong" button if you want to try the word again.

5. The app will save your progress in `data/new_word.csv` for future sessions.

## Contributing

If you have suggestions or would like to contribute to the project, please fork the repository and submit a pull request. 
---

![image](https://github.com/chaw-thiri/Korean_flashcard_project-/assets/113085742/c2452b87-478e-4297-a504-29fded20a9b0)
