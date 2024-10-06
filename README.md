# basic_text_analysis_tool
<br>
<p1>
 <b> Objective:</b>
this is a Python program that analyzes a string of text input by the user. The 
program will provide various types of text analysis, including counting words, 
characters, and sentences, and analyzing word frequency. It will also include 
functionality to identify the longest word, the most common word, and assess the 
readability of the text.
<b>Features:</b>
1. User Input:
 - Prompt the user to enter a string of text for analysis.
 - Handle multi-line input if necessary, allowing users to input longer passages.
2. Text Analysis Components:
 A. Word Count:
 - Calculate the total number of words in the text. 
 - Words are defined as sequences of characters separated by spaces or 
punctuation.
 
 B. Character Count:
 - Count the total number of characters in the text, including spaces.
 - Count the number of characters excluding spaces.
 C. Sentence Count:
 - Count the total number of sentences in the text. 
 - Sentences are typically defined by the presence of punctuation marks such as 
periods (.), exclamation points (!), or question marks (?).
 D. Word Frequency:
 - Analyze the frequency of each word in the text.
 - Display a sorted list of words by frequency, showing the most frequent words 
first.
 E. Longest Word:
 - Identify the longest word in the text. 
 - If there are multiple words of the same maximum length, display all of them.
 F. Most Common Word:
 - Determine the most frequently occurring word in the text. 
 - In case of a tie, display all words with the highest frequency.
 G. Readability Analysis (Optional):
 - Calculate readability metrics such as the Flesch-Kincaid readability score.
 - Provide an indication of the text’s readability level (e.g., grade level).
3. Output Formatting:
 A. Display Results:
 - Present the analysis results in a clear, formatted manner.
 - Use headers and bullet points for readability.
 B. Example Output:
 Text Analysis Results
 Total Words: 120
 Total Characters (including spaces): 800
 Total Characters (excluding spaces): 680
 Total Sentences: 8
 Word Frequency:
 - the: 25
 - and: 15
 - to: 12
 - of: 10
 - in: 8
 Longest Word(s):
 - Phenomenal (10 characters)
 Most Common Word(s):
 - the (25 occurrences)
 Readability Analysis:
 - Flesch-Kincaid Grade Level: 8.2
4. Input Validation:
 - Ensure the text input is valid and non-empty.
 - Handle edge cases such as very short texts or texts with unusual formatting.
5. Error Handling:
 - Provide meaningful error messages if the input cannot be processed.
 - Handle cases where text analysis operations fail due to unexpected input
</p1>
